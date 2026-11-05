import numpy as np, subprocess, sys
from PIL import Image
D='/home/claude/thelanternkeeper_design/TechArtAsset/Menu/'
S=0.5; W,H=int(1920*S),int(1080*S); FPS=30; SEC=10
bg=np.asarray(Image.open(D+'MENU_L0_BG_1920.png').convert('RGB').resize((W,H)),float)/255
def load(p,size=None):
    im=Image.open(p).convert('RGBA')
    if size: im=im.resize(size,Image.LANCZOS)
    a=np.asarray(im,float)/255; return a
ld=load(D+'MENU_L1_left_dark.png',(W,H))
title=load(D+'TITLE_FRAMED_v1.png'); th=int(title.shape[0]*720/title.shape[1]*S); title=load(D+'TITLE_FRAMED_v1.png',(int(720*S),th))
fa=load('MENU_FX_Fog_A.png'); fb=load('MENU_FX_Fog_B.png')
# display: fog A texture 2048x512 shown at 2400x600 (screen px), rect y 260..860 ; fog B 2048x256 shown 2400x300, rect y 640..940
fa=load('MENU_FX_Fog_A.png',(int(2400*S),int(600*S))); fb=load('MENU_FX_Fog_B.png',(int(2400*S),int(300*S)))
glow=load('MENU_FX_LanternGlow.png',(int(440*S),int(440*S)))
def over(dst,src,x,y,alpha=1.0):
    h,w=src.shape[:2]; x0,y0=max(x,0),max(y,0); x1,y1=min(x+w,W),min(y+h,H)
    if x1<=x0 or y1<=y0: return
    s=src[y0-y:y1-y,x0-x:x1-x]; a=s[...,3:4]*alpha
    dst[y0:y1,x0:x1]=dst[y0:y1,x0:x1]*(1-a)+s[...,:3]*a
def scrolled(tex,offset):
    off=int(offset)%tex.shape[1]; t=np.roll(tex,off,axis=1); return t[:, :W]
p=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','veryfast','menu_fx_preview.mp4'],stdin=subprocess.PIPE)
rng=np.random.default_rng(1); flick=np.cumsum(rng.standard_normal(SEC*FPS+1))*0.02
from scipy.ndimage import gaussian_filter1d; flick=gaussian_filter1d(rng.standard_normal(SEC*FPS+1),4)*0.25
for f in range(SEC*FPS):
    t=f/FPS; fr=bg.copy()
    over(fr,scrolled(fa,t*14*S),0,int(260*S),0.9)
    over(fr,scrolled(fb,t*26*S),0,int(640*S),0.9)
    breath=0.5+0.5*np.sin(2*np.pi*t/3.2)
    a=0.30+0.70*breath+0.10*flick[f]; sc=0.86+0.24*breath
    g=glow if abs(sc-1)<0.01 else np.asarray(Image.fromarray((glow*255).astype(np.uint8)).resize((int(glow.shape[1]*sc),int(glow.shape[0]*sc)),Image.BILINEAR),float)/255
    over(fr,g,int(1591*S)-g.shape[1]//2,int(373*S)-g.shape[0]//2,np.clip(a,0,1))
    over(fr,ld,0,0)
    over(fr,title,int(100*S),int(70*S))
    p.stdin.write((np.clip(fr,0,1)*255).astype(np.uint8).tobytes())
    if f==45: Image.fromarray((np.clip(fr,0,1)*255).astype(np.uint8)).save('frame.png')
p.stdin.close(); p.wait(); print('done')
