import pytest
from environment import GridWorld

class TestGridWorld:
    
    @pytest.fixture
    def env(self):
        """Khởi tạo environment mới cho mỗi test"""
        return GridWorld()
    
    # ✅ TEST RESET
    def test_reset(self, env):
        """Test reset đưa agent về start position"""
        state = env.reset()
        assert state == (0, 0), "Reset should return start position (0, 0)"
        assert env.current_pos == (0, 0), "Current position should be (0, 0)"
    
    # ✅ TEST NORMAL MOVEMENT
    def test_move_right(self, env):
        """Test di chuyển sang phải (action=3)"""
        env.reset()
        next_state, reward, done = env.step(3)  # RIGHT
        assert next_state == (1, 0), "Moving RIGHT from (0,0) should be (1,0)"
        assert reward == -1, "Normal movement should have reward -1"
        assert done == False, "Should not be done after one step"
    
    def test_move_left(self, env):
        """Test di chuyển sang trái vào tường"""
        env.reset()
        env.current_pos = (2, 2)  # ✅ Agent ở (2,2)
        next_state, reward, done = env.step(2)  # LEFT → (1,2) [WALL!]
        assert next_state == (2, 2), "Should stay at (2,2) when wall at (1,2)"
        assert reward == -1
        assert done == False
    
    def test_move_up(self, env):
        """Test di chuyển lên vượt biên"""
        env.reset()
        next_state, reward, done = env.step(0)  # UP → (0,-1) [INVALID]
        assert env.current_pos == (0, 0), "Should stay at (0,0) when trying to move UP"
        assert reward == -1
        assert done == False
    
    def test_move_down(self, env):
        """Test di chuyển xuống (action=1)"""
        env.reset()
        next_state, reward, done = env.step(1)  # DOWN
        assert next_state == (0, 1), "Moving DOWN from (0,0) should be (0,1)"
        assert reward == -1
        assert done == False
    
    # ✅ TEST BOUNDARY (Vượt biên)
    def test_boundary_up_left(self, env):
        """Test không thể vượt biên trên-trái"""
        env.reset()
        # Cố gắng đi UP từ (0,0)
        next_state, reward, done = env.step(0)  # UP → (0,-1)
        assert env.current_pos == (0, 0), "Should stay at (0,0) when trying to move UP"
        assert reward == -1
        assert done == False
    
    def test_boundary_right(self, env):
        """Test không thể vượt biên phải"""
        env.reset()
        env.current_pos = (3, 0)
        # Cố gắng đi RIGHT từ (3,0)
        next_state, reward, done = env.step(3)  # RIGHT → (4,0)
        assert env.current_pos == (3, 0), "Should stay at (3,0) when trying to move RIGHT"
        assert reward == -1
        assert done == False
    
    def test_boundary_down(self, env):
        """Test không thể vượt biên dưới"""
        env.reset()
        env.current_pos = (0, 3)
        # Cố gắng đi DOWN từ (0,3)
        next_state, reward, done = env.step(1)  # DOWN → (0,4)
        assert env.current_pos == (0, 3), "Should stay at (0,3) when trying to move DOWN"
        assert reward == -1
        assert done == False
    
    # ✅ TEST WALL (Tường)
    def test_wall_collision(self, env):
        """Test không thể đi vào tường tại (1,2)"""
        env.reset()
        env.current_pos = (1, 1)
        # Cố gắng đi DOWN vào tường tại (1,2)
        next_state, reward, done = env.step(1)  # DOWN
        assert env.current_pos == (1, 1), "Should stay at (1,1) when wall at (1,2)"
        assert reward == -1
        assert done == False
    
    def test_wall_collision_from_side(self, env):
        """Test không thể vào tường từ phía bên"""
        env.reset()
        env.current_pos = (0, 2)
        # Cố gắng đi RIGHT vào tường tại (1,2)
        next_state, reward, done = env.step(3)  # RIGHT
        assert env.current_pos == (0, 2), "Should stay at (0,2) when wall at (1,2)"
        assert reward == -1
        assert done == False
    
    # ✅ TEST GOAL
    def test_reach_goal(self, env):
        """Test khi đạt goal"""
        env.reset()
        env.current_pos = (3, 2)
        # Di chuyển DOWN để đạt goal tại (3,3)
        next_state, reward, done = env.step(1)  # DOWN
        assert env.current_pos == (3, 3), "Should reach goal at (3,3)"
        assert reward == +10, "Reward should be +10 when reaching goal"
        assert done == True, "Done should be True when reaching goal"
    
    def test_already_at_goal(self, env):
        """Test khi đã ở tại goal"""
        env.reset()
        env.current_pos = (3, 3)
        # Thực hiện action bất kỳ (vẫn ở goal)
        next_state, reward, done = env.step(0)  # UP → (3,2)
        assert env.current_pos == (3, 2), "Should move away from goal"
        assert done == False
    
    # ✅ TEST IS_VALID_POSITION
    def test_is_valid_position_in_bounds(self, env):
        """Test vị trí hợp lệ trong biên"""
        assert env.is_valid_position((0, 0)) == True
        assert env.is_valid_position((2, 2)) == True
        assert env.is_valid_position((3, 3)) == True
    
    def test_is_valid_position_out_of_bounds_negative(self, env):
        """Test vị trí vượt biên âm"""
        assert env.is_valid_position((-1, 0)) == False
        assert env.is_valid_position((0, -1)) == False
        assert env.is_valid_position((-1, -1)) == False
    
    def test_is_valid_position_out_of_bounds_positive(self, env):
        """Test vị trí vượt biên dương"""
        assert env.is_valid_position((4, 0)) == False
        assert env.is_valid_position((0, 4)) == False
        assert env.is_valid_position((4, 4)) == False
    
    def test_is_valid_position_wall(self, env):
        """Test vị trí tường không hợp lệ"""
        assert env.is_valid_position((1, 2)) == False, "Wall position should be invalid"
    
    def test_is_valid_position_goal_is_valid(self, env):
        """Test goal position là hợp lệ (agent có thể vào)"""
        assert env.is_valid_position((3, 3)) == True, "Goal should be valid"
    
    # ✅ TEST SEQUENCE
    def test_path_to_goal(self, env):
        """Test đi từ start đến goal theo đường tối ưu"""
        env.reset()
        
        # Path: (0,0) → (1,0) → (2,0) → (3,0) → (3,1) → (3,2) → (3,3)
        actions = [3, 3, 3, 1, 1, 1]  # RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN
        
        for action in actions:
            next_state, reward, done = env.step(action)
            if done:
                break
            assert reward == -1, f"Non-goal step should have reward -1, got {reward}"
        
        assert env.current_pos == (3, 3), "Should reach goal"
        assert done == True
    
    # ✅ TEST EDGE CASES
    def test_multiple_resets(self, env):
        """Test reset nhiều lần"""
        for _ in range(5):
            state = env.reset()
            assert state == (0, 0)
            assert env.current_pos == (0, 0)
    
    def test_wall_position_correct(self, env):
        """Test tường ở đúng vị trí (1,2)"""
        assert env.wall_pos == (1, 2)
    
    def test_goal_position_correct(self, env):
        """Test goal ở đúng vị trí (3,3)"""
        assert env.goal_pos == (3, 3)
    
    def test_grid_size(self, env):
        """Test kích thước lưới là 4x4"""
        assert env.grid_size == 4
