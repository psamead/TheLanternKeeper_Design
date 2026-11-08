# v1.4 legs: colour match (far leg slightly darker than near), thicken far thigh inside its box, harden semi-transparent leg edges.
import numpy as np
from PIL import Image
L=lambda n: np.array(Image.open(f'orig/{n}.png').convert('RGBA')).astype(float)
def bbox(a): ys,xs=np.nonzero(a[...,3]>0); return (xs.min(),ys.min(),xs.max(),ys.max())
out={}
for far,near in [('Leg_Upper_L','Leg_Upper_R'),('Leg_Lower_L','Leg_Lower_R'),('Boot_L','Boot_R')]:
    a,b=L(far),L(near); ma,mb=a[...,3]>200,b[...,3]>200
    mu_a,sd_a=a[ma][:,:3].mean(0),a[ma][:,:3].std(0)+1e-3; mu_b,sd_b=b[mb][:,:3].mean(0),b[mb][:,:3].std(0)
    a[...,:3]=np.where(a[...,3:]>0,(a[...,:3]-mu_a)/sd_a*sd_b+mu_b*0.93,a[...,:3])
    out[far]=a; out[near]=b
# thicken far thigh: each row's opaque span at least the width of the row 6 below (tapering), grown leftward, inside the box
a=out['Leg_Upper_L']; x0,y0,x1,y1=bbox(a); col=np.median(a[a[...,3]>200][:,:3],0)
spans={}
for y in range(y0,y1+1):
    xs=np.nonzero(a[y,:,3]>200)[0]
    if len(xs): spans[y]=(xs.min(),xs.max())
widths={y:s[1]-s[0] for y,s in spans.items()}
ref=np.median([w for y,w in widths.items() if y>y0+(y1-y0)//2])
for y,(l,r) in spans.items():
    want=int(ref*0.92)
    if r-l<want:
        nl=max(x0,r-want)
        a[y,nl:l,:3]=col; a[y,nl:l,3]=255
out['Leg_Upper_L']=a
# harden semi-transparent edges (alpha 60..254 -> 255) on all six leg layers so no background line shows between legs
for n,a in out.items():
    m=(a[...,3]>60)&(a[...,3]<255); a[m,3]=255
ok=True
for n,a in out.items():
    b0,b1=bbox(L(n)),bbox(a); print(n,'OK' if b0==b1 else f'BOUNDS {b0}->{b1}'); ok&=b0==b1
    Image.fromarray(a.clip(0,255).astype(np.uint8)).save(f'fixed/{n}.png')
print('ALL SAME' if ok else 'FAIL')
