
def won(i, j):
    global board

    player = board[i][j]

    is_winner = (board[i][0] == player) and (board[i][1] == player) and (board[i][2] == player)
    if is_winner:
        return True

    is_winner = (board[0][j] == player) and (board[1][j] == player) and (board[2][j] == player)
    if is_winner:
        return True

    if i == j:
        is_winner = (board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player)
        if is_winner:
            return True

    if i == 2-j:
        is_winner = (board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player)
        if is_winner:
            return True

    return False

def play_game(player):
    global board

    WON = 1
    LOSE = 0
    DRAW = -1

    draw_move = None
    for i in xrange(3):
        for j in xrange(3):
            move_code = 3 * i + j
            if board[i][j] == 0:
                board[i][j] = player
                if not won(i, j):
                    move = play_game(-player)
                    if move == None:
                        board[i][j] = 0
                        return (DRAW, move_code)

                    if move[0] == LOSE:
                        board[i][j] = 0
                        return (WON, move_code)

                    if move[0] == DRAW:
                        draw_move = (DRAW, move_code)
                    elif draw_move == None:
                        draw_move = (LOSE, move_code)
 
                elif draw_move == None:
                    draw_move = (LOSE, move_code)
                    
                board[i][j] = 0

    return draw_move

for i in xrange(int(raw_input())):
    line_board = [int(w) for w in raw_input().split()]
    board = [[line_board[i * 3 + j] for j in xrange(3)] for i in xrange(3)]

    move = play_game(1)
    if move == None:
        print [i for i in xrange(9) if line_board[i] == 0][0]
    else:
        print move[1]
