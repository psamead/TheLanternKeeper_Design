"""Present layer: break the ladder in Home_Present_v1 (erase its upper part, jagged break) -> Present/Home_Present_v2_brokenLadder.png"""
import cv2, numpy as np
im=cv2.imread('Present/Home_Present_v1.png'); H,W=im.shape[:2]
m=np.zeros((H,W),np.uint8)
poly=np.array([(1812,120),(1968,120),(2092,560),(1872,560)],np.int32)
cv2.fillPoly(m,[poly],255)
# jagged break line around y=540-575
rng=np.random.default_rng(3); pts=[(1860,560)]
for x in range(1860,2110,14): pts.append((x,int(548+rng.integers(-18,22))))
pts+= [(2110,600),(1860,600)]
cut=np.zeros_like(m); cv2.fillPoly(cut,[np.array(pts,np.int32)],255)
low=np.zeros_like(m); low[565:,:]=255
m=np.where((cut>0)&(low>0),0,m)  # keep below the jag
m=cv2.dilate(m,np.ones((7,7),np.uint8))
out=cv2.inpaint(im,m,21,cv2.INPAINT_TELEA)
# re-add painterly texture: blend in a blurred copy of the wall's own noise
noise=cv2.GaussianBlur(im,(0,0),9)-cv2.GaussianBlur(im,(0,0),25)
tex=np.clip(out.astype(np.int16)+noise.astype(np.int16)//2,0,255).astype(np.uint8)
mf=cv2.GaussianBlur(m,(0,0),4)[...,None]/255.0
out=(tex*mf+out*(1-mf)).astype(np.uint8)
cv2.imwrite('Present/Home_Present_v2_brokenLadder.png',out)
cv2.imwrite('Present/_work/_ladder_before_after.jpg',np.vstack([im[0:900,1650:2250],out[0:900,1650:2250]]))
print('ok')
