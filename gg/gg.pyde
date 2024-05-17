dirx=400
diry=400
x=400
y=700
def setup():
    size (800,800)
    
def draw():
    global dirx,diry,x,y
    background (255,255,255)
    ellipse(dirx,diry,100,100)
    
    rect (x,y, 150,25)
    dirx=dirx+3
    diry=diry-2
    if dirx>799:
        dirx=dirx-3
    if diry>799:
        diry=diry+2
    if dirx<1:
        dirx=dirx+3
    if diry>799:
        diry=diry-2
    if keyPressed==True:
         if key=="d" or key=="D":
            x=x+10
         if key=="a" or key=="A":
            x=x-10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
