def e(b):return any([b[i]==b[i+d]==b[i+2*d]!=0 for i,d in((0,1),(3,1),(6,1),(0,3),(1,3),(2,3),(0,4),(2,2))])
b,w=[0]*9,1
while 1:
    [print([[' ','O','X'][i]for i in b][x:x+3])for x in[0,3,6]]
    if all(b)or e(b):break
    u=input()
    if u.isdigit():
        u=int(u)-1
        if u<9and not b[u]:b[u],w=w,w*-1
