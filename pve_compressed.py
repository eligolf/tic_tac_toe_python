def f(b):
    [print(['X' if i<0 else 'O' if i>0 else ' ' for i in b][x*3:3+x*3]) for x in r(3)]
def e(b,t):
    for p in ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]):
        if b[p[0]]==b[p[1]]==b[p[2]]==t: return 1
def n(b,d,t):
    if e(b,t): return 0,9
    if e(b,-t): return 0,-9
    if 0 not in b: return 0,0
    x=-20
    for m in r(9):
        if not b[m]:
            b[m]=t
            s=-n(b,d-1,-t)[1]
            b[m]=0
            if s>x:x,y=s,m
    return y,x
def g():
    b,w=[0]*9,1
    f(b)
    while 1:
        if 0 not in b or (e(b,w) or e(b,-w)):
            if i('?')!='y': break
            g()
            break
        if w>0:
            while 1:
                u=i(':')
                if u.isnumeric():u=int(u)-1
                    if u<9 and not b[u]:
                        b[u],w=-1,w*-1
                        f(b)
                        break
        if w<0:
            m,s=n(b,8,1)
            b[m],w=1,w*-1
            f(b)
i,r=input,range
g()
