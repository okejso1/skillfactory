board = {
        '0': ['-', '-', '-'],
        '1': ['-', '-', '-'],
        '2': ['-', '-', '-'],
    }


def print_board():
    x0 = ' '.join(board['0'])
    x1 = ' '.join(board['1'])
    x2 = ' '.join(board['2'])
    print(' ', '0', '1', '2')
    print('0', x0)
    print('1', x1)
    print('2', x2)


def update_condition_x():
    a = int(input('enter row (0-2) for X: '))
    b = int(input('enter column (0-2) for X: '))

    if a == 0 and b == 0:
        board['0'][0] = 'x'
    if a == 0 and b == 1:
        board['0'][1] = 'x'
    if a == 0 and b == 2:
        board['0'][2] = 'x'

    if a == 1 and b == 0:
        board['1'][0] = 'x'
    if a == 1 and b == 1:
        board['1'][1] = 'x'
    if a == 1 and b == 2:
        board['1'][2] = 'x'

    if a == 2 and b == 0:
        board['2'][0] = 'x'
    if a == 2 and b == 1:
        board['2'][1] = 'x'
    if a == 2 and b == 2:
        board['2'][2] = 'x'


def update_condition_o():
    a = int(input('enter row (0-2) for O: '))
    b = int(input('enter column (0-2) for O: '))

    if a == 0 and b == 0:
        board['0'][0] = 'o'
    if a == 0 and b == 1:
        board['0'][1] = 'o'
    if a == 0 and b == 2:
        board['0'][2] = 'o'

    if a == 1 and b == 0:
        board['1'][0] = 'o'
    if a == 1 and b == 1:
        board['1'][1] = 'o'
    if a == 1 and b == 2:
        board['1'][2] = 'o'

    if a == 2 and b == 0:
        board['2'][0] = 'o'
    if a == 2 and b == 1:
        board['2'][1] = 'o'
    if a == 2 and b == 2:
        board['2'][2] = 'o'


def check_winner():
    if board['0'][0] == board['0'][1] and board['0'][1] == board['0'][2]:
        return board['0'][0]
    if board['1'][0] == board['1'][1] and board['1'][1] == board['1'][2]:
        return board['1'][0]
    if board['2'][0] == board['2'][1] and board['2'][1] == board['2'][2]:
        return board['2'][0]

    if board['0'][0] == board['1'][0] and board['1'][0] == board['2'][0]:
        return board['0'][0]
    if board['0'][1] == board['1'][1] and board['1'][1] == board['2'][1]:
        return board['0'][1]
    if board['0'][2] == board['1'][2] and board['1'][2] == board['2'][2]:
        return board['0'][2]

    if board['0'][0] == board['1'][1] and board['1'][1] == board['2'][2]:
        return board['0'][0]
    if board['2'][0] == board['1'][1] and board['1'][1] == board['0'][2]:
        return board['2'][0]


def main():
    while check_winner() != 'x' or check_winner() != 'o':
        if check_winner() == 'x' or check_winner() == 'o':
            print(check_winner(), 'is the WINNER!')
            break
        else:
            print_board()
            update_condition_x()
            check_winner()

        if check_winner() == 'x' or check_winner() == 'o':
            print(check_winner(), 'is the WINNER!')
            break
        else:
            print_board()
            update_condition_o()
            check_winner()


main()
