# Nhóm 16
# Nguyễn Thanh Nghị     - MSSV: N19DCCN120
# Lê Đăng Khánh         - MSSV: N19DCCN089
# Trần Minh Long        - MSSV: N19DCCN100
#
import pygame
from tkinter import messagebox

#Mảng quản lí các ô cờ
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Giới hạn các giá trị max min
MAX = 2
MIN = -2

FPS = 60


check_x = 1
check_o = -1

def is_move_left(state):
    for i in range(3):
        for j in range(3):
            if (state[i][j] == 0):
                return True
    return False

def check_winner(state):
    for row in range(3):
        if state[row][0] == state[row][1] and state[row][1] == state[row][2]:
            if state[row][0] == check_x:
                return 10
            elif state[row][0] == check_o:
                return -10
    for col in range(3):
        if state[0][col] == state[1][col] and state[1][col] == state[2][col]:
            if state[0][col] == check_x:
                return 10
            elif state[0][col] == check_o:
                return -10
    if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        if state[0][0] == check_x:
            return 10
        elif state[0][0] == check_o:
            return -10

    if state[0][2] == state[1][1] and state[1][1] == state[2][0]:

        if state[0][2] == check_x:
            return 10
        elif state[0][2] == check_o:
            return -10

    # Chưa thắng = 0
    return 0

def alphabeta(state, depth, a, b, is_max):
    score = check_winner(state)
    if score != 0:
        return score
    if not is_move_left(state):
        return 0
    if is_max:
        best = MIN
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = check_x
                    best = max(best, alphabeta(state, depth + 1, a, b, not is_max))
                    a = max(best, a)
                    state[i][j] = 0
                    if b <= a:
                        break
        return best
    else:
        best = MAX
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = check_o
                    best = min(best, alphabeta(state, depth + 1, a, b, not is_max))
                    b = min(best, b)
                    state[i][j] = 0
                    if b <= a:
                        break
        return best


def minimax(state, depth, is_max):
    score = check_winner(state)
    if score != 0:
        return score

    if not is_move_left(state):
        return 0

    if is_max:
        best = MIN
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = check_x
                    best = max(best, minimax(state, depth + 1, not is_max))
                    state[i][j] = 0
        return best
    else:
        best = MAX
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = check_o
                    best = min(best, minimax(state, depth + 1, not is_max))
                    state[i][j] = 0
        return best

def find_best_move(board):
    best_val = -2
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = check_x
                # move_val = minimax(board, 0, False)
                move_val = alphabeta(board, 0, -2, 2, False)
                board[i][j] = 0
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    print(best_move)
    return best_move

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.flip()
    pygame.display.set_caption("CARO 3x3")
    x_img = pygame.transform.smoothscale(pygame.image.load("X.png").convert(), (123, 123))
    o_img = pygame.transform.smoothscale(pygame.image.load("O.png").convert(), (123, 123))
    running = True
    clock = pygame.time.Clock()

    x = 200
    y = 25
    turn = 0
    while running:
        result = check_winner(grid)
        if result != 0:
            running = False
        if turn > 9:
            running = False
        screen.fill((0, 0, 0))
        cellIndexX = 0
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x + i * 125, y + j * 125, 125, 125), 1)
                if grid[i][j] == 1:
                    screen.blit(x_img, (x + j * 125, y + i * 125))
                if grid[i][j] == -1:
                    screen.blit(o_img, (x + j * 125, y + i * 125))
        for event in pygame.event.get():
            if not is_move_left(grid):
                running = False
            if event.type == pygame.QUIT:
                running = False
                exit();
            if turn % 2 == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0]
                    row = pos[1]
                    if col > 200 and col < 325:
                        if row > 25 and row < 150:
                            if grid[0][0] == 0:
                                grid[0][0] = 1
                                turn += 1
                        if row > 150 and row < 275:
                            if grid[1][0] == 0:
                                grid[1][0] = 1
                                turn += 1
                        if row > 275 and row < 400:
                            if grid[2][0] == 0:
                                grid[2][0] = 1
                                turn += 1
                    elif col > 325 and col < 450:
                        if row > 25 and row < 150:
                            if grid[0][1] == 0:
                                grid[0][1] = 1
                                turn += 1
                        if row > 150 and row < 275:
                            if grid[1][1] == 0:
                                grid[1][1] = 1
                                turn += 1
                        if row > 275 and row < 400:
                            if grid[2][1] == 0:
                                grid[2][1] = 1
                                turn += 1
                    elif col > 450 and col < 575:
                        if row > 25 and row < 150:
                            if grid[0][2] == 0:
                                grid[0][2] = 1
                                turn += 1
                        if row > 150 and row < 275:
                            if grid[1][2] == 0:
                                grid[1][2] = 1
                                turn += 1
                        if row > 275 and row < 400:
                            if grid[2][2] == 0:
                                grid[2][2] = 1
                                turn += 1
            else:
                bot_move = find_best_move(grid)
                grid[bot_move[0]][bot_move[1]] = -1
                turn += 1

        pygame.display.update()
        clock.tick(FPS)


    if result == 10:
        messagebox.showinfo('Result', 'You win!')
    elif result == -10:
        messagebox.showinfo('Result', 'You lose!')
    else:
        messagebox.showinfo('Result', 'Draw!')
