"""
Test QLearningAgent hoạt động đúng không
"""

import random
from environment import GridWorld
from q_learning_agent import QLearningAgent

print("=" * 60)
print("TEST QLearningAgent")
print("=" * 60)

# ===== TEST 1: Khởi tạo Agent =====
print("\n--- TEST 1: Khởi tạo Agent ---")
try:
    # Tạo state_space (tất cả tọa độ 4x4)
    state_space = [(x, y) for x in range(4) for y in range(4)]
    action_space = [0, 1, 2, 3]
    
    agent = QLearningAgent(
        state_space=state_space,
        action_space=action_space,
        learning_rate=0.1,
        discount=0.99,
        epsilon=0.1
    )
    
    print("✅ Agent khởi tạo thành công")
    print(f"   State space size: {len(agent.Q_table)}")
    print(f"   Q-table keys (first 3): {list(agent.Q_table.keys())[:3]}")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    exit(1)

# ===== TEST 2: Choose Action =====
print("\n--- TEST 2: Choose Action ---")
try:
    state = (0, 0)
    action = agent.choose_action(state)
    print(f"✅ Choose action từ {state}: {action}")
    print(f"   Action phải trong [0, 1, 2, 3]: {action in [0, 1, 2, 3]}")
    
    # Test nhiều lần (để thấy explore vs exploit)
    actions = [agent.choose_action(state) for _ in range(10)]
    print(f"   10 lần chọn action: {actions}")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    exit(1)

# ===== TEST 3: Update Q =====
print("\n--- TEST 3: Update Q ---")
try:
    state = (0, 0)
    action = 3
    reward = -1
    next_state = (0, 1)
    done = False
    
    q_before = agent.Q_table[state][action]
    print(f"   Q-value trước update: {q_before}")
    
    agent.update_q(state, action, reward, next_state, done)
    
    q_after = agent.Q_table[state][action]
    print(f"   Q-value sau update: {q_after}")
    print(f"✅ Update Q thành công (Q-value thay đổi: {q_after != q_before})")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    exit(1)

# ===== TEST 4: Update Q with Done =====
print("\n--- TEST 4: Update Q (Done=True) ---")
try:
    state = (3, 2)
    action = 1
    reward = +10
    next_state = (3, 3)
    done = True
    
    q_before = agent.Q_table[state][action]
    print(f"   Q-value trước: {q_before}")
    
    agent.update_q(state, action, reward, next_state, done)
    
    q_after = agent.Q_table[state][action]
    print(f"   Q-value sau: {q_after}")
    print(f"✅ Update Q (done) thành công")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    exit(1)

# ===== TEST 5: Extract Policy =====
print("\n--- TEST 5: Extract Policy ---")
try:
    policy = agent.extract_policy()
    print(f"✅ Extract policy thành công")
    print(f"   Policy size: {len(policy)}")
    print(f"   Policy (first 5 states):")
    for state in list(policy.keys())[:5]:
        print(f"     State {state}: action {policy[state]}")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    exit(1)