"""Independent narrative stems v1. Existing Menu synthesis helpers; no music generation."""
from pathlib import Path
import importlib.util, sys
import numpy as np
from scipy.io import wavfile
out = Path(__file__).resolve().parents[1]
helper = out.parent/'Menu/_src/synth_menu_audio.py'
sys.argv = [str(helper), str(out), 'none']
spec = importlib.util.spec_from_file_location('menu', helper)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.rng = np.random.default_rng(20261115)
length = 40
# Pure wave events: no wind helper, music or source samples.
waves = np.zeros((int(52*m.SR),2))
for i, start in enumerate(range(0, 44, 6)):
    event = m.pan(m.wave_event(8, seed=1100+i, bright=0.72), (-0.25 if i%2 else 0.25))
    a=int(start*m.SR); waves[a:a+len(event)] += event
waves = m.norm(m.make_loop(waves, length), -6)
# Pure sustained wind: no wave_event, foam or surf envelope.
wind = np.stack([m.wind(44, seed=1201, base=360, depth=0.4, gust_rate=0.09),
                 m.wind(44, seed=1202, base=400, depth=0.4, gust_rate=0.09)], axis=1)
wind = m.norm(m.make_loop(m.fade(wind, 3, 3), length), -8)
for name, data in [('AMB_Story_Waves_loop_v1',waves),('AMB_Story_Wind_loop_v1',wind)]:
    wavfile.write(out/(name+'.wav'),m.SR,(np.clip(data,-1,1)*32767).astype(np.int16))
    print(name, len(data)/m.SR)
