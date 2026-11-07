# Placeholder Home ground floor (present, cold). Replace with painted art later; keep FLOOR_TOP.
from PIL import Image, ImageDraw, ImageFilter
import random, math
W,H=2400,1080; FLOOR_TOP=H-160
random.seed(3)
INK=(18,22,32); WALL=(62,76,96); WALL2=(52,64,82); WALL3=(74,90,112)
WOOD=(70,58,52); WOOD2=(54,44,40); WOODL=(92,78,68); SHEET=(150,164,180); SHEET2=(118,132,150)
im=Image.new('RGB',(W,H),WALL); d=ImageDraw.Draw(im)
def poly(p,f,o=INK,w=4): d.polygon(p,fill=f); d.line(p+[p[0]],fill=o,width=w,joint='curve')
def rect(x0,y0,x1,y1,f,o=INK,w=4): d.rectangle((x0,y0,x1,y1),fill=f,outline=o,width=w)
# stone wall blocks
y=110
while y<FLOOR_TOP:
    h=random.randint(70,95); x=-random.randint(0,120)
    while x<W:
        w=random.randint(140,230); c=random.choice([WALL,WALL2,WALL3,WALL])
        d.rounded_rectangle((x+4,y+4,x+w-4,y+h-4),radius=14,fill=c,outline=(40,50,66),width=3); x+=w
    y+=h
# ceiling + beams
rect(-5,-5,W+5,110,(36,42,56))
for bx in range(80,W,360): rect(bx,0,bx+60,130,WOOD2)
d.rectangle((0,100,W,130),fill=WOOD,outline=INK,width=4)
# attic hole (right) + broken ladder
rect(1980,-5,2240,132,(10,12,18))
LADDER_TOP=(2020,120); 
for side in (0,110):
    x0=1930+side; poly([(x0,FLOOR_TOP),(x0+22,FLOOR_TOP),(x0+92,130),(x0+70,130)],WOOD)
for i,t in enumerate([0.1,0.25,0.4,0.55,0.7,0.85]):
    if i in (2,3,4): # missing rungs: stubs only
        yy=FLOOR_TOP-(FLOOR_TOP-130)*t; xx=1941+(70)*t
        d.line((xx,yy,xx+18,yy+6),fill=WOODL,width=8); continue
    yy=FLOOR_TOP-(FLOOR_TOP-130)*t; xx=1941+70*t
    d.line((xx,yy,xx+112,yy),fill=INK,width=12); d.line((xx,yy,xx+112,yy),fill=WOODL,width=6)
# fallen rungs on floor
d.line((2150,FLOOR_TOP-8,2260,FLOOR_TOP-20),fill=INK,width=12); d.line((2150,FLOOR_TOP-8,2260,FLOOR_TOP-20),fill=WOODL,width=6)
# door (left)
rect(90,330,330,FLOOR_TOP,WOOD); 
for px in (150,210,270): d.line((px,340,px,FLOOR_TOP-5),fill=WOOD2,width=4)
d.ellipse((295,600,315,620),fill=(150,130,90),outline=INK,width=3)
# fireplace
rect(480,420,860,FLOOR_TOP,(84,92,104)); rect(540,560,800,FLOOR_TOP,(14,16,22)); rect(460,400,880,440,(96,104,116))
for i in range(5): d.ellipse((580+i*40,FLOOR_TOP-30,640+i*40,FLOOR_TOP-5),fill=(40,40,44),outline=INK,width=2)
# rocking chair (silhouette-ish, cel)
cx=980
poly([(cx,FLOOR_TOP-260),(cx+30,FLOOR_TOP-260),(cx+50,FLOOR_TOP-120),(cx+20,FLOOR_TOP-120)],WOOD)
poly([(cx+20,FLOOR_TOP-130),(cx+170,FLOOR_TOP-130),(cx+170,FLOOR_TOP-110),(cx+20,FLOOR_TOP-110)],WOOD)
for lx in (cx+35,cx+150): d.line((lx,FLOOR_TOP-112,lx,FLOOR_TOP-30),fill=INK,width=12); d.line((lx,FLOOR_TOP-112,lx,FLOOR_TOP-30),fill=WOOD,width=6)
d.arc((cx-40,FLOOR_TOP-90,cx+230,FLOOR_TOP+30),200,340,fill=INK,width=12); d.arc((cx-40,FLOOR_TOP-90,cx+230,FLOOR_TOP+30),200,340,fill=WOODL,width=6)
# window with sea + dark lighthouse
WX0,WY0,WX1,WY1=1240,300,1560,600
rect(WX0-16,WY0-16,WX1+16,WY1+16,WOOD)
sky=Image.new('RGB',(WX1-WX0,WY1-WY0)); sd=ImageDraw.Draw(sky)
for yy in range(WY1-WY0):
    t=yy/(WY1-WY0); sd.line((0,yy,WX1,yy),fill=(int(40+30*t),int(56+34*t),int(84+30*t)))
sd.ellipse((210,40,260,90),fill=(214,222,230))
sd.rectangle((0,200,320,300),fill=(34,46,66))
sd.polygon([(0,230),(120,190),(180,200),(180,300),(0,300)],fill=(22,28,40))
sd.polygon([(120,190),(132,110),(146,110),(156,193)],fill=(30,36,50)); sd.rectangle((128,96,150,112),fill=(30,36,50))
im.paste(sky.filter(ImageFilter.GaussianBlur(1)),(WX0,WY0))
d.line((WX0+(WX1-WX0)//2,WY0,WX0+(WX1-WX0)//2,WY1),fill=WOOD,width=12); d.line((WX0,WY0+(WY1-WY0)//2,WX1,WY0+(WY1-WY0)//2),fill=WOOD,width=12)
rect(WX0-30,WY1+14,WX1+30,WY1+36,WOODL)
# moonlight shaft
shaft=Image.new('L',(W,H),0); sh=ImageDraw.Draw(shaft)
sh.polygon([(WX0,WY0),(WX1,WY0),(WX1+260,FLOOR_TOP),(WX0+80,FLOOR_TOP)],fill=38)
im=Image.composite(Image.new('RGB',(W,H),(170,190,215)),im,shaft.filter(ImageFilter.GaussianBlur(30))); d=ImageDraw.Draw(im)
# sheet-covered furniture
def sheet(x,w,h):
    pts=[(x,FLOOR_TOP),(x+10,FLOOR_TOP-h+40),(x+40,FLOOR_TOP-h),(x+w-40,FLOOR_TOP-h+6),(x+w-8,FLOOR_TOP-h+50),(x+w,FLOOR_TOP)]
    poly(pts,SHEET)
    for i in range(3): fx=x+w*(0.25+0.25*i); d.line((fx,FLOOR_TOP-h+30,fx-10+i*8,FLOOR_TOP-4),fill=SHEET2,width=6)
sheet(1600,240,210); sheet(1340,150,130)
# sea chest
rect(1700,FLOOR_TOP-120,1880,FLOOR_TOP,WOOD); d.rectangle((1690,FLOOR_TOP-140,1890,FLOOR_TOP-112),fill=WOODL,outline=INK,width=4)
for bx in (1730,1840): d.rectangle((bx,FLOOR_TOP-140,bx+14,FLOOR_TOP),fill=(110,96,70),outline=INK,width=2)
# floor
d.rectangle((0,FLOOR_TOP,W,H),fill=WOOD)
d.line((0,FLOOR_TOP,W,FLOOR_TOP),fill=INK,width=6)
for yy in (FLOOR_TOP+50,FLOOR_TOP+105): d.line((0,yy,W,yy),fill=WOOD2,width=4)
x=0
while x<W: x+=random.randint(180,320); r=random.choice([0,1]); d.line((x,FLOOR_TOP+(0 if r else 50),x,FLOOR_TOP+(50 if r else 105)),fill=WOOD2,width=4)
# vignette
v=Image.new('L',(W,H),0); vd=ImageDraw.Draw(v); vd.rectangle((0,0,W,H),fill=110); vd.ellipse((-300,-200,W+300,H+250),fill=0)
im=Image.composite(Image.new('RGB',(W,H),(10,12,20)),im,v.filter(ImageFilter.GaussianBlur(120)))
im.save('../Home_Present_placeholder_v0.png')
# crate prop
c=Image.new('RGBA',(130,110),(0,0,0,0)); cd=ImageDraw.Draw(c)
cd.rectangle((3,3,126,106),fill=WOOD,outline=INK,width=5); cd.line((8,8,122,102),fill=WOOD2,width=10); cd.rectangle((3,3,126,20),fill=WOODL,outline=INK,width=4)
c.save('../Crate_placeholder_v0.png'); print('ok FLOOR_TOP',FLOOR_TOP)
