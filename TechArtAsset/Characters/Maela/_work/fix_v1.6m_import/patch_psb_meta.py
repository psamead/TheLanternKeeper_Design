"""Maela v1.6 import fix: write new layer sizes into Maela.psb.meta (layeredSpriteImportData).
Usage: python patch_psb_meta.py <Maela.psb (new)> <Maela.psb.meta> [--dry]
- For every sprite whose PSB layer bbox differs from the meta: set rect width/height = layer size,
  spritePosition = (left, canvasH - bottom). rect x/y (atlas position) left as is; importer repacks.
- Keeps CRLF, spriteID, everything else. Writes <meta>.bak first. Also writes expected_rects.json
  next to the meta for MaelaSpriteRectCheck.cs.
"""
import sys, re, json, os
from psd_tools import PSDImage
psb, meta = sys.argv[1], sys.argv[2]; dry = '--dry' in sys.argv
p = PSDImage.open(psb); H = p.height
layers = {l.name: l for l in p.descendants() if not l.is_group()}
raw = open(meta, 'rb').read().decode('utf-8'); nl = '\r\n' if '\r\n' in raw else '\n'
lines = raw.split(nl)
start = lines.index('  layeredSpriteImportData:'); i = start + 1
expected, changes = [], []
while i < len(lines) and lines[i].startswith('  - name:'):
    name = lines[i][len('  - name: '):].strip(); j = i + 1
    while j < len(lines) and not lines[j].startswith('  - ') and lines[j].startswith('    '): j += 1
    blk = range(i, j); L = layers.get(name)
    if L is not None:
        l, t, r, b = L.bbox; w, h = r - l, b - t; sp = (l, H - b)
        expected.append(dict(name=name, w=w, h=h, posX=sp[0], posY=sp[1]))
        for k in blk:
            s = lines[k]
            if s.startswith('      width: ') and int(s.split(':')[1]) != w: changes.append((name,'w',s.strip(),w)); lines[k] = f'      width: {w}'
            if s.startswith('      height: ') and int(s.split(':')[1]) != h: changes.append((name,'h',s.strip(),h)); lines[k] = f'      height: {h}'
            if s.startswith('    spritePosition:'):
                new = f'    spritePosition: {{x: {sp[0]}, y: {sp[1]}}}'
                if s != new: changes.append((name,'pos',s.strip(),sp)); lines[k] = new
    i = j
for c in changes: print(*c)
print(len(changes), 'changes;', len(expected), 'sprites checked')
if not dry:
    open(meta + '.bak', 'wb').write(raw.encode('utf-8'))
    open(meta, 'wb').write(nl.join(lines).encode('utf-8'))
    json.dump(dict(psb=psb.split('/')[-1], canvasH=H, sprites=expected), open(os.path.join(os.path.dirname(os.path.abspath(meta)), 'maela_expected_rects.json'), 'w'), indent=1)
