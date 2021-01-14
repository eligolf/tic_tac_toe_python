def p(b):
    b2 = [' ' if i == 0 else 'X' if i == -1 else 'O' if i == 1 else i for i in b]
    [print(f'\n{b2[r*3:3+r*3]}') if r == 0 else print(b2[r*3:3+r*3]) for r in range(3)]
def e(b, t):
    for p in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
        if b[p[0]] == b[p[1]] == b[p[2]] == t: return 1
def nm(b, d, t):
    if e(b, t) == 1: return None, (10+d)
    if e(b, -t) == 1: return None, -(10 + d)
    if 0 not in b: return None, 0
    bs = -20
    for m in [i for i in range(len(b)) if b[i] == 0]:
        b[m] = t
        score = -nm(b, d - 1, -t)[1]
        b[m] = 0
        if score > bs: bs, bm = score, m
    return bm, bs
def r():
    b, ut = [0]*9, -1
    p(b)
    while 1:
        if ut == -1 and not e(b, ut) and not e(b, -ut) and 0 in b:
            while 1:
                u = input('\nPlease enter your move (1-9): ')
                if u.isnumeric() and int(u) - 1 in range(9) and b[int(u) - 1] == 0:
                    b[int(u)-1], ut = -1, ut*-1
                    p(b)
                    break
        elif ut == 1 and not e(b, ut) and not e(b, -ut) and 0 in b:
            move, score = nm(b, 8, 1)
            b[move], ut = 1, ut*-1
            p(b)
        else:
            text = 'You won!' if e(b, -1) else 'AI won!' if e(b, 1) else 'Game drawn!'
            if input(f'\n{text} Do you want to play again (y/n)? ').lower() != 'y': break
            r()
            break
r()