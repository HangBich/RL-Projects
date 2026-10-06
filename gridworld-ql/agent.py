import numpy as np 


class QLearningAgent: 
    def __init__(self, row=4, col=4, num_action=4, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.row = row 
        self.col = col 
        self.num_action = num_action
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon 
        self.Q_table = np.zeros((self.row, self.col, self.num_action))

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return  np.random.randint(0, self.num_action)
        return np.argmax(self.Q_table[state[0], state[1]])

    def update(self, state, action, reward, next_state, done):
        current_q = self.Q_table[state[0], state[1]][action]
        best_next_q = np.max(self.Q_table[next_state[0], next_state[1]])
        target = reward + self.gamma*best_next_q*(1-done)
        self.Q_table[state[0], state[1]][action] += self.alpha*(target-current_q)
