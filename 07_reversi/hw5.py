import random
 
 
class MyPlayer:
    """Hrac bude hrat nahodne"""
 
    def __init__(self, my_color, opponent_color):
        self.name = "remelvic"
        self.my_color = my_color
        self.opponent_color = opponent_color
 
    def move(self, board):
        positions = []  # first positions in a board
        for new_r in range(len(board)):
            for new_c in range(len(board[new_r])):
                if board[new_r][new_c] == self.my_color:
                    positions.append((new_r, new_c))
 
        all_stone = []
        for j in positions:
            possible_moves = self.find_move(board, j[0], j[1])
            if possible_moves != []:
                all_stone.append(possible_moves)
 
        if len(all_stone) == 0:  # if don't have moves
            return None
 
        final_move = int(random.random() * len(all_stone))
        final_move2 = int(random.random() * len(all_stone[final_move]))
 
        return all_stone[final_move][final_move2]
 
    def find_move(self, board, r, c):
        # search we can go
        possible_moves = []
        start_r = r
        start_c = c
 
        # cell up
        while r - 1 >= 0:
            if board[start_r - 1][start_c] != self.opponent_color:
                break
            if board[r - 1][c] == -1:
                possible_moves.append((r - 1, c))
                break
            elif board[r - 1][c] == self.my_color:
                break
            else:
                r -= 1
        r = start_r
        c = start_c
        # cell up-right
        while r - 1 >= 0 and c + 1 <= 7:
            if board[start_r - 1][start_c + 1] != self.opponent_color:
                break
            if board[r - 1][c + 1] == -1:
                possible_moves.append((r - 1, c + 1))
                break
            elif board[r - 1][c + 1] == self.my_color:
                break
            else:
                r -= 1
                c += 1
        r = start_r
        c = start_c
 
        # cell right
        while c + 1 <= 7:
            if board[start_r][start_c + 1] != self.opponent_color:
                break
            if board[r][c + 1] == -1:
                possible_moves.append((r, c + 1))
                break
            elif board[r][c + 1] == self.my_color:
                break
            else:
                c += 1
        r = start_r
        c = start_c
 
        # cell right-down
        while r + 1 <= 7 and c + 1 <= 7:
            if board[start_r + 1][start_c + 1] != self.opponent_color:
                break
            if board[r + 1][c + 1] == -1:
                possible_moves.append((r + 1, c + 1))
                break
            elif board[r + 1][c + 1] == self.my_color:
                break
            else:
                r += 1
                c += 1
        r = start_r
        c = start_c
 
        # cell down
        while r + 1 <= 7:
            if board[start_r + 1][start_c] != self.opponent_color:
                break
            if board[r + 1][c] == -1:
                possible_moves.append((r + 1, c))
                break
            elif board[r + 1][c] == self.my_color:
                break
            else:
                r += 1
        r = start_r
        c = start_c
        # cell left-down
        while r + 1 <= 7 and c - 1 >= 0:
            if board[start_r + 1][start_c - 1] != self.opponent_color:
                break
            if board[r + 1][c - 1] == -1:
                possible_moves.append((r + 1, c - 1))
                break
            elif board[r + 1][c - 1] == self.my_color:
                break
            else:
                r += 1
                c -= 1
        r = start_r
        c = start_c
 
        # cell left
        while c - 1 >= 0:
            if board[start_r][start_c - 1] != self.opponent_color:
                break
            if board[r][c - 1] == -1:
                possible_moves.append((r, c - 1))
                break
            elif board[r][c - 1] == self.my_color:
                break
            else:
                c -= 1
        r = start_r
        c = start_c
 
        # cell left-up
        while r - 1 >= 0 and c - 1 >= 0:
            if board[start_r - 1][start_c - 1] != self.opponent_color:
                break
            if board[r - 1][c - 1] == -1:
                possible_moves.append((r - 1, c - 1))
                break
            elif board[r - 1][c - 1] == self.my_color:
                break
            else:
                r -= 1
                c -= 1
        r = start_r
        c = start_c
 
        return possible_moves
