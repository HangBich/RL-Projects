import gymnasium as gym
from ddpg import DDPG
import torch

env = gym.make("Pendulum-v1", render_mode="human")
state, _ = env.reset()
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
max_action = float(env.action_space.high[0])

agent = DDPG(state_dim, action_dim, max_action)
agent.actor.load_state_dict(torch.load("actor.pth"))
agent.actor.eval()


for episode in range(5):
    state, _ = env.reset()
    episode_reward = 0
    terminated = truncated = False
    while not (terminated or truncated):
        action = agent.select_action(state)
        state, reward, terminated, truncated, _ = env.step(action)
        episode_reward += reward
    print(episode_reward)

env.close()