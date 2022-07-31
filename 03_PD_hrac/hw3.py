class MyPlayer:
    """Hrac bude hrat jako oko za oko, zub za zub"""
 
    def __init__(self, payoff_matrix, number_of_iterations=10):
        self.matrice = payoff_matrix
        self.num = number_of_iterations
        self.mujlist = [True]
        self.protivniklist = [True]
 
    def move(self):
        return self.protivniklist[len(self.protivniklist) - 1]  # Hrac kopiruje pohyb protivnika
 
    def record_last_moves(self, my_last_move, opponent_last_move):  # zapis chodu
        self.mujlist.append(my_last_move)
        self.protivniklist.append(opponent_last_move)
