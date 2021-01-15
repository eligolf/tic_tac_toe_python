def p(b):
    c = [' ' if i == 0 else 'X' if i == -1 else 'O' if i == 1 else i for i in b]
    [print(f'\n{c[r*3:3+r*3]}') if r == 0 else print(c[r*3:3+r*3]) for r in range(3)]
def e(b, t):
    for p in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
        if b[p[0]] == b[p[1]] == b[p[2]] == t: return 1
def n(b, d, t):
    if e(b, t): return 0, (9+d)
    if e(b, -t): return 0, -(9 + d)
    if 0 not in b: return 0, 0
    x = -20
    for m in [i for i in range(9) if not b[i]]:
        b[m] = t
        s = -n(b, d - 1, -t)[1]
        b[m] = 0
        if s > x: x, y = s, m
    return y, x
def r():
    b, w = [0]*9, -1
    p(b)
    while 1:
        if w == -1 and not (e(b, w) or e(b, -w)) and 0 in b:
            while 1:
                u = input('\nPlease enter your move (1-9): ')
                if u.isnumeric():
                    u = int(u)-1
                    if 0 <= u < 9 and not b[u]:
                        b[u], w = -1, w*-1
                        p(b)
                        break
        elif w == 1 and not (e(b, w) or e(b, -w)) and 0 in b:
            move, score = n(b, 8, 1)
            b[move], w = 1, w*-1
            p(b)
        else:
            f = 'You won!' if e(b, -1) else 'AI won!' if e(b, 1) else 'Game drawn!'
            if input(f'\n{f} Do you want to play again (y/n)? ') != 'y': break
            r()
            break
r()