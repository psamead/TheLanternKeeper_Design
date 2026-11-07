import os,math,importlib
from PIL import Image
picks=[('Maela_Run',0.0),('Maela_Run',0.125),('Maela_Run',0.25),('Maela_Run',0.375),('Maela_JumpUp',0.3),('Maela_Fall',0.15),('Maela_Lantern',0.5)]
rows=[]
for tag in ['canvas_v1','canvas_v13']:
  os.environ['PARTS']='../fix_v1.3/'+tag
  import render; importlib.reload(render)
  row=Image.new('RGB',(7*300,480),(255,0,255))
  for i,(c,t) in enumerate(picks):
    pz=render.pose(c,t);W=render.world(pz);fr=Image.new('RGBA',(700,1020),(255,0,255,255));ox,oy=120,60
    for n,b in render.BIND:
      im,cx,cy=render.img[n];bx,by,br=W[b];jx,jy=render.J[b][0]*3,render.J[b][1]*3
      dx,dy=cx-jx,-(cy-jy);a=math.radians(br)
      sx=bx+dx*math.cos(a)-dy*math.sin(a);sy=by+dx*math.sin(a)+dy*math.cos(a)
      r=im.rotate(br,resample=Image.NEAREST,expand=True)
      fr.alpha_composite(r,(int(round(ox+sx-r.width/2)),int(round(oy-sy-r.height/2))))
    row.paste(fr.crop((40,180,520,1000)).resize((300,512)).crop((0,30,300,510)).convert('RGB'),(i*300,0))
  rows.append(row)
o=Image.new('RGB',(2100,970),(30,30,30));o.paste(rows[0],(0,0));o.paste(rows[1],(0,490));o.save('compare_v1_v13.jpg',quality=88)
