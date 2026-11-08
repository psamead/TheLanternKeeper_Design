"""MJ upscale -> SB_Px.png (2208x1242, same as SB_P1).
Usage: python finish_sb.py <mj.png> P2 [--y 0.5] [--x 0.5] [--zoom 1.0]
  x/y = where the crop sits (0 = left/top, 1 = right/bottom); zoom>1 crops tighter.
Fills to 16:9 by cropping (never stretches), Lanczos resize, writes ../SB_P2.png and a 1/4 preview here.
"""
import sys, argparse
from PIL import Image
a = argparse.ArgumentParser(); a.add_argument('src'); a.add_argument('page')
a.add_argument('--x', type=float, default=.5); a.add_argument('--y', type=float, default=.5); a.add_argument('--zoom', type=float, default=1.0)
o = a.parse_args(); W, H = 2208, 1242
im = Image.open(o.src).convert('RGB'); w, h = im.size
cw = min(w, h * W / H) / o.zoom; ch = cw * H / W
x0 = (w - cw) * o.x; y0 = (h - ch) * o.y
out = im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((W, H), Image.LANCZOS)
out.save(f'../SB_{o.page}.png'); out.resize((W // 4, H // 4)).save(f'SB_{o.page}_preview.jpg', quality=85)
print(f'{o.src} {w}x{h} -> crop {cw:.0f}x{ch:.0f} @({x0:.0f},{y0:.0f}) -> ../SB_{o.page}.png')
if cw < W: print('WARNING: source smaller than 2208 wide -> upscaled; use MJ Upscale (Subtle) first')
