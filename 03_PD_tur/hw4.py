COOPERATE = False
DEFECT = True
 
 
class MyPlayer:
    """Hrac bude hrat akuratni a bude zvysovat sve body, kdy bude vedet, ze dominuje"""
 
    def __init__(self, payoff_matrix, number_of_iterations=10):
        self.matrix = payoff_matrix
        self.mujlist = []
        self.protivniklist = []
        self.moves = 0
        self.Score = [0, 0]
 
    def control_matrix(self):  # if betraying is more profitable for us, then we better betray
        if self.matrix[0][0][0] <= self.matrix[1][1][0]:
            return True
        return False
 
    def move(self):
        self.moves += 1
        cop = 0
        if self.control_matrix() == True:
            # we betray another player, because it is profitable,if not profitable,
            # the condition will not work
            return DEFECT
        for i in range(0, len(self.mujlist)):  # control with who plays the player
            if self.mujlist[i] == self.protivniklist[i]:
                cop += 1
        if self.moves > 3:  # We check the one to play in the third moves
            if cop == self.moves - 1:
                return COOPERATE
 
        if self.moves > 1:
            distract = self.Score[0] - self.Score[1]  # difference between my score and the opponent's score
            risk = self.matrix[0][1][1] - self.matrix[0][1][0]
            # see how many points my player will lose in case: I trust I will be deceived
            if distract > risk:  # let's try to trust him
                return COOPERATE
            else:
                return DEFECT
        else:
            return DEFECT
 
    def record_last_moves(self, my_last_move, opponent_last_move):  # writing down the moves
        self.mujlist.append(my_last_move)
        self.protivniklist.append(opponent_last_move)
 
        for i in range(len(self.Score)):
            self.Score[i] += self.matrix[my_last_move][opponent_last_move][i]  # write down points
