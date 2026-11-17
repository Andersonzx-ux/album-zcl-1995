import sys, numpy as np, colorsys
from PIL import Image
a=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(float)
hx=lambda c:'#%02x%02x%02x'%tuple(int(round(v)) for v in c)
def reg(n,x0,y0,x1,y1):
    r=a[y0:y1,x0:x1].reshape(-1,3); print(f'{n:14s} med {hx(np.median(r,0))} mean {hx(r.mean(0))}')
reg('sky-top',1000,300,1380,500); reg('sky-low',1000,700,1380,880); reg('sky-near-title',700,20,880,120)
reg('rock-left',10,300,120,700); reg('rock-top',100,20,380,160); reg('rock-mid',150,700,230,1000)
reg('ground',200,1320,1380,1395); reg('hills',1100,1000,1380,1150); reg('hills-far',1060,920,1380,960)
reg('denim',250,700,420,950); reg('shirt',400,260,470,480); reg('black-pants',700,700,900,1000)
reg('title-letters',900,100,1340,170)
f=a.reshape(-1,3)[::13]; hsv=np.array([colorsys.rgb_to_hsv(*(p/255)) for p in f]); l=f@[.2126,.7152,.0722]
def sel(n,m): print(n,m.sum(),hx(np.median(f[m],0)) if m.sum() else '-')
sel('rock bright',(hsv[:,0]<.08)&(hsv[:,1]>.5)&(hsv[:,2]>.8))
sel('rock mid',(hsv[:,0]<.08)&(hsv[:,1]>.5)&(hsv[:,2]>.6)&(hsv[:,2]<.8))
sel('rock deep',(hsv[:,0]<.07)&(hsv[:,1]>.5)&(hsv[:,2]>.35)&(hsv[:,2]<.6))
sel('rock dark',(hsv[:,0]<.08)&(hsv[:,1]>.4)&(hsv[:,2]>.15)&(hsv[:,2]<.35))
sel('sky blue',(hsv[:,0]>.55)&(hsv[:,0]<.7)&(hsv[:,2]>.8))
sel('black',(l<30))
sel('olive',(hsv[:,0]>.12)&(hsv[:,0]<.25)&(hsv[:,1]>.25))
# eroded title letters (darkest in title box)
t=a[70:235,880:1360].reshape(-1,3); tl=t@[.2126,.7152,.0722]; print('title dark',hx(np.median(t[tl<np.percentile(tl,8)],0)))
