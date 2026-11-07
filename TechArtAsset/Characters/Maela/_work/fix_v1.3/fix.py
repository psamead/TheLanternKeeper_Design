# v1.3: interior-only fixes. Rule: layer bounds (alpha>0 bbox) must equal v1 exactly.
import numpy as np, glob, os
from PIL import Image
from scipy import ndimage as nd
import json
OFF=json.load(open('offsets.json'))
def load(n):
    c=Image.new('RGBA',(149,320)); c.paste(Image.open('orig/%s.png'%n).convert('RGBA'),tuple(OFF[n][:2]))
    return np.array(c).astype(np.int32)
def bbox(a):
    ys,xs=np.nonzero(a[...,3]>0); return (xs.min(),ys.min(),xs.max(),ys.max())
def keep_main(a):
    """Stray slivers -> alpha 1 (invisible, bounds kept)."""
    lab,n=nd.label(a[...,3]>60)
    if n<=1: return a
    sizes=nd.sum(np.ones_like(lab),lab,range(1,n+1)); main=lab==(np.argmax(sizes)+1)
    near=nd.binary_dilation(main,iterations=2)
    kill=(a[...,3]>0)&~near
    a[kill,3]=1
    return a
def knee(a,offy,cy,side):
    """Paint a rounded knee inside the layer's existing pixel box."""
    H,W=a.shape[:2]; y0=cy-offy
    rows=[r for r in range(max(0,y0-6),min(H,y0+8)) if (a[r,:,3]>200).sum()>3]
    if not rows: print('no knee rows',side,cy); return a
    r=rows[len(rows)//2]; xs=np.nonzero(a[r,:,3]>200)[0]; cx=(xs.min()+xs.max())/2; hw=(xs.max()-xs.min())/2
    col=np.median(a[a[...,3]>230][:,:3],axis=0)
    yy,xx=np.mgrid[0:H,0:W]; m=((xx-cx)/hw)**2+((yy-y0)/(hw*0.9))**2<=1
    x0,y0b,x1,y1=bbox(a); m&=(xx>=x0)&(xx<=x1)&(yy>=y0b)&(yy<=y1)
    m&=a[...,3]<230
    a[m,:3]=col; a[m,3]=255
    return a
fixes={}
for n in ['Boot_L','Boot_R','Leg_Lower_L','Leg_Lower_R','Leg_Upper_L','Leg_Upper_R']:
    fixes[n]=keep_main(load(n))
# knees: joint y in canvas px; layers are full-canvas so offy=0
fixes['Leg_Lower_R']=knee(fixes['Leg_Lower_R'],0,247,'R'); fixes['Leg_Lower_L']=knee(fixes['Leg_Lower_L'],0,245,'L')
fixes['Leg_Upper_R']=knee(fixes['Leg_Upper_R'],0,245,'R'); fixes['Leg_Upper_L']=knee(fixes['Leg_Upper_L'],0,243,'L')
# coat hem notch: fill horizontal spans between opaque coat pixels, above dress top (y<190)
a=load('Coat_Hem'); op=a[...,3]>200; dark=np.median(a[op&(a[...,:3].sum(-1)<330)][:,:3],axis=0)
for y in range(a.shape[0]):
    xs=np.nonzero(op[y])[0]
    if len(xs)<2 or y>=192: continue
    seg=np.arange(xs.min(),xs.max()+1); hole=seg[a[y,seg,3]<200]
    # only fill gaps narrower than 30 px (the front opening), not outside silhouette
    if 0<len(hole)<30: a[y,hole,:3]=dark; a[y,hole,3]=255
fixes['Coat_Hem']=a
# coat body: whitish low-saturation pixels -> local coat colour
a=load('Coat_Body'); rgb=a[...,:3]; mx=rgb.max(-1); mn=rgb.min(-1)
white=(a[...,3]>0)&(mn>170)&(mx-mn<70)
good=(a[...,3]>200)&~white
idx=nd.distance_transform_edt(~good,return_distances=False,return_indices=True)
a[white,:3]=rgb[idx[0][white],idx[1][white]]
fixes['Coat_Body']=a
os.makedirs('fixed',exist_ok=True)
ok=True
for n,a in fixes.items():
    b0=bbox(load(n)); b1=bbox(a)
    print(n,b0,b1,'OK' if b0==b1 else 'BOUNDS CHANGED'); ok&=b0==b1
    Image.fromarray(a.clip(0,255).astype(np.uint8)).save('fixed/%s.png'%n)
print('ALL BOUNDS SAME' if ok else 'FAIL')
