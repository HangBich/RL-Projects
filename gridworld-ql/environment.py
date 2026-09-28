class GridWorld:
    def __init__(self):
        self.size = 4
        self.start = [0,0]
        self.goal = [3,3]
        self.current = [0,0]

    def reset(self):
        self.current = self.start.copy()
        return self.start.copy()

    def step(self, action):
        next_state = self.current.copy()
        reward = -1
        done = False
        # tính vị trí mới từ action
        MOVES = {0: (-1, 0), 1: (+1, 0), 2: (0, +1), 3: (0,-1)}
        next_state[0] += MOVES[action][0]
        next_state[1] += MOVES[action][1]
        
        # xử lý đụng tường
        if next_state[0]<0 or next_state[1]<0 or next_state[0]>self.size-1 or next_state[1]>self.size-1:
            next_state = self.current.copy()
            reward = -10
        # kiểm tra đã tới đích chưa
        if next_state == self.goal:
            reward += 10
            done = True 
        self.current = next_state
        return next_state, reward, done 


env = GridWorld()
env.reset()
env.step(1)
env.step(2)
s = env.reset()
s2, r, done = env.step(2)
# s2 phải là [0,1], không phải [1,2]
print(s2, r, done)