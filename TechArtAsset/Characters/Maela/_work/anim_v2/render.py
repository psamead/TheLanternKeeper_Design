import math, sys
from PIL import Image
from poses import CLIPS, HIP_Y
import os
P=os.environ.get("PARTS","parts_canvas_v1.6m")+"/"
S=3 if 'canvas' in P else 0.1288*3          # source px -> preview px (3x of the 149x320 psb)
# joints in psb px (149x320, y down), from 2026-11-06 import doc
J={'Hip':(59,206,None),'Body':(59,206,'Hip'),'Head':(69,70,'Body'),'Shoulder_R':(89,93,'Body'),
 'Elbow_R':(102,123,'Shoulder_R'),'Wrist_R':(124,123,'Elbow_R'),'Lantern':(130,127,'Wrist_R'),
 'Shoulder_L':(64,86,'Body'),'Elbow_L':(53,144,'Shoulder_L'),'Thigh_R':(66,206,'Hip'),'Shin_R':(66,247,'Thigh_R'),
 'Foot_R':(64,278,'Shin_R'),'Thigh_L':(52,206,'Hip'),'Shin_L':(48,245,'Thigh_L'),'Foot_L':(42,276,'Shin_L')}
BIND=[('Hair_Back','Head'),('Hand_L','Elbow_L'),('Leg_Upper_L','Thigh_L'),('Leg_Lower_L','Shin_L'),('Boot_L','Foot_L'),
 ('Leg_Upper_R','Thigh_R'),('Leg_Lower_R','Shin_R'),('Boot_R','Foot_R'),('Dress','Hip'),('Coat_Hem','Hip'),
 ('Coat_Body','Body'),('Head','Head'),('Hair_Front','Head'),('Arm_Upper_R','Shoulder_R'),('Arm_Lower_R','Elbow_R'),
 ('Hand_R','Wrist_R'),('Lantern','Lantern')]
img={}
for n,_ in BIND:
  im=Image.open(P+n+'.png').convert('RGBA'); bb=im.getbbox(); c=im.crop(bb)
  c=c.resize((max(1,round(c.width*S)),max(1,round(c.height*S))),Image.LANCZOS)
  cx=(bb[0]+bb[2])/2*S; cy=(bb[1]+bb[3])/2*S
  img[n]=(c,cx,cy)
def path(b):
  p=J[b][2]; return (path(p)+'/' if p else '')+b
def sample(vals,times,t):
  for i in range(len(times)-1):
    if times[i]<=t<=times[i+1]:
      u=(t-times[i])/(times[i+1]-times[i]); u=u*u*(3-2*u)
      return vals[i]+(vals[i+1]-vals[i])*u
  return vals[-1]
def pose(clip,t):
  c=CLIPS[clip]; keys=c['keys']; n=len(next(iter(keys.values())))
  times=c.get('times',[c['length']*i/(n-1) for i in range(n)])
  return {k:sample(v,times,t) for k,v in keys.items()}
def world(pz):
  W={}
  def get(b):
    if b in W: return W[b]
    x,y,p=J[b]; X=x*3/S*S; Y=-y*3   # y-up preview px (3x)
    X=x*3
    rot=pz.get(path(b),0)
    if b=='Hip' and 'Hip:y' in pz: Y+= (pz['Hip:y']-HIP_Y)*200*3
    if p is None: W[b]=(X,Y,rot); return W[b]
    px,py,pr=get(p); ox,oy=x*3-J[p][0]*3, -(y*3-J[p][1]*3)
    a=math.radians(pr); wx=px+ox*math.cos(a)-oy*math.sin(a); wy=py+ox*math.sin(a)+oy*math.cos(a)
    W[b]=(wx,wy,pr+rot); return W[b]
  for b in J: get(b)
  return W
def frame(clip,t,size=(700,1020)):
  pz=pose(clip,t); W=world(pz); out=Image.new('RGBA',size,(24,32,52,255))
  ox,oy=size[0]//2-230, 60
  for n,b in BIND:
    c,cx,cy=img[n]; bx,by,br=W[b]; jx,jy=J[b][0]*3,J[b][1]*3
    # sprite centre relative to joint (rest), rotate by world rot
    dx,dy=cx-jx,-(cy-jy); a=math.radians(br)
    sx=bx+dx*math.cos(a)-dy*math.sin(a); sy=by+dx*math.sin(a)+dy*math.cos(a)
    r=c.rotate(br,resample=Image.BICUBIC,expand=True)
    out.alpha_composite(r,(int(round(ox+sx-r.width/2)),int(round(oy-sy-r.height/2))))
  return out,pz.get('LIGHT',1.0)
if __name__=='__main__':
  fps=30; sheets=[]
  for clip,c in CLIPS.items():
    L=c['length']; n=int(round(L*fps))+1
    fr=[frame(clip,i/fps)[0] for i in range(n)]
    fr[0].save(clip+'.gif',save_all=True,append_images=fr[1:]+([] if c['loop'] else [fr[-1]]*15),duration=int(1000/fps),loop=0,disposal=2)
    picks=[fr[int(i*(n-1)/4)].resize((350,510)) for i in range(5)]
    s=Image.new('RGBA',(350*5,510)); [s.paste(p,(i*350,0)) for i,p in enumerate(picks)]; sheets.append(s)
  big=Image.new('RGBA',(1750,510*len(sheets))); [big.paste(s,(0,i*510)) for i,s in enumerate(sheets)]
  big.convert('RGB').save('contact_sheet.png'); print('ok')
