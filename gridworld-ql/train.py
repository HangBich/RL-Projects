from environment import GridWorld
from agent import QLearningAgent

import matplotlib.pyplot as plt
import numpy as np


def train(num_episodes=1000, use_decay=True):
    np.random.seed(42)
    env = GridWorld()
    agent = QLearningAgent()
    rewards = []

    for episode in range(num_episodes):
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
        if use_decay: 
            agent.update_epsilon()
    return rewards

def plot_rewards(rewards, ylabel):
    window = 50 
    ma = np.convolve(rewards, np.ones(window)/window, mode="valid")
    plt.figure(figsize=(8,4))
    plt.plot(rewards, alpha=0.3, label="Reward mỗi episode")
    plt.plot(range(window-1, len(rewards)), ma, label=f"Trung bình trượt {window}")
    plt.xlabel("Episode"); plt.ylabel(ylabel); plt.legend(); plt.tight_layout()
    plt.savefig(f"learning_curve_{ylabel}.png", dpi=120)
    plt.close()

def plot_comparison(r_fixed, r_decay, window=50, filename="comparison.png"):
    ma_fixed = np.convolve(r_fixed, np.ones(window)/window, mode="valid")
    ma_decay = np.convolve(r_decay, np.ones(window)/window, mode="valid")
    x = range(window-1, len(r_fixed))

    plt.figure(figsize=(8,4))
    plt.plot(x, ma_fixed, label="Epsilon cố định 0.1")
    plt.plot(x, ma_decay, label="Epsilon decay 0.995 -> 0.01")
    plt.xlabel("Episode")
    plt.ylabel("Reward (Trung bình trượt 50)")
    plt.ylim(-30, 10)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=120)
    plt.close()

if __name__ == "__main__":
    r_fixed = train(use_decay=False)
    r_decay = train(use_decay=True)
    plot_rewards(r_fixed, "reward_fixed")
    plot_rewards(r_decay, "reward_decay")
    plot_comparison(r_fixed, r_decay)
    print(f"Fixed: {np.mean(r_fixed[-100:]):.2f}")
    print(f"Decay: {np.mean(r_decay[-100:]):.2f}")

