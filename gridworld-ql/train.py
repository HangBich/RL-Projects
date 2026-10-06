from environment import GridWorld
from agent import QLearningAgent

import matplotlib.pyplot as plt
import numpy as np


n_episodes = 1000

env = GridWorld()
agent = QLearningAgent()
rewards = []

for episode in range(n_episodes):
    state = env.reset()
    done = False 
    steps = 0
    r = 0
    while not done and steps < 100: 
        action = agent.select_action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state, done)
        state = next_state
        steps += 1 
        r += reward
    rewards.append(r)


window = 50 
ma = np.convolve(rewards, np.ones(window)/window, mode="valid")
plt.figure(figsize=(8,4))
plt.plot(rewards, alpha=0.3, label="Reward mỗi episode")
plt.plot(range(window-1, len(rewards)), ma, label=f"Trung bình trượt {window}")
plt.xlabel("Episode"); plt.ylabel("Reward"); plt.legend(); plt.tight_layout()
plt.savefig("learning_curve.png", dpi=120)
