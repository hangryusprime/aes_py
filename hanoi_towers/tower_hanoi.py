def hanoi_tower(n=None):
    if n is None:
        n = int(input('Please input the tower size: '))
    steps = []
    x = ['Peg1'] + list(range(1, n + 1))
    y = ['Peg2']
    z = ['Peg3']
    comb1 = [x, '-', y, '-', z]
    steps.append("".join(map(str, comb1)))

    def tower_solver(n, x, y, z):
        if n != 1:
            tower_solver(n-1, x, z, y)
            tower_solver(1, x, y, z)
            tower_solver(n-1, y, x, z)
        else:
            steps.append(print_step(x, y, z))

    tower_solver(n, x, y, z)
    return steps


def print_step(a=[], b=[], c=[]):
    if a[0] == 'Peg1' and b[0] == 'Peg2':
        c.insert(1, a.pop(1))
        comb = [a, '-', b, '-', c]
        return("".join(map(str, comb)))
    elif a[0] == 'Peg1' and b[0] == 'Peg3':
        c.insert(1, a.pop(1))
        comb = [a, '-', c, '-', b]
        return("".join(map(str, comb)))
    elif a[0] == 'Peg2' and b[0] == 'Peg1':
        c.insert(1, a.pop(1))
        comb = [b, '-', a, '-', c]
        return("".join(map(str, comb)))
    elif a[0] == 'Peg2' and b[0] == 'Peg3':
        c.insert(1, a.pop(1))
        comb = [c, '-', a, '-', b]
        return("".join(map(str, comb)))
    elif a[0] == 'Peg3' and b[0] == 'Peg1':
        c.insert(1, a.pop(1))
        comb = [b, '-', c, '-', a]
        return("".join(map(str, comb)))
    elif a[0] == 'Peg3' and b[0] == 'Peg2':
        c.insert(1, a.pop(1))
        comb = [c, '-', b, '-', a]
        return("".join(map(str, comb)))


#if __name__ == '__main__':
#    hanoi_tower()
