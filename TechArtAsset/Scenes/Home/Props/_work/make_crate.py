"""Crate_src_MJ.png -> Crate_v1.png (520x440, transparent, bottom-aligned, defringed, cooled)."""
import numpy as np
from PIL import Image, ImageFilter
from collections import deque
src=Image.open('_work/Crate_src_MJ.png').convert('RGB'); a=np.asarray(src).astype(np.float32)
H,W,_=a.shape
mx=a.max(2); mn=a.min(2); sat=(mx-mn)/(mx+1e-3); val=mx/255
bgish=(val>0.72)&(sat<0.22)          # white bg
yy=np.arange(H)[:,None]
bgish|=(yy>H*0.86)&(val>0.45)&(sat<0.35)   # pale floor shadow under the crate
# also: anything outside the crate's column span in the bottom band
mid=~bgish[int(H*0.5)]; xs=np.where(mid)[0]; x0,x1=xs.min(),xs.max()
band_out=(yy>H*0.8)&((np.arange(W)[None,:]<x0-8)|(np.arange(W)[None,:]>x1+8))
bgish|=band_out
# flood fill from borders through bg-ish pixels
mask=np.zeros((H,W),bool); q=deque()
for x in range(W): q+= [(0,x),(H-1,x)]
for y in range(H): q+= [(y,0),(y,W-1)]
while q:
    y,x=q.popleft()
    if 0<=y<H and 0<=x<W and not mask[y,x] and bgish[y,x]:
        mask[y,x]=True; q+= [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]
alpha=Image.fromarray(np.where(mask,0,255).astype(np.uint8))
# remove specks: keep largest component via open/close
alpha=alpha.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(5))
alpha=alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
A=np.asarray(alpha).astype(np.float32)/255
# defringe: edge band colours -> blurred interior colours
inner=(A>0.99).astype(np.float32)
blur_rgb=np.stack([np.asarray(Image.fromarray(a[...,c]*inner).filter(ImageFilter.GaussianBlur(10)),np.float32) if False else 0 for c in range(3)],0) if False else None
im_in=Image.fromarray((a*inner[...,None]).astype(np.uint8)); w_in=Image.fromarray((inner*255).astype(np.uint8))
bi=np.asarray(im_in.filter(ImageFilter.GaussianBlur(12))).astype(np.float32); bw=np.asarray(w_in.filter(ImageFilter.GaussianBlur(12))).astype(np.float32)[...,None]/255
fill=bi/np.maximum(bw,1e-3)
band=(A>0)&(A<0.99)
near=np.asarray(Image.fromarray(((A<0.99)*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(13)))>0
whitish=(val>0.75)&(sat<0.25)&near
rep=band|whitish
a2=a.copy(); a2[rep]=fill[rep]
# cool + darken toward Home night palette
cool=np.array([0.78,0.84,1.00]); a2=a2*0.82*cool; a2=np.clip(a2,0,255)
rgba=np.dstack([a2,A*255]).astype(np.uint8); im=Image.fromarray(rgba,'RGBA')
bb=im.getchannel('A').point(lambda v:255 if v>20 else 0).getbbox(); im=im.crop(bb)
w,h=im.size; TW,TH=520,440
s=min(TW/w,TH/h); im=im.resize((round(w*s),round(h*s)),Image.LANCZOS)
out=Image.new('RGBA',(TW,TH),(0,0,0,0)); out.paste(im,((TW-im.width)//2,TH-im.height),im)
out.save('Crate_v1.png'); print('bbox',bb,'scaled',im.size)
