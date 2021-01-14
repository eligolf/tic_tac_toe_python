def p(b):
    b2 = ['-' if i == 0 else 'O' if i == -1 else 'X' if i == 1 else i for i in b]
    [print(f'\n{b2[r*3:3+r*3]}') if r == 0 else print(b2[r*3:3+r*3]) for r in range(3)]
def w(b):
    for l in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
        if b[l[0]] == b[l[1]] == b[l[2]] != 0: return 1
def r():
    b, t = [0]*9, 1
    p(b)
    while 1:
        u = input('\nPlease enter your move (1-9): ')
        if u.isnumeric() and int(u)-1 in range(9) and b[int(u)-1] == 0:
            b[int(u)-1], t = t, t*-1
            p(b)
        if w(b) or 0 not in b:
            x = f'\n{"X" if t == -1 else "O"} won!' if w(b) else 'Game drawn!'
            if input(f'{x} Do you want to play again (y/n)? ') != 'y': break
            r()
            break
r()