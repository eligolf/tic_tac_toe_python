def p(b):[print(['X'if i<0 else'O'if i>0 else' 'for i in b][x*3:3+x*3])for x in r(3)]
def e(b,t):
    for i,d in (0,1),(3,1),(6,1),(0,3),(1,3),(2,3),(0,4),(2,2):
        if b[i]==b[i+d]==b[i+2*d]==t:return 1
def n(b,d,t):
    if e(b,t):return 0,9
    if e(b,-t):return 0,-9
    if all(b):return 0,0
    x=-20
    for m in r(9):
        if not b[m]:
            b[m]=t
            s,b[m]=-n(b,d-1,-t)[1],0
            if s>x:x,y=s,m
    return y,x
def g():
    b,w=[0]*9,1
    p(b)
    while 1:
        if all(b)or(e(b,w)or e(b,-w)):
            if i('?')!='y':break
            g()
            break
        if w>0:
            u=i(':')
            if u.isnumeric():
                u=int(u)-1
                if u<9 and not b[u]:
                    b[u],w=-1,w*-1
                    p(b)
        else:
            m,s=n(b,8,1)
            b[m],w=1,w*-1
            p(b)
i,r=input,range
g()
