# P1: graft the poster lighthouse top (dark lantern room + spire) onto the MJ tower. Outputs layered PNGs + preview.
import numpy as np
from PIL import Image, ImageFilter
EXT=200
t=np.array(Image.open('SB_P1_src_MJ_towerEdit.png').convert('RGB')).astype(float)
H,W,_=t.shape
# 1) base with sky extended upward: repeat top row, blur vertically, add tiny noise
# smooth sky: per-column mean of top 60 rows, heavily blurred sideways, then ramp-blend into the original
col=t[:60].mean(0)                                   # (W,3)
cimg=Image.fromarray(np.repeat(col[None],8,0).clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(90))
col=np.array(cimg).astype(float)[4]
ext=np.repeat(col[None],EXT,0)
g=np.linspace(0.92,1.0,EXT)[:,None,None]; ext=ext*g  # slightly deeper toward the top
base=np.concatenate([ext,t],0)
R=140                                                # blend original top rows toward the smooth sky
a=np.linspace(1,0,R)[:,None,None]
base[EXT:EXT+R]=base[EXT:EXT+R]*(1-a*0.85)+col[None]*a*0.85
# 2) sky patch over the old rounded cap (x 690-1010, y 60-255 in source -> +EXT)
x0,x1,y0,y1=680,1020,EXT+40,EXT+262
patch=base.copy()
L=base[:,x0-10:x0].mean(1); R_=base[:,x1:x1+10].mean(1)
for x in range(x0,x1):
    u=(x-x0)/(x1-x0); patch[y0:y1,x]=L[y0:y1]*(1-u)+R_[y0:y1]*u
pm=np.zeros((H+EXT,W)); pm[y0:y1,x0:x1]=1
patch[y1:y1+50,x0:x1]=0+patch[y1:y1+50,x0:x1]
for x in list(range(x0,728))+list(range(982,x1)):
    u=(x-x0)/(x1-x0); patch[y1:y1+55,x]=L[y1:y1+55]*(1-u)+R_[y1:y1+55]*u
pm[y1:y1+55,x0:728]=1; pm[y1:y1+55,982:x1]=1
pmask=Image.fromarray((pm*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
# keep tower body below cap: fade mask out toward y1
# 3) poster top silhouette
p=np.array(Image.open('_work/poster_top_crop.png').convert('RGB')).astype(float)[20:262,40:236]
lum=p@[0.3,0.5,0.2]
sky=np.median(lum[:10]); sil=lum<sky-12           # dark tower vs lighter sky
m=Image.fromarray((sil*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
# colour transfer onto target tower colours
body=base[EXT+300:EXT+420,740:960].reshape(-1,3)
src=p[sil]; mu_s,sd_s=src.mean(0),src.std(0)+1e-3; mu_t,sd_t=body.mean(0),body.std(0)
rec=(p-mu_s)/sd_s*sd_t*0.9+mu_t*0.92            # slightly darker than the lit body
S=1.53
ph,pw=p.shape[:2]; nw,nh=int(pw*S),int(ph*S)
topimg=Image.fromarray(rec.clip(0,255).astype(np.uint8)).resize((nw,nh),Image.LANCZOS)
topmask=m.resize((nw,nh),Image.LANCZOS)
cx=850; gy=EXT+265                               # gallery bottom sits on straight body
ox,oy=cx-nw//2,gy-nh
layer_top=Image.new('RGBA',(W,H+EXT),(0,0,0,0)); tm=Image.new('L',(W,H+EXT),0)
layer_top.paste(topimg,(ox,oy)); tm.paste(topmask,(ox,oy)); layer_top.putalpha(tm)
layer_sky=Image.fromarray(patch.clip(0,255).astype(np.uint8)).convert('RGBA'); layer_sky.putalpha(pmask)
Image.fromarray(base.clip(0,255).astype(np.uint8)).save('_work/L0_base_ext.png')
layer_sky.save('_work/L1_sky_patch.png'); layer_top.save('_work/L2_tower_top.png')
comp=Image.open('_work/L0_base_ext.png').convert('RGBA'); comp.alpha_composite(layer_sky); comp.alpha_composite(layer_top)
comp=comp.convert('RGB'); comp.save('_work/comp_full.png')
print('tip y',oy,'size',comp.size)
comp.crop((500,0,1200,700)).save('_work/_view_comp_top.jpg'); comp.resize((1092,int(1092*comp.height/comp.width))).save('_work/_view_comp.jpg')
