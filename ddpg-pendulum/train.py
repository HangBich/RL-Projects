import gymnasium as gym
import numpy as np 
import torch

from ddpg import DDPG
from buffer import Buffer

np.random.seed(42)
torch.manual_seed(42)

env = gym.make("Pendulum-v1")

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
max_action = float(env.action_space.high[0])

agent = DDPG(state_dim, action_dim, max_action)
buffer = Buffer(state_dim, action_dim, max_size=int(1e6))
rewards = []

for episode in range(500):
    state, _ = env.reset()
    episode_reward = 0 

    terminated = False
    truncated = False

    while not(terminated or truncated):
        action =  agent.select_action(state) + np.random.normal(0,0.1*max_action, size=action_dim)
        action = np.clip(action, -max_action, max_action)

        next_state, reward, terminated, truncated, _ = env.step(action)

        buffer.add(state, action, reward, next_state, float(terminated))
        state = next_state 
        episode_reward += reward 

        if buffer.size > 1000: 
            agent.update(buffer, 256)
    rewards.append(episode_reward)
    if episode % 10 == 0:
        print(episode_reward)
torch.save(agent.actor.state_dict(), "actor.pth")
env.close()


import matplotlib.pyplot as plt

window = 20
ma = np.convolve(rewards, np.ones(window)/window, mode="valid")
plt.figure(figsize=(8,4))
plt.plot(rewards, alpha=0.3, label="Reward mỗi episode")
plt.plot(range(window-1, len(rewards)), ma, label=f"Trung bình trượt {window}")
plt.xlabel("Episode"); plt.ylabel("Reward"); plt.legend(); plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("learning_curve.png", dpi=120)
plt.close()