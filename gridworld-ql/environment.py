class GridWorld: 
    def __init__(self, grid_size=4):
        self.grid_size = 4
        self.start_pos = (0, 0)
        self.goal_pos = (3, 3)
        self.wall_pos = (1, 2)
        self.current_pos = None 

    def reset(self):
        self.current_pos = self.start_pos 
        return self.current_pos

    def is_valid_position(self, pos):
        """Check vị trí hợp lệ (boundary + wall)"""
        if pos == self.wall_pos:
            return False
        if pos[0] < 0 or pos[0] >= self.grid_size or pos[1] < 0 or pos[1] >= self.grid_size:
            return False
        return True

    def step(self, action):
        """Thực hiện 1 action"""
        x, y = self.current_pos
        
        # 1. Tính next_pos dựa trên action 
        if action == 0:  # UP
            next_pos = (x, y - 1)
        elif action == 1:  # DOWN
            next_pos = (x, y + 1)
        elif action == 2:  # LEFT
            next_pos = (x - 1, y)
        elif action == 3:  # RIGHT
            next_pos = (x + 1, y)
        
        # 2. Check hợp lệ (boundary + wall)
        if self.is_valid_position(next_pos):
            self.current_pos = next_pos
        # else: stay tại (x, y)
        
        # 3. Tính reward + done
        if self.current_pos == self.goal_pos:
            reward = 10
            done = True
        else:
            reward = -1
            done = False

        return self.current_pos, reward, done
