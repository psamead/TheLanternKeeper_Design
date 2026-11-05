import numpy as np
from PIL import Image
rng=np.random.default_rng(3)
def fft_noise(h,w,beta,seed):
    r=np.random.default_rng(seed)
    fy=np.fft.fftfreq(h)[:,None]; fx=np.fft.fftfreq(w)[None,:]
    f=np.sqrt(fx**2+(fy*w/h)**2*0+fy**2); f[0,0]=1
    spec=(r.standard_normal((h,w))+1j*r.standard_normal((h,w)))/f**beta
    spec[0,0]=0
    n=np.real(np.fft.ifft2(spec)); n=(n-n.min())/(n.max()-n.min()); return n  # periodic in x and y
def fog(h,w,beta,seed,thresh,soft,amax,band):
    n=fft_noise(h,w,beta,seed)*0.75+fft_noise(h,w,beta-0.6,seed+1)*0.25
    a=np.clip((n-thresh)/soft,0,1)**1.5
    y=np.linspace(0,1,h)[:,None]
    a*=np.exp(-((y-0.5)/band)**2)            # soft top / bottom edges
    d=np.clip(np.minimum(y,1-y)/0.18,0,1)      # 0 at the very top/bottom rows, 1 after 18 %
    a*=d*d*(3-2*d)                             # smoothstep window: no visible cut at the rect edge
    a*=amax
    col=np.array([0x9C,0xAD,0xC4],float)     # cool mist, close to present-layer light #8FA3BF
    img=np.zeros((h,w,4),np.uint8); img[...,:3]=col; img[...,3]=(a*255).astype(np.uint8)
    return img
Image.fromarray(fog(512,2048,1.9,11,0.40,0.38,0.62,0.30)).save('MENU_FX_Fog_A.png')   # big soft banks
Image.fromarray(fog(256,2048,1.5,21,0.50,0.30,0.45,0.28)).save('MENU_FX_Fog_B.png')   # thin wisps
# lantern glow: warm radial, premultiplied-friendly soft falloff
s=512; y,x=np.mgrid[0:s,0:s]; r=np.hypot(x-s/2,y-s/2)/(s/2)
core=np.exp(-(r/0.08)**2); halo=np.exp(-(r/0.30)**2)*0.5; wide=np.exp(-(r/0.6)**2)*0.12
edge=np.clip(1-r,0,1)**2*(3-2*np.clip(1-r,0,1))  # smoothstep to 0 at the rim
a=np.clip(core+halo+wide,0,1)*edge
col=np.zeros((s,s,3)); 
c_core=np.array([255,226,150]); c_halo=np.array([0xE8,0xB4,0x5A]); 
t=np.clip(core/(core+halo+wide+1e-6),0,1)[...,None]; col=c_core*t+c_halo*(1-t)
img=np.zeros((s,s,4),np.uint8); img[...,:3]=col.astype(np.uint8); img[...,3]=(a*255).astype(np.uint8)
Image.fromarray(img).save('MENU_FX_LanternGlow.png')
print('ok')
