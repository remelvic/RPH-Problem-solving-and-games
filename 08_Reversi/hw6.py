class MyPlayer:
    """Hrac otoci max. pocet kamenu a polozi svuj kamen na nejvyhodnejsi misto"""
 
    def __init__(self, my_color, opponent_color):
        self.name = "remelvic"
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.dict_of_stones = {}  # use for the number of inverted stones
        self.rating_board = {10: [(0, 0), (7, 7), (0, 7), (7, 0)],  # evaluating the board, trying to put the stone
                                                                    # in the most expensive position
                             9: [(0, 2), (0, 3), (0, 4), (0, 5), (2, 0), (2, 7), (3, 0), (3, 7),
                                 (4, 0), (4, 7), (5, 0), (5, 7), (7, 2), (7, 3), (7, 4), (7, 5)],
                             8: [(2, 3), (2, 4), (3, 2), (4, 2), (5, 3), (5, 4), (4, 5), (4, 3)],
                             7: [(2, 2), (2, 5), (5, 2), (5, 5)],
                             6: [(3, 1), (4, 1), (6, 3), (6, 4), (4, 6), (3, 6), (1, 3), (1, 4)],
                             5: [(1, 2), (1, 5), (2, 1), (2, 6), (5, 1), (5, 6), (6, 2), (6, 5)],
                             4: [(0, 1), (1, 0), (1, 1), (0, 6), (1, 6), (1, 7), (6, 0), (6, 1), (7, 1), (6, 6), (6, 7),
                                 (7, 6)]}
 
    def move(self, board):
        positions = []  # first positions in a board
        for new_r in range(len(board)):
            for new_c in range(len(board[new_r])):
                if board[new_r][new_c] == self.my_color:
                    positions.append((new_r, new_c))
 
        all_moves = []  # all our available found moves
        for j in positions:
            possible_moves = self.find_move(board, j[0], j[1])
            if possible_moves != []:
                all_moves.append(possible_moves)
 
        find_best_move = {10: [], 9: [], 8: [], 7: [], 6: [], 5: [], 4: []}
 
        for i in range(len(all_moves)):  # we determine the most advantageous possible position
            for j in range(len(all_moves[i])):
                for k in range(10, 3, -1):  # go through the whole graded board
                    if all_moves[i][j] in self.rating_board[k]:
                        find_best_move[k].append(all_moves[i][j])
 
        for k in range(10, 3, -1):  # we determine in which position we can turn the maximum number of stones
            if find_best_move[k] != []:
                i_max = 0
                max = 0
                for i in range(len(find_best_move[k])):
                    if self.dict_of_stones[find_best_move[k][i]] > max:
                        max = self.dict_of_stones[find_best_move[k][i]]
                        i_max = i
                return find_best_move[k][i_max]  # make the most profitable move
 
            if len(find_best_move) == 0:  # if don't have moves
                return None
 
    def find_move(self, board, r, c):
        """
        looking for moves all over the board and at the same time looking for the maximum number of stones that we
        can turn
        """
        possible_moves = []  # We write down all possible moves, but not all can be profitable
        start_r = r
        start_c = c
        stones = 0  # the number of stones that we can turn
 
        # cell up
        while r - 1 >= 0:
            if board[start_r - 1][start_c] != self.opponent_color:
                break
            if board[r - 1][c] == -1:
                possible_moves.append((r - 1, c))
                self.dict_of_stones[(r - 1, c)] = stones
                break
            elif board[r - 1][c] == self.my_color:
                break
            else:
                r -= 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell up-right
        stones = 0
        while r - 1 >= 0 and c + 1 <= 7:
            if board[start_r - 1][start_c + 1] != self.opponent_color:
                break
            if board[r - 1][c + 1] == -1:
                possible_moves.append((r - 1, c + 1))
                self.dict_of_stones[(r - 1, c + 1)] = stones
                break
            elif board[r - 1][c + 1] == self.my_color:
                break
            else:
                r -= 1
                c += 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell right
        stones = 0
        while c + 1 <= 7:
            if board[start_r][start_c + 1] != self.opponent_color:
                break
            if board[r][c + 1] == -1:
                possible_moves.append((r, c + 1))
                self.dict_of_stones[(r, c + 1)] = stones
                break
            elif board[r][c + 1] == self.my_color:
                break
            else:
                c += 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell right-down
        stones = 0
        while r + 1 <= 7 and c + 1 <= 7:
            if board[start_r + 1][start_c + 1] != self.opponent_color:
                break
            if board[r + 1][c + 1] == -1:
                possible_moves.append((r + 1, c + 1))
                self.dict_of_stones[(r + 1, c + 1)] = stones
                break
            elif board[r + 1][c + 1] == self.my_color:
                break
            else:
                r += 1
                c += 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell down
        stones = 0
        while r + 1 <= 7:
            if board[start_r + 1][start_c] != self.opponent_color:
                break
            if board[r + 1][c] == -1:
                possible_moves.append((r + 1, c))
                self.dict_of_stones[(r + 1, c)] = stones
                break
            elif board[r + 1][c] == self.my_color:
                break
            else:
                r += 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell left-down
        stones = 0
        while r + 1 <= 7 and c - 1 >= 0:
            if board[start_r + 1][start_c - 1] != self.opponent_color:
                break
            if board[r + 1][c - 1] == -1:
                possible_moves.append((r + 1, c - 1))
                self.dict_of_stones[(r + 1, c - 1)] = stones
                break
            elif board[r + 1][c - 1] == self.my_color:
                break
            else:
                r += 1
                c -= 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell left
        stones = 0
        while c - 1 >= 0:
            if board[start_r][start_c - 1] != self.opponent_color:
                break
            if board[r][c - 1] == -1:
                possible_moves.append((r, c - 1))
                self.dict_of_stones[(r, c - 1)] = stones
                break
            elif board[r][c - 1] == self.my_color:
                break
            else:
                c -= 1
                stones += 1
        r = start_r
        c = start_c
 
        # cell left-up
        stones = 0
        while r - 1 >= 0 and c - 1 >= 0:
            if board[start_r - 1][start_c - 1] != self.opponent_color:
                break
            if board[r - 1][c - 1] == -1:
                possible_moves.append((r - 1, c - 1))
                self.dict_of_stones[(r - 1, c - 1)] = stones
                break
            elif board[r - 1][c - 1] == self.my_color:
                break
            else:
                r -= 1
                c -= 1
                stones += 1
        r = start_r
        c = start_c
 
        return possible_moves
