# P1 variant B: keep the MJ round cap, add only the poster's pointed roof (smaller) on top.
import numpy as np
from PIL import Image, ImageFilter
EXT=200
base=Image.open('_work/L0_base_ext.png').convert('RGB'); W,H=base.size
b=np.array(base).astype(float)
p=np.array(Image.open('_work/poster_top_crop.png').convert('RGB')).astype(float)
roof=p[20:150,40:236]                     # spire + roof only (down to the eaves)
lum=roof@[0.3,0.5,0.2]; sky=np.median(lum[:10]); sil=lum<sky-12
# cut away the dormer-window hole's sky (keep it as part of roof) – fill small holes
from PIL import ImageFilter
m=Image.fromarray((sil*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.0))
body=b[EXT+300:EXT+420,740:960].reshape(-1,3)
src=roof[sil]; rec=(roof-src.mean(0))/(src.std(0)+1e-3)*body.std(0)*0.9+body.mean(0)*0.9
# find cap top: first row where the cap (darker than sky) appears around x=850
col=b[:, 800:900].mean(1)@[0.3,0.5,0.2]; skyv=col[EXT+5]
cap_top=next(y for y in range(EXT,EXT+400) if col[y]<skyv-25)
S=0.95; ph,pw=roof.shape[:2]; nw,nh=int(pw*S),int(ph*S)
img=Image.fromarray(rec.clip(0,255).astype(np.uint8)).resize((nw,nh),Image.LANCZOS); mm=m.resize((nw,nh),Image.LANCZOS)
cx=852; ox,oy=cx-nw//2,cap_top+18-nh          # eaves overlap the cap top a little
layer=Image.new('RGBA',(W,H),(0,0,0,0)); lm=Image.new('L',(W,H),0); layer.paste(img,(ox,oy)); lm.paste(mm,(ox,oy)); layer.putalpha(lm)
layer.save('_work/L2B_roof_small.png')
comp=base.convert('RGBA'); comp.alpha_composite(layer); comp=comp.convert('RGB'); comp.save('_work/compB_full.png')
print('cap_top',cap_top,'roof tip',oy)
comp.crop((500,0,1200,700)).save('_work/_view_compB_top.jpg')
f=comp.crop((0,0,2912,1638)).resize((2208,1242),Image.LANCZOS); f.save('SB_P1_B.png')
f.convert('RGB').resize((1104,621)).save('_work/SB_P1_B_preview.jpg',quality=88)
