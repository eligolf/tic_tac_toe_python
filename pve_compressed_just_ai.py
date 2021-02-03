def e(b,t):return any([b[i]==b[i+d]==b[i+2*d]==t for i,d in((0,1),(3,1),(6,1),(0,3),(1,3),(2,3),(0,4),(2,2))])
def n(b,t,d=8):
    if e(b,t):return 0,1
    if e(b,-t):return 0,-1
    if all(b):return 0,0
    x=-2
    for m in range(9):
        if b[m]==0:
            b[m]=t;s,b[m]=-n(b,-t,d-1)[1],0
            if s>x:x,y=s,m
    return y,x
