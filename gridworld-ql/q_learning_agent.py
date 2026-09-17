import random

class QLearningAgent:
    def __init__(self, state_space, action_space, learning_rate=0.1, discount=0.99, epsilon=0.1):
        self.state_space = state_space
        self.action_space = action_space
        self.learning_rate = learning_rate 
        self.discount = discount
        self.epsilon = epsilon

        self.initialize_q_table()
        

    def initialize_q_table(self):
        self.Q_table = {}
        for state in self.state_space:
            self.Q_table[state] = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0}

    def choose_action(self, state):
        if random.random() < self.epsilon:
            # Explore: random action
            return random.choice(self.action_space)
        else:
            # Exploit: best action 
            max_action = 0
            max_q_value = self.Q_table[state][0] 
            for action in self.action_space:
                if self.Q_table[state][action] > max_q_value: 
                    max_q_value = self.Q_table[state][action]
                    max_action = action
            return max_action

    def update_q(self, state, action, reward, next_state, done):
        if done: 
            max_next_q = 0 
        else:
            max_next_q = max(self.Q_table[next_state].values())
        self.Q_table[state][action] += self.learning_rate*(reward + self.discount*max_next_q-self.Q_table[state][action])

    def extract_policy(self):
        self.policy = {
            state: max(self.Q_table[state], key=lambda a: self.Q_table[state][a])
            for state in self.Q_table
        }
        return self.policy 
