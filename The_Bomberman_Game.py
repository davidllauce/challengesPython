'''Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds.
Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb
detonates in cell , any valid cells  and  are cleared. If there is a bomb in a neighboring cell, the neighboring bomb
is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
After one second, Bomberman does nothing.
After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs.
No bombs detonate at this point.
After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back
and observes. Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact
same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine
the state of the grid after  seconds.
'''

''' Descomentar para datos de prueba estaticos'''
# r, c, n = 6, 7, 11
# grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']

# r, c, n = 192, 189, 2
# grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']


# r, c, n = 6, 7, 5
# grid = ['.......', '...O.O.', '....O..', '..O....', 'OO...OO', 'OO.O...']

# r, c, n = 1, 199, 181054341
# grid = [
#     'O..OO........O..O........OO.O.OO.OO...O.....OOO...OO.O..OOOOO...O.O..O..O.O..OOO..O..O..O....O...O....O...O..O..O....O.O.O.O.....O.....OOOO..O......O.O.....OOO....OO....OO....O.O...O..OO....OO..O...O']
''' Fin datos de prueba estatico'''

'''Descomentar para ingresar datos por consola'''

r, c, n = map(int, input().rstrip().split())
grid = []
for _ in range(r):
    grid_item = input()
    grid.append(grid_item)

''' Fin de ingresar datos consola'''

r = len(grid)
if n % 4 == 1:
    count = 2
else:
    count = 1

while (n > 1 and count > 0):
    a = []
    b = []

    for i in grid:
        c = len(i)
        a.append(list(i))
        b.append(list(['O'] * c))
    if n % 2 == 0:
        grid[:] = []
        grid = b
        break
    for i, vali in enumerate(a):
        for j, valj in enumerate(vali):
            if valj == 'O':
                b[i][j] = '.'
                if i + 1 < r: b[i + 1][j] = '.'
                if i - 1 < r and i - 1 > -1: b[i - 1][j] = '.'
                if j + 1 < c: b[i][j + 1] = '.'
                if j - 1 < c and j - 1 > -1: b[i][j - 1] = '.'
    grid[:] = []
    grid = b
    count -= 1

'''Con la de hackeran'''

# return o print([''.join(i) for i in grid])

'''Sin la función de hackeran'''
for row in grid:
    print(''.join([str(elem) for elem in row]))
