"""Lantern Keeper - Prologue + Home audio v1 (2026-11-08). Procedural, reuses helpers of the menu synth.
Usage: python synth_prologue_home_audio.py <out_dir> [bgm amb home sfx]
Flow clip (Google Flow, user's own generation) is mixed into the prologue ambience once per loop.
"""
import sys, os, importlib.util
import numpy as np
from scipy import signal
from scipy.io import wavfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("m", os.path.join(HERE, "../../Menu/_src/synth_menu_audio.py"))
sys_argv = sys.argv; sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else "out", "none"]
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); sys.argv = sys_argv
from_m = ["SR", "noise", "bp", "lp", "hp", "smooth_env", "slow_random", "add_reverb", "pan", "fade", "norm",
          "make_loop", "wave_event", "wind", "modal", "brass_ting", "wood_knock", "rope_creak", "harp_note",
          "whistle_note", "drone", "t_axis", "mtof"]
globals().update({k: getattr(m, k) for k in from_m})
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"; os.makedirs(OUT, exist_ok=True)

def save(name, x, do_trim=False):
    if do_trim: x = m.trim(x, -50)
    x = np.clip(x, -1, 1); wavfile.write(os.path.join(OUT, name + ".wav"), SR, (x * 32767).astype(np.int16))
    print("wrote", name, f"{len(x)/SR:.2f}s")

# ============================================================ Prologue BGM: "Ar Mor Du" (the dark sea)
# Slower and sparser than the menu Gwerz: D aeolian, 3/4 at 60 bpm, harp alone first, whistle enters
# half-way and ends on an unresolved A (prologue leads into the story; loop returns to Dm).
PROG = ["Dm", "Dm", "Bb", "Bb", "F", "F", "C", "C", "Dm", "Dm", "Gm", "Gm", "Bb", "C", "Am", "Am"]
CH = {"Dm": (50, [0, 7, 12, 15, 19]), "Bb": (46, [0, 7, 12, 16, 19]), "F": (53, [0, 7, 12, 16, 19]),
      "C": (48, [0, 7, 12, 16, 19]), "Gm": (43, [0, 7, 12, 15, 19]), "Am": (45, [0, 7, 12, 15, 19])}
MEL = [[(69, 3)], [(70, 1), (69, 1), (67, 1)], [(65, 3)], [(62, 3)],
       [(65, 2), (67, 1)], [(69, 3)], [(67, 2), (64, 1)], [(64, 3)],
       [(62, 2), (65, 1)], [(69, 2), (70, 1)], [(70, 2), (69, 1)], [(67, 3)],
       [(65, 2), (62, 1)], [(64, 3)], [(69, 3)], [(None, 3)]]

def bgm_prologue(bpm=60):
    beat = 60 / bpm; bar = 3 * beat; bars = len(PROG) * 2; L = bars * bar; total = L + 7
    n = int(total * SR); harp = np.zeros(n); lead = np.zeros(n); r = np.random.default_rng(15)
    for b in range(bars):
        root, tones = CH[PROG[b % len(PROG)]]
        # sparse: bass + 2-3 tones, dotted rhythm
        hits = [(0, tones[0], .9), (1.0, tones[1], .45), (1.5, tones[2], .5), (2.25, tones[3 + (b % 2)], .4)]
        if b % 4 == 3: hits = hits[:2]
        for pos, st, v in hits:
            tt = max(0, b * bar + pos * beat + r.normal(0, .008)); s = int(tt * SR)
            note = harp_note(root + st, 4.0, v * r.uniform(.85, 1.05)); harp[s:s + len(note)] += note[:n - s]
    for b in range(len(PROG)):
        tt = (len(PROG) + b) * bar
        for mid, beats in MEL[b]:
            d = beats * beat
            if mid is not None:
                note = whistle_note(mid, d * .96, .8); s = int(tt * SR); lead[s:s + len(note)] += note[:n - s]
            tt += d
    dr = drone(total, root=50) * .4
    st = pan(harp, .2) * .6 + pan(lead, -.25) * .38 + pan(lp(dr, 600), 0) * .55
    st = add_reverb(st, wet=.4, dur=4.0, damp_hz=3800)
    loop = make_loop(st, L); print(f"Prologue BGM loop {L:.2f}s"); return norm(loop, -3)

# ============================================================ Prologue ambience: sea + wind + Flow clip
def load_flow():
    p = os.path.join(HERE, "../SB_P1_flow_v1_ambience.wav")
    sr, x = wavfile.read(p); x = x.astype(float) / 32768
    x = signal.resample_poly(x, SR, sr, axis=0)  # 48k -> 44.1k
    return x

def amb_prologue(L=48.0):
    total = L + 6; n = int(total * SR); st = np.zeros((n, 2)); r = np.random.default_rng(41); t = .5; i = 0
    while t < total - 1:
        d = r.uniform(7, 10); w = wave_event(d, r.uniform(.6, .95), seed=300 + i, bright=r.uniform(.6, .85))
        s = int(t * SR); e = min(n, s + len(w)); st[s:e] += pan(w[:e - s], r.uniform(-.5, .5)); t += r.uniform(5, 8); i += 1
    st[:, 0] += wind(total, 51, 360, .8, .08) * .45; st[:, 1] += wind(total, 52, 400, .8, .08) * .45
    st = norm(st, -8)
    f = load_flow(); f = f / (np.max(np.abs(f)) + 1e-9) * 10 ** (-9 / 20)
    k = len(f); e = np.ones(k); a = int(1.5 * SR); e[:a] = np.linspace(0, 1, a); e[-a:] = np.linspace(1, 0, a)
    s = int(14 * SR); st[s:s + k] += f * e[:, None]
    st = add_reverb(st, wet=.12, dur=1.6)
    return norm(make_loop(st, L), -6)

# ============================================================ Home interior ambience
def clock_tick(seed, hi=True):
    y = modal([2900 if hi else 2500, 4100, 6200], [.006, .004, .003], [1, .5, .3], .05, .4, (2000, 8000), seed)
    return hp(y, 1200)

def fire_crackle(n, seed):
    r = np.random.default_rng(seed); y = np.zeros(n)
    pops = np.where(r.random(n) < 2.2 / SR)[0]
    for p in pops:
        d = int(r.uniform(.005, .02) * SR); b = bp(r.standard_normal(d), 1500, 7000) * np.exp(-np.arange(d) / (d / 4))
        y[p:p + d] += b[:n - p] * r.uniform(.2, 1)
    hiss = lp(noise(n, "pink"), 900) * .04
    return y + hiss

def amb_home(L=40.0):
    total = L + 4; n = int(total * SR); st = np.zeros((n, 2)); r = np.random.default_rng(61)
    # outside: wind + waves through walls (heavy lowpass)
    out = np.zeros((n, 2)); t = .5; i = 0
    while t < total - 1:
        w = wave_event(r.uniform(7, 10), .7, seed=500 + i, bright=.5); s = int(t * SR); e = min(n, s + len(w))
        out[s:e] += pan(w[:e - s], r.uniform(-.3, .3)); t += r.uniform(6, 9); i += 1
    out[:, 0] += wind(total, 71, 300, .9, .07) * .6; out[:, 1] += wind(total, 72, 330, .9, .07) * .6
    out = lp(out.T, 450, 2).T; st += norm(out, -14)
    # room: clock (1 s, tick-tock) left, fire right, rare beam creaks
    clk = np.zeros(n)
    for k in range(int(total)):
        c = clock_tick(k % 7, k % 2 == 0); s = int((k + .25) * SR); clk[s:s + len(c)] += c[:n - s]
    st += pan(clk, -.55) * 10 ** (-30 / 20) / (np.max(np.abs(clk)) + 1e-9)
    fc = fire_crackle(n, 62); st += pan(fc, .5) * 10 ** (-27 / 20) / (np.max(np.abs(fc)) + 1e-9)
    for tt in (9.0, 27.5):
        c = rope_creak(.6, int(tt)); c = lp(c, 1400); s = int(tt * SR)
        st[s:s + len(c)] += pan(c, r.uniform(-.4, .4)) * 10 ** (-26 / 20) / (np.max(np.abs(c)) + 1e-9)
    st = add_reverb(st, wet=.2, dur=.7, damp_hz=3000)
    return norm(make_loop(st, L), -10)

# ============================================================ Maela SFX (small girl, rain boots, wood floor)
def footstep(seed):
    r = np.random.default_rng(seed); dur = .28; n = int(dur * SR); t = np.arange(n) / SR
    heel = wood_knock(r.uniform(115, 150), .25, seed) * .9
    rubber = lp(bp(noise(n, "pink"), 150, 900) * np.clip(t / .003, 0, 1) * np.exp(-t / .025), 1200) * .6
    scuff = bp(noise(n), 1500, 5000) * smooth_env(n, [0, .02, .05, .12, dur], [0, 0, .25, 0, 0]) * .25
    y = rubber + scuff; y[:len(heel)] += heel
    st = pan(y, r.uniform(-.1, .1)); st = add_reverb(st, .12, dur=.5, damp_hz=4000)
    return fade(norm(st, -10 - r.uniform(0, 1.5)), .001, .05)

def cloth_whoosh(dur, seed, up=True):
    n = int(dur * SR); t = np.arange(n) / SR
    fc = np.linspace(500, 1400, n) if up else np.linspace(1300, 500, n)
    from scipy.signal import sosfilt
    src = noise(n, "pink"); y = m.svf_sweep(src, fc, 1.5)
    return y * np.sin(np.pi * t / dur) ** 2

def sfx_jump(seed):
    dur = .45; n = int(dur * SR); out = np.zeros(n)
    push = footstep(seed)[:, 0] * .8; out[:len(push)] += push[:n]
    w = cloth_whoosh(.35, seed); s = int(.03 * SR); out[s:s + len(w)] += w[:n - s] * .5 / (np.max(np.abs(w)) + 1e-9) * np.max(np.abs(push))
    st = pan(out, 0); return fade(norm(st, -11), .001, .06)

def sfx_land(seed):
    r = np.random.default_rng(seed); dur = .5; n = int(dur * SR); t = np.arange(n) / SR
    thump = lp(noise(n, "brown"), 220) * np.clip(t / .002, 0, 1) * np.exp(-t / .05) * 1.4
    k1 = wood_knock(r.uniform(95, 115), .3, seed); k2 = wood_knock(r.uniform(120, 140), .3, seed + 1)
    y = thump.copy(); y[:len(k1)] += k1; o = int(.035 * SR); y[o:o + len(k2)] += k2[:n - o] * .7
    w = cloth_whoosh(.25, seed + 3, up=False); o2 = int(.01 * SR); y[o2:o2 + len(w)] += w[:n - o2] * .15
    st = add_reverb(pan(y, 0), .15, dur=.6, damp_hz=3500); return fade(norm(st, -8), .001, .08)

def sfx_lantern_raise(seed=7):
    """Lift: handle creak + brass ting, then light swells (soft shimmer, rising fifth)."""
    dur = 2.4; n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros((n, 2))
    c = rope_creak(.3, seed); out[:len(c)] += pan(c, -.1) * .25
    b = brass_ting(1180, 1.6, seed); o = int(.12 * SR); out[o:o + len(b)] += pan(b, .1) * .35
    glow = np.zeros(n)
    for f, a in [(587.3, 1), (880, .6), (1174.7, .35), (1760, .15)]:
        glow += a * np.sin(2 * np.pi * f * t * (1 + .002 * np.sin(2 * np.pi * 4.5 * t)))
    shimmer = bp(noise(n), 3000, 9000) * .08
    env = smooth_env(n, [0, .25, 1.0, 1.6, dur], [0, 0, 1, .7, 0])
    out += pan((glow * .22 + shimmer) * env, 0)
    out = add_reverb(out, .35, dur=2.4); return fade(norm(out, -6), .002, .3)

if __name__ == "__main__":
    which = sys.argv[2:] or ["bgm", "amb", "home", "sfx"]
    if "bgm" in which: save("BGM_Prologue_ArMorDu_loop_v1", bgm_prologue())
    if "amb" in which: save("AMB_Prologue_SeaWind_loop_v1", amb_prologue())
    if "home" in which: save("AMB_Home_Interior_loop_v1", amb_home())
    if "sfx" in which:
        for i in range(4): save(f"SFX_Maela_Step_Wood_0{i+1}_v1", footstep(200 + i * 13), True)
        for i in range(2): save(f"SFX_Maela_Jump_0{i+1}_v1", sfx_jump(300 + i * 7), True)
        for i in range(2): save(f"SFX_Maela_Land_0{i+1}_v1", sfx_land(400 + i * 7), True)
        save("SFX_Maela_LanternRaise_v1", sfx_lantern_raise(), True)

# ---------------------------------------------------------------- v2 footstep (11-08): "knock on a door", not a drum
def plank_knock(f0, seed, vel=1.0):
    """Hollow wooden plank: mid-frequency modes, very short decay, sharp click, small cavity boom."""
    r = np.random.default_rng(seed); dur = .18; n = int(dur * SR); t = np.arange(n) / SR
    ratios = [1.0, 1.58, 2.71, 4.3, 6.2]; decays = [.035, .022, .014, .008, .005]; amps = [1, .7, .45, .25, .12]
    y = modal([f0 * k * r.uniform(.98, 1.02) for k in ratios], decays, amps, dur, strike_noise=.9, strike_bp=(1500, 6000), seed=seed)
    cav = bp(r.standard_normal(n), 170, 320) * np.exp(-t / .018) * .35      # hollow under the boards, short
    click = hp(r.standard_normal(n), 2500) * np.exp(-t / .0012) * .5
    return hp(y + cav + click, 140) * vel

def footstep_v2(seed):
    r = np.random.default_rng(seed); dur = .30; n = int(dur * SR); y = np.zeros(n)
    heel = plank_knock(r.uniform(420, 520), seed, 1.0); y[:len(heel)] += heel
    o = int(r.uniform(.05, .075) * SR); toe = plank_knock(r.uniform(520, 640), seed + 1, .45); y[o:o + len(toe)] += toe[:n - o]
    st = pan(y, r.uniform(-.1, .1)); st = add_reverb(st, .14, dur=.45, damp_hz=5000)
    return fade(norm(st, -11 - r.uniform(0, 1.5)), .0005, .04)

if __name__ == "__main__" and "step2" in sys.argv[2:]:
    for i in range(4): save(f"SFX_Maela_Step_Wood_0{i+1}_v2", footstep_v2(600 + i * 17), True)

# ---------------------------------------------------------------- v3 footstep (11-08): v2 knock, but lower and heavier
def footstep_v3(seed):
    r = np.random.default_rng(seed); dur = .32; n = int(dur * SR); y = np.zeros(n); t = np.arange(n) / SR
    heel = plank_knock(r.uniform(260, 310), seed, 1.0); y[:len(heel)] += lp(heel, 3500)
    o = int(r.uniform(.055, .08) * SR); toe = plank_knock(r.uniform(320, 380), seed + 1, .4); y[o:o + len(toe)] += lp(toe, 3000)[:n - o]
    body = bp(r.standard_normal(n), 110, 200) * np.exp(-t / .03) * .45   # deeper hollow under the boards
    y += body
    st = pan(y, r.uniform(-.1, .1)); st = add_reverb(st, .14, dur=.5, damp_hz=4000)
    return fade(norm(st, -11 - r.uniform(0, 1.5)), .0005, .04)

if __name__ == "__main__" and "step3" in sys.argv[2:]:
    for i in range(4): save(f"SFX_Maela_Step_Wood_0{i+1}_v3", footstep_v3(700 + i * 17), True)

# ---------------------------------------------------------------- v4 footstep (11-08): old floorboards, deep "dong", ~1 octave below v3
def footstep_v4(seed):
    r = np.random.default_rng(seed); dur = .40; n = int(dur * SR); y = np.zeros(n); t = np.arange(n) / SR
    heel = plank_knock(r.uniform(130, 155), seed, 1.0); y[:len(heel)] += lp(heel, 2200)
    o = int(r.uniform(.06, .085) * SR); toe = plank_knock(r.uniform(165, 195), seed + 1, .35); y[o:o + len(toe)] += lp(toe, 2000)[:n - o]
    body = bp(r.standard_normal(n), 60, 120) * np.exp(-t / .045) * .6     # hollow space under old boards
    y += body
    if r.random() < .5:                                                    # old board gives a small creak sometimes
        c = lp(rope_creak(.18, seed + 5), 1200); s = int(.04 * SR); y[s:s + len(c)] += c[:n - s] * .12 / (np.max(np.abs(c)) + 1e-9) * np.max(np.abs(y))
    st = pan(y, r.uniform(-.1, .1)); st = add_reverb(st, .16, dur=.6, damp_hz=3000)
    return fade(norm(st, -10 - r.uniform(0, 1.5)), .0005, .05)

if __name__ == "__main__" and "step4" in sys.argv[2:]:
    for i in range(4): save(f"SFX_Maela_Step_Wood_0{i+1}_v4", footstep_v4(800 + i * 17), True)

# ---------------------------------------------------------------- v2 lantern (11-08): no temple-bell tail.
# Small handle-wire tick + glass/tin "tink" with very short decay, then the soft glow swell.
def sfx_lantern_raise_v2(seed=9):
    r = np.random.default_rng(seed); dur = 1.8; n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros((n, 2))
    c = rope_creak(.2, seed); out[:len(c)] += pan(lp(c, 2500), -.1) * .18
    tink = modal([2650, 4120, 6900], [.05, .03, .015], [1, .5, .25], .3, .3, (4000, 10000), seed)   # tin/glass, short
    o = int(.1 * SR); out[o:o + len(tink)] += pan(tink, .1) * .22
    wire = modal([3400, 5100], [.02, .012], [1, .4], .12, .2, (5000, 11000), seed + 1)
    o2 = int(.16 * SR); out[o2:o2 + len(wire)] += pan(wire, .15) * .1
    glow = np.zeros(n)
    for f, a in [(587.3, 1), (880, .5), (1174.7, .2)]:
        glow += a * np.sin(2 * np.pi * f * t)
    shimmer = bp(noise(n), 3500, 9000) * .05
    env = smooth_env(n, [0, .2, .8, 1.3, dur], [0, 0, 1, .5, 0])
    out += pan((glow * .12 + shimmer) * env, 0)
    out = add_reverb(out, .18, dur=1.0, damp_hz=5000); return fade(norm(out, -8), .002, .25)

if __name__ == "__main__" and "lantern2" in sys.argv[2:]:
    save("SFX_Maela_LanternRaise_v2", sfx_lantern_raise_v2(), True)

# ---------------------------------------------------------------- v3 lantern (11-08): v1's brass strike (head only) + v2 from the "beep" on
def sfx_lantern_raise_v3(seed=7):
    dur = 1.9; n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros((n, 2))
    c = rope_creak(.3, seed); out[:len(c)] += pan(c, -.1) * .2
    b = brass_ting(1180, .8, seed); tb = np.arange(len(b)) / SR
    b = b * np.where(tb < .12, 1.0, np.exp(-(tb - .12) / .07))          # keep the strike, cut the long temple-bell tail
    o = int(.12 * SR); out[o:o + len(b)] += pan(b, .1) * .35
    v2 = sfx_lantern_raise_v2(9); s = int(.08 * SR)                      # v2 tink + glow "beep" + shimmer
    k = min(len(v2), n - s); out[s:s + k] += v2[:k] * .8
    out = add_reverb(out, .12, dur=.8, damp_hz=5000); return fade(norm(out, -7), .002, .25)

if __name__ == "__main__" and "lantern3" in sys.argv[2:]:
    save("SFX_Maela_LanternRaise_v3", sfx_lantern_raise_v3(), True)

# ---------------------------------------------------------------- v4 lantern (11-08): v1 exactly, minus everything that lingers
# removed: sustained glow tones, sympathetic fifth ring, long reverb; brass ting decay shortened.
def sfx_lantern_raise_v4(seed=7):
    dur = 1.2; n = int(dur * SR); out = np.zeros((n, 2))
    c = rope_creak(.3, seed); out[:len(c)] += pan(c, -.1) * .25
    b = brass_ting(1180, .9, seed); tb = np.arange(len(b)) / SR
    b = b * np.exp(-tb / .28)
    o = int(.12 * SR); out[o:o + len(b)] += pan(b, .1) * .35
    shimmer = bp(noise(n), 3000, 9000) * .05 * smooth_env(n, [0, .2, .5, .8, dur], [0, 0, 1, 0, 0])
    out += pan(shimmer, 0)
    out = add_reverb(out, .12, dur=.6, damp_hz=5000); return fade(norm(out, -7), .002, .15)

if __name__ == "__main__" and "lantern4" in sys.argv[2:]:
    save("SFX_Maela_LanternRaise_v4", sfx_lantern_raise_v4(), True)

# ---------------------------------------------------------------- v5 lantern (11-08): bright loud strike, straight tone (no beating pairs), long clean tail
def sfx_lantern_raise_v5(seed=7):
    dur = 3.2; n = int(dur * SR); out = np.zeros((n, 2))
    c = rope_creak(.3, seed); out[:len(c)] += pan(c, -.1) * .2
    ratios = [1.0, 2.32, 4.07, 5.6]; decays = [1.6, .7, .3, .15]; amps = [1.0, .5, .3, .15]   # single partials -> no wobble
    b = modal([1180 * r for r in ratios], decays, amps, 3.0, strike_noise=.6, strike_bp=(3000, 11000), seed=seed)
    o = int(.12 * SR); out[o:o + len(b)] += pan(b, .1) * .6
    out = add_reverb(out, .1, dur=.8, damp_hz=6000); return fade(norm(out, -5), .001, .4)

if __name__ == "__main__" and "lantern5" in sys.argv[2:]:
    save("SFX_Maela_LanternRaise_v5", sfx_lantern_raise_v5(), True)
