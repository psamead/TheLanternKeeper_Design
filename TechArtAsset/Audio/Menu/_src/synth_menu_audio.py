"""Lantern Keeper - start-menu audio v1 (all procedurally synthesized, no samples).
Outputs WAV (master) to OUT dir; OGG conversion done separately with ffmpeg.
"""
import sys, os
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 44100
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- helpers
def t_axis(dur):
    return np.arange(int(dur * SR)) / SR

def noise(n, color="white"):
    w = rng.standard_normal(n)
    if color == "white":
        return w
    if color == "pink":  # Voss-ish via filter
        b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
        a = [1, -2.494956002, 2.017265875, -0.522189400]
        return signal.lfilter(b, a, w) * 4
    if color == "brown":
        x = np.cumsum(w)
        x = signal.lfilter([1, -1], [1, -0.999], x)  # DC block
        return x / (np.std(x) + 1e-9)

def bp(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, hi], btype="band", fs=SR, output="sos")
    return signal.sosfilt(sos, x)

def lp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, fs=SR, output="sos"), x)

def hp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, btype="high", fs=SR, output="sos"), x)

def smooth_env(n, knots_t, knots_v):
    """Smooth (cosine-interpolated) envelope through knots (times in s)."""
    t = np.arange(n) / SR
    v = np.interp(t, knots_t, knots_v)
    return lp(np.concatenate([v, v[-1:].repeat(2000)]), 30, 1)[:n]

def svf_sweep(x, fc, q):
    """State-variable bandpass with per-sample centre freq array fc (Hz)."""
    y = np.zeros_like(x)
    low = band = 0.0
    f = 2 * np.sin(np.pi * np.clip(fc, 20, SR / 6) / SR)
    damp = 1.0 / q
    for i in range(len(x)):
        high = x[i] - low - damp * band
        band += f[i] * high
        low += f[i] * band
        y[i] = band
    return y

def slow_random(n, rate_hz, seed):
    r = np.random.default_rng(seed)
    k = max(4, int(n / SR * rate_hz) + 4)
    pts = r.standard_normal(k)
    xs = np.linspace(0, n, k)
    v = np.interp(np.arange(n), xs, pts)
    return lp(v, rate_hz * 1.5, 2)

def reverb_ir(dur=2.6, predelay=0.02, damp_hz=5000, seed=3):
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    ir = np.zeros((n, 2))
    for c in range(2):
        e = r.standard_normal(n) * np.exp(-t * 6.9 / dur)
        e = lp(e, damp_hz, 1)
        ir[:, c] = e
    pd = np.zeros((int(predelay * SR), 2))
    ir = np.vstack([pd, ir])
    return ir / np.sqrt(np.sum(ir ** 2, axis=0, keepdims=True))

def add_reverb(st, wet=0.25, **kw):
    ir = reverb_ir(**kw)
    out = np.zeros((st.shape[0] + ir.shape[0] - 1, 2))
    for c in range(2):
        out[:, c] = signal.fftconvolve(st[:, c], ir[:, c])
    dry = np.vstack([st, np.zeros((ir.shape[0] - 1, 2))])
    return dry * (1 - wet) + out * wet

def pan(mono, p):  # p -1..1, equal power
    a = (p + 1) * np.pi / 4
    return np.stack([mono * np.cos(a), mono * np.sin(a)], axis=1)

def fade(x, fin=0.003, fout=0.02):
    n = len(x)
    e = np.ones(n)
    a, b = int(fin * SR), int(fout * SR)
    if a: e[:a] = np.linspace(0, 1, a)
    if b: e[-b:] *= np.linspace(1, 0, b)
    return x * (e[:, None] if x.ndim == 2 else e)

def norm(x, peak_db=-3.0):
    return x / (np.max(np.abs(x)) + 1e-9) * 10 ** (peak_db / 20)

def trim(x, db=-55):
    m = np.max(np.abs(x), axis=1) if x.ndim == 2 else np.abs(x)
    idx = np.where(m > 10 ** (db / 20))[0]
    end = min(len(x), idx[-1] + int(0.02 * SR)) if len(idx) else len(x)
    return fade(x[:end], 0, 0.05)

def save(name, x, do_trim=True):
    if do_trim: x = trim(x)
    x = np.clip(x, -1, 1)
    wavfile.write(os.path.join(OUT, name + ".wav"), SR, (x * 32767).astype(np.int16))
    print("wrote", name, f"{len(x)/SR:.2f}s")

def make_loop(x, loop_len):
    """x longer than loop_len; fold the tail back onto the head -> seamless loop."""
    n = int(loop_len * SR)
    y = x[:n].copy()
    tail = x[n:]
    y[: len(tail)] += tail[: n]
    return y

# ---------------------------------------------------------------- sea & wind
def wave_event(dur, strength=1.0, seed=0, bright=1.0):
    """One wave: low swell -> break (broadband) -> foam fizz receding."""
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    swell_t = dur * r.uniform(0.32, 0.42)
    lowb = lp(noise(n, "brown"), 380)
    mid = bp(noise(n, "pink"), 350, 1800)
    high = bp(noise(n), 1800, 9000 * bright)
    e_low = smooth_env(n, [0, swell_t, swell_t + 0.5, dur], [0, 1, 0.55, 0])
    e_mid = smooth_env(n, [0, swell_t * 0.8, swell_t + 0.15, swell_t + 1.0, dur], [0, 0.25, 1, 0.45, 0])
    e_hi = smooth_env(n, [0, swell_t, swell_t + 0.25, dur * 0.85, dur], [0, 0.05, 0.9, 0.25, 0])
    # foam: sparse crackle
    crackle = (r.random(n) < 0.004) * r.standard_normal(n)
    crackle = bp(crackle, 2500, 9000) * 6
    e_fz = smooth_env(n, [0, swell_t + 0.2, swell_t + 0.6, dur], [0, 0, 1, 0])
    m = 0.9 * lowb * e_low + 0.6 * mid * e_mid + 0.35 * high * e_hi + 0.25 * crackle * e_fz
    return m * strength

def wind(dur, seed=11, base=420, depth=0.6, gust_rate=0.12):
    n = int(dur * SR)
    g = slow_random(n, gust_rate, seed)
    g = (g - g.min()) / (np.ptp(g) + 1e-9)
    fc = base * (1 + depth * (g - 0.5)) + 40 * slow_random(n, 0.8, seed + 1)
    src = noise(n, "pink")
    whistle = svf_sweep(src, fc, q=7) * 0.5
    body = lp(noise(n, "brown"), 250) * 0.6
    air = bp(src, 1500, 5000) * 0.15
    amp = 0.35 + 0.65 * g
    return (whistle + body + air) * amp

# ---------------------------------------------------------------- struck objects
def modal(freqs, decays, amps, dur, strike_noise=0.0, strike_bp=(2000, 8000), seed=0):
    t = t_axis(dur)
    r = np.random.default_rng(seed)
    y = np.zeros_like(t)
    for f, d, a in zip(freqs, decays, amps):
        ph = r.uniform(0, 2 * np.pi)
        y += a * np.sin(2 * np.pi * f * t + ph) * np.exp(-t / d)
    if strike_noise:
        nb = bp(r.standard_normal(len(t)), *strike_bp) * np.exp(-t / 0.004)
        y += strike_noise * nb
    att = np.clip(t / 0.0015, 0, 1)
    return y * att

def brass_ting(f0=1180, dur=1.6, seed=0, bright=1.0):
    # small brass lantern bell: inharmonic, paired partials for gentle beating
    ratios = [1.0, 1.003, 2.32, 2.33, 4.07, 5.6, 7.2]
    decays = [1.1, 1.0, 0.55, 0.5, 0.25, 0.14, 0.08]
    amps = [1.0, 0.6, 0.45 * bright, 0.3 * bright, 0.22 * bright, 0.12 * bright, 0.07 * bright]
    return modal([f0 * r for r in ratios], decays, amps, dur, strike_noise=0.25, strike_bp=(3000, 10000), seed=seed)

def wood_knock(f0=330, dur=0.35, seed=0):
    ratios = [1.0, 2.57, 4.21, 6.1]
    decays = [0.060, 0.030, 0.018, 0.010]
    amps = [1.0, 0.55, 0.3, 0.15]
    y = modal([f0 * r for r in ratios], decays, amps, dur, strike_noise=0.6, strike_bp=(800, 4000), seed=seed)
    return lp(y, 3500)

def rope_creak(dur=0.45, seed=0):
    """Short damp wood/rope creak: band-limited stick-slip pulse train."""
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    rate = 90 + 40 * np.sin(np.pi * t / dur)  # pulses/sec
    ph = np.cumsum(rate / SR)
    pulses = (np.diff(np.floor(ph), prepend=0) > 0).astype(float) * (0.6 + 0.4 * r.random(n))
    y = bp(pulses, 300, 1600) * 3
    y = svf_sweep(y, 600 + 250 * np.sin(np.pi * t / dur), 5)
    return y * np.sin(np.pi * t / dur) ** 1.5

# ================================================================ SFX
def sfx_hover(seed, dur=0.75):
    """A tiny wave lap on stone + a breath of wind. Short, soft."""
    n = int(dur * SR)
    w = wave_event(dur, seed=seed, bright=0.8)
    # compress the swell earlier for snappier response: re-envelope
    e = smooth_env(n, [0, 0.07, 0.22, 0.5, dur], [0, 1, 0.6, 0.2, 0])
    w = w * e
    wi = wind(dur, seed=seed + 50, base=700, depth=0.4, gust_rate=2.0) * smooth_env(n, [0, 0.1, dur * 0.6, dur], [0, 0.35, 0.15, 0])
    m = pan(w, 0.0) * 1.0
    m[:, 0] += wi * 0.6
    m[:, 1] += np.roll(wi, 300) * 0.6
    m = lp(m.T, 4200, 2).T  # softer, less hiss
    m = add_reverb(m, wet=0.18, dur=0.8)
    return fade(norm(m, -9), 0.004, 0.15)

def sfx_confirm(seed=1):
    """Lift the lantern: wooden handle knock + brass ting + soft wave swell."""
    dur = 2.2
    n = int(dur * SR)
    out = np.zeros((n, 2))
    k = wood_knock(300, 0.4, seed)
    out[: len(k)] += pan(k, -0.1) * 0.55
    off = int(0.035 * SR)
    b = brass_ting(1180, 1.8, seed)
    b2 = brass_ting(1180 * 1.498, 1.2, seed + 1, bright=0.6)  # faint fifth sympathetic ring
    out[off: off + len(b)] += pan(b, 0.15) * 0.55
    out[off + 600: off + 600 + len(b2)] += pan(b2, 0.25) * 0.12
    w = wave_event(dur, seed=seed + 9, strength=0.35, bright=0.7)
    out += pan(w, 0) * 0.35
    out = add_reverb(out, wet=0.28, dur=2.2)
    return fade(norm(out, -4), 0.002, 0.3)

def sfx_back(seed=2):
    """Close / back: soft wood knock + damp rope creak."""
    dur = 0.8
    n = int(dur * SR)
    out = np.zeros((n, 2))
    c = rope_creak(0.4, seed)
    out[: len(c)] += pan(c, -0.2) * 0.35
    k = wood_knock(240, 0.35, seed + 3)
    o = int(0.28 * SR)
    out[o: o + len(k)] += pan(k, 0.1) * 0.7
    out = add_reverb(out, wet=0.2, dur=1.2)
    return fade(norm(out, -7), 0.002, 0.1)

# ================================================================ ambience loop
def ambience(loop_len=60.0):
    total = loop_len + 6
    n = int(total * SR)
    st = np.zeros((n, 2))
    r = np.random.default_rng(21)
    tpos = 0.3
    i = 0
    while tpos < total - 1:
        d = r.uniform(6.5, 9.5)
        w = wave_event(d, strength=r.uniform(0.7, 1.0), seed=100 + i, bright=r.uniform(0.7, 1.0))
        p = r.uniform(-0.45, 0.45)
        s = int(tpos * SR)
        e = min(n, s + len(w))
        st[s:e] += pan(w[: e - s], p)
        tpos += r.uniform(4.5, 7.5)
        i += 1
    wl = wind(total, seed=31, base=380, depth=0.7, gust_rate=0.1)
    wr = wind(total, seed=32, base=430, depth=0.7, gust_rate=0.1)
    st[:, 0] += wl * 0.35
    st[:, 1] += wr * 0.35
    st = add_reverb(st, wet=0.15, dur=1.8)
    loop = make_loop(st, loop_len)
    return norm(loop, -6)

# ================================================================ music
def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)

def harp_note(midi, dur=3.5, vel=1.0):
    f = mtof(midi)
    t = t_axis(dur)
    y = np.zeros_like(t)
    B = 0.00015  # slight inharmonicity
    for k in range(1, 14):
        fk = f * k * np.sqrt(1 + B * k * k)
        if fk > SR / 2.2: break
        a = (1 / k ** 1.25) * (0.6 + 0.4 * np.sin(np.pi * k * 0.13) ** 2)  # pluck point colouring
        d = (2.6 if midi < 55 else 1.9) / (1 + 0.35 * (k - 1)) * (220 / max(f, 110)) ** 0.25
        y += a * np.sin(2 * np.pi * fk * t) * np.exp(-t / d)
    y *= np.clip(t / 0.004, 0, 1)
    y += 0.04 * bp(rng.standard_normal(len(t)), 1500, 6000) * np.exp(-t / 0.006)
    return y * vel

def whistle_note(midi, dur, vel=1.0):
    """Low whistle / wooden flute: near-sine with breath, delayed vibrato."""
    f = mtof(midi)
    t = t_axis(dur + 0.25)
    vib = 1 + 0.006 * np.sin(2 * np.pi * 5.2 * t) * np.clip((t - 0.35) / 0.4, 0, 1)
    ph = 2 * np.pi * np.cumsum(f * vib) / SR
    tone = np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph)
    breath = bp(rng.standard_normal(len(t)), f * 0.8, min(f * 3.5, 12000)) * 0.12
    env = np.interp(t, [0, 0.07, 0.2, dur - 0.05, dur + 0.25], [0, 0.85, 0.75, 0.68, 0])
    env = lp(env, 40, 1)
    return (tone + breath) * env * vel

def drone(dur, root=50):
    t = t_axis(dur)
    y = np.zeros_like(t)
    for m, a in [(root - 12, 0.5), (root, 0.35), (root + 7, 0.22)]:
        f = mtof(m)
        for k, ak in [(1, 1), (2, 0.35), (3, 0.15), (4, 0.06)]:
            y += a * ak * np.sin(2 * np.pi * f * k * t * (1 + 0.0007 * k) + k)
    lfo = 0.75 + 0.25 * np.sin(2 * np.pi * t / 11.0)
    return lp(y, 900) * lfo

CHORDS = {  # root(midi, octave 3), chord tones semitones
    "Dm": (50, [0, 7, 12, 15, 19, 24]),
    "C": (48, [0, 7, 12, 16, 19, 24]),
    "Am": (45, [0, 7, 12, 15, 19, 24]),
    "F": (53, [0, 7, 12, 16, 19, 24]),
    "G": (43, [0, 7, 12, 16, 19, 24]),
}
PROG = ["Dm", "Dm", "C", "C", "Dm", "Am", "F", "C", "F", "F", "C", "C", "G", "G", "Dm", "Dm"]
MELODY = [  # (midi, beats) per bar, D dorian, 3/4
    [(74, 2), (72, 1)], [(69, 3)], [(67, 1), (69, 1), (72, 1)], [(67, 3)],
    [(65, 1), (67, 1), (69, 1)], [(72, 2), (69, 1)], [(69, 1), (67, 1), (65, 1)], [(64, 3)],
    [(65, 2), (69, 1)], [(72, 3)], [(74, 2), (72, 1)], [(67, 3)],
    [(71, 2), (69, 1)], [(67, 1), (69, 1), (71, 1)], [(69, 1), (65, 1), (64, 1)], [(62, 3)],
]

def bgm(bpm=72):
    beat = 60 / bpm
    bar = 3 * beat
    bars = len(PROG) * 2  # pass 1 harp+drone, pass 2 + whistle
    loop_len = bars * bar
    total = loop_len + 6
    n = int(total * SR)
    harp = np.zeros(n); lead = np.zeros(n)
    r = np.random.default_rng(5)
    for b in range(bars):
        name = PROG[b % len(PROG)]
        root, tones = CHORDS[name]
        start = b * bar
        # 6 eighth notes rising arpeggio; in pass 2 slightly varied
        pattern = tones if (b // len(PROG)) == 0 else [tones[i] for i in (0, 1, 2, 4, 3, 2)]
        for i, st in enumerate(pattern):
            tt = max(0.0, start + i * beat / 2 + r.normal(0, 0.006))
            vel = (0.9 if i == 0 else 0.55) * r.uniform(0.85, 1.05)
            note = harp_note(root + st, 3.2, vel)
            s = int(tt * SR)
            harp[s: s + len(note)] += note[: n - s]
    # whistle only on 2nd pass
    for b in range(len(PROG)):
        tt = (len(PROG) + b) * bar
        for midi, beats in MELODY[b]:
            d = beats * beat
            note = whistle_note(midi, d * 0.97, 0.9)
            s = int(tt * SR)
            lead[s: s + len(note)] += note[: n - s]
            tt += d
    dr = drone(total) * 0.35
    st = pan(harp, 0.25) * 0.55 + pan(lead, -0.2) * 0.42 + pan(dr, 0) * 0.5
    st = add_reverb(st, wet=0.32, dur=3.2, damp_hz=4500)
    loop = make_loop(st, loop_len)
    print(f"BGM loop length {loop_len:.2f}s")
    return norm(loop, -2.0)

if __name__ == "__main__":
    which = sys.argv[2:] or ["sfx", "amb", "bgm"]
    if "sfx" in which:
        for i in range(3):
            save(f"SFX_Menu_Hover_Wave_0{i+1}", sfx_hover(40 + i * 7))
        save("SFX_Menu_Confirm_Lantern", sfx_confirm())
        save("SFX_Menu_Back_Wood", sfx_back())
    if "amb" in which:
        save("AMB_Menu_SeaWind_loop", ambience(), False)
    if "bgm" in which:
        save("BGM_Menu_Gwerz_loop", bgm(), False)

# ---------------------------------------------------------------- v2 hover (2026-11-03)
def sfx_hover_v2(seed, dur=0.7):
    """Immediate wave lap: loudest within ~15 ms, then foam recedes. Follows fast mouse sweeps."""
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    low = lp(noise(n, "brown"), 420)
    mid = bp(noise(n, "pink"), 300, 1600)
    hi = bp(noise(n), 1600, 5500)
    att = np.clip(t / 0.012, 0, 1)
    e_low = att * np.exp(-t / 0.16)
    e_mid = att * np.exp(-t / 0.22)
    e_hi = np.clip(t / 0.03, 0, 1) * np.exp(-t / 0.30) * (0.6 + 0.4 * np.sin(np.pi * np.clip(t / 0.4, 0, 1)))
    crackle = bp((r.random(n) < 0.004) * r.standard_normal(n), 2500, 7000) * 5 * np.exp(-t / 0.35)
    m = 0.9 * low * e_low + 0.7 * mid * e_mid + 0.3 * hi * e_hi + 0.2 * crackle
    st = pan(m, r.uniform(-0.15, 0.15))
    st = lp(st.T, 4200, 2).T
    st = add_reverb(st, wet=0.15, dur=0.6)
    return fade(norm(st, -9), 0.002, 0.12)

if __name__ == "__main__" and "hover2" in sys.argv[2:]:
    for i in range(3):
        save(f"SFX_Menu_Hover_Wave_0{i+1}", sfx_hover_v2(70 + i * 9))

# ---------------------------------------------------------------- v3 hover: peak within 5-10 ms
def sfx_hover_v3(seed, dur=0.7):
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    low = lp(noise(n, "brown"), 420)
    mid = bp(noise(n, "pink"), 300, 1600)
    hi = bp(noise(n), 1600, 5500)
    att = np.clip(t / 0.004, 0, 1)                      # 4 ms attack
    e_low = att * np.exp(-t / 0.14)
    e_mid = att * np.exp(-t / 0.20)
    e_hi = att * np.exp(-t / 0.28)
    crackle = bp((r.random(n) < 0.004) * r.standard_normal(n), 2500, 7000) * 5 * np.exp(-t / 0.3)
    slap = bp(noise(n, "pink"), 180, 3200)
    slap = slap / (np.std(slap[: int(0.03 * SR)]) + 1e-9)
    e_slap = att * np.exp(-t / 0.010)                   # water slapping stone: ~10 ms burst
    body = 0.9 * low * e_low + 0.75 * mid * e_mid + 0.3 * hi * e_hi + 0.2 * crackle
    sl = slap * e_slap
    sl = sl / (np.max(np.abs(sl)) + 1e-9)
    body = body / (np.max(np.abs(body)) + 1e-9)
    m = 1.8 * sl + 0.4 * body                            # slap always the loudest moment
    st = pan(m, r.uniform(-0.15, 0.15))
    st = lp(st.T, 4200, 2).T
    st = add_reverb(st, wet=0.12, dur=0.5)
    return fade(norm(st, -9), 0.001, 0.12)

if __name__ == "__main__" and "hover3" in sys.argv[2:]:
    for i in range(3):
        save(f"SFX_Menu_Hover_Wave_0{i+1}", sfx_hover_v3(90 + i * 11))
