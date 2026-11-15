"""Dialogue box v1 for The Lantern Keeper — same language as TITLE_FRAME_v1:
double gold line, concave (cut-arc) corners, Breton ermine-tail (hermine) motif, dark navy fill.
Outputs (1080p sizes; @2x versions for crispness):
  DIALOGUE_BOX_v1.png (1600x300)  NAMEPLATE_v1.png (360x72)  NEXT_ICON_v1.png (40x40)
"""
import cairo, math
GOLD=(232/255,180/255,96/255); FILL=(14/255,22/255,36/255)
def hermine(c,x,y,s):
    # ermine spot: three dots on top + flared tail
    c.set_source_rgb(*GOLD)
    for dx,dy in [(-0.28,-0.62),(0.28,-0.62),(0,-0.92)]:
        c.arc(x+dx*s,y+dy*s,0.13*s,0,2*math.pi); c.fill()
    c.move_to(x,y-0.45*s); c.curve_to(x+0.08*s,y-0.1*s,x+0.25*s,y+0.25*s,x+0.42*s,y+0.55*s)
    c.line_to(x+0.14*s,y+0.42*s); c.line_to(x,y+0.62*s); c.line_to(x-0.14*s,y+0.42*s); c.line_to(x-0.42*s,y+0.55*s)
    c.curve_to(x-0.25*s,y+0.25*s,x-0.08*s,y-0.1*s,x,y-0.45*s); c.close_path(); c.fill()
def cut_rect(c,x,y,w,h,r):
    # rectangle whose corners are concave quarter-arcs of radius r
    c.new_path()
    c.move_to(x+r,y); c.line_to(x+w-r,y); c.arc_negative(x+w,y,r,math.pi,math.pi/2)
    c.line_to(x+w,y+h-r); c.arc_negative(x+w,y+h,r,-math.pi/2,-math.pi)
    c.line_to(x+r,y+h); c.arc_negative(x,y+h,r,0,-math.pi/2)
    c.line_to(x,y+r); c.arc_negative(x,y,r,math.pi/2,0); c.close_path()
def surface(w,h,k): s=cairo.ImageSurface(cairo.FORMAT_ARGB32,w*k,h*k); c=cairo.Context(s); c.scale(k,k); return s,c
def box(k):
    W,H=1600,300; s,c=surface(W,H,k)
    cut_rect(c,6,6,W-12,H-12,26); c.set_source_rgba(*FILL,0.88); c.fill()
    cut_rect(c,6,6,W-12,H-12,26); c.set_source_rgb(*GOLD); c.set_line_width(3); c.stroke()
    cut_rect(c,16,16,W-32,H-32,20); c.set_source_rgba(*GOLD,0.55); c.set_line_width(1.2); c.stroke()
    for x in (16+3,W-16-3):  # side motifs sit on the inner line, middle height
        c.set_source_rgba(*FILL,1); c.rectangle(x-14,H/2-24,28,48); c.fill(); hermine(c,x,H/2,26)
    # small diamonds at top/bottom centre
    for y in (6,H-6):
        c.set_source_rgba(*FILL,1); c.rectangle(W/2-18,y-6,36,12); c.fill()
        c.set_source_rgb(*GOLD); c.move_to(W/2,y-7); c.line_to(W/2+9,y); c.line_to(W/2,y+7); c.line_to(W/2-9,y); c.close_path(); c.fill()
    return s
def nameplate(k):
    W,H=360,72; s,c=surface(W,H,k)
    cut_rect(c,4,4,W-8,H-8,14); c.set_source_rgba(*FILL,0.95); c.fill()
    cut_rect(c,4,4,W-8,H-8,14); c.set_source_rgb(*GOLD); c.set_line_width(2.5); c.stroke()
    return s
def nexticon(k):
    W=H=40; s,c=surface(W,H,k); hermine(c,W/2,H/2+2,30); return s
for k,suf in ((1,''),(2,'@2x')):
    box(k).write_to_png(f'DIALOGUE_BOX_v1{suf}.png'); nameplate(k).write_to_png(f'NAMEPLATE_v1{suf}.png'); nexticon(k).write_to_png(f'NEXT_ICON_v1{suf}.png')
print('ok')
