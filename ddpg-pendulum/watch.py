import gymnasium as gym

env = gym.make("Pendulum-v1", render_mode="human")
state, _ = env.reset()

for _ in range(500):
    action = env.action_space.sample()   # hành động ngẫu nhiên
    state, reward, terminated, truncated, _ = env.step(action)
    if terminated or truncated:
        state, _ = env.reset()

env.close()