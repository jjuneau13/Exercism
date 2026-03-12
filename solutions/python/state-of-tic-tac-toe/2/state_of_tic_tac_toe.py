from collections import Counter
def gamestate(board):
    cols = [[board[row][col] for row in range(3)] for col in range(3)]
    diags = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    count = Counter(''.join(board))
    rwins, cwins, dwins = 0, 0, 0
    if count['X'] < count['O']:
        raise ValueError('Wrong turn order: O started')
    if count['X'] > count['O'] + 1:
        raise ValueError('Wrong turn order: X went twice')
    for num, row in enumerate(board):
        if win(row):
            rwins += 1
        if win(cols[num]):
            cwins += 1
        if num < 2:
            if win(diags[num]):
                dwins += 1
    if cwins > 1 or rwins > 1:
        raise ValueError('Impossible board: game should have ended after the game was won')
    if rwins == 1 or cwins == 1 or dwins > 0:
        return 'win'
    if not count[' ']:
        return 'draw'
    return 'ongoing'

def win(row):
    if ((len(row)) == 3 and len(set(row)) == 1 and row.count(' ') == 0):
        return True