def p(b):[print([[' ','O','X'][i]for i in b][x:x+3])for x in [0,3,6]]
def e(b,t):
    for i,d in(0,1),(3,1),(6,1),(0,3),(1,3),(2,3),(0,4),(2,2):
        if b[i]==b[i+d]==b[i+2*d]==t:return 1
def n(b,d,t):
    if e(b,t):return 0,1
    if e(b,-t):return 0,-1
    if all(b):return 0,0
    x=-2
    for m in range(9):
        if b[m]==0:
            b[m]=t;s,b[m]=-n(b,d-1,-t)[1],0
            if s>x:x,y=s,m
    return y,x
def g():
    b,w=[0]*9,1
    while 1:
        p(b)
        if all(b)or(e(b,w)or e(b,-w)):
            if i('?')!='y':break
            g()
            break
        if w>0:
            u=i(':')
            if u.isdigit():
                u=int(u)-1
                if u<9&~b[u]:b[u],w=-1,-1
        else:(m,s),b[m],w=n(b,8,1),1,1
i=input;g()
