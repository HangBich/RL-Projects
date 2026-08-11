# RL-From-Scratch: GridWorld + Robot Manipulation

**Status:** In Progress (Week X/4)  
**Target Completion:** 4 weeks  
**Destination:** Lab application to Prof. Huỳnh Thị Thanh Bình

---

## 📌 PROJECT PURPOSE

Learning Reinforcement Learning from fundamentals to prepare for joining **Huỳnh Thị Thanh Bình's lab** to work on **MOPDERL** (Multi-Objective Evolutionary Reinforcement Learning for robot control).

**Why these projects?**
- Demonstrate understanding of core RL algorithms (not just library usage)
- Show progression: tabular RL → deep RL → robotics
- Build portfolio for research lab application
- Foundation for multi-objective RL research

---

## 🎯 PROJECT 1: GridWorld Q-Learning (Week 1)

### PURPOSE
Learn tabular Q-Learning on simple 4×4 grid environment. Foundation for understanding MDPs, Bellman equation, and value-based RL.

### CHECKLIST - MUST COMPLETE:

#### Code Implementation
- [ ] `environment.py` - GridWorld environment
  - [ ] 4×4 grid with wall at (1,2)
  - [ ] State: (x, y) tuples
  - [ ] Actions: 0=UP, 1=DOWN, 2=LEFT, 3=RIGHT
  - [ ] Rewards: +10 goal, -1 else
  - [ ] Functions: `step()`, `reset()`
  
- [ ] `q_learning_agent.py` - QLearningAgent class
  - [ ] `initialize_q_table()` - Create Q(s,a) dictionary
  - [ ] `choose_action(state)` - ε-greedy selection
  - [ ] `update_q(s, a, r, s', done)` - Bellman update
  - [ ] `extract_policy()` - Greedy policy from Q-table
  
- [ ] `train.py` - Training loop
  - [ ] 500 episodes minimum
  - [ ] ε-greedy exploration (ε=0.1)
  - [ ] Track total reward per episode
  - [ ] Decay ε over time (optional)
  
- [ ] `test.py` - Evaluation
  - [ ] Test learned policy (greedy, no exploration)
  - [ ] Print optimal path (sequence of states)
  - [ ] Show steps to goal (should be ~6)
  - [ ] Compare random vs learned policy
  
- [ ] `utils.py` - Helpers
  - [ ] Plot learning curve (rewards over episodes)
  - [ ] Plot grid with optimal policy arrows
  - [ ] Pretty print results

#### Code Quality
- [ ] No external RL frameworks used (no stable-baselines, gym wrapper)
- [ ] NumPy allowed (not PyTorch)
- [ ] Clear comments explaining algorithm
- [ ] Functions have docstrings
- [ ] Code is readable and modular

#### Results & Visualization
- [ ] Learning curve shows improvement over 500 episodes
- [ ] Episode 1: random agent, ~-160 reward
- [ ] Episode 500: learned agent, ~+8 reward
- [ ] Optimal path visualization (grid with arrows)
- [ ] Save plots as PNG in `/results/`

#### Documentation
- [ ] `README.md` explaining:
  - What Q-Learning is
  - How the environment works
  - Results achieved
  - How to run the code
- [ ] Comments in code explaining Bellman equation
- [ ] Example run output showing learning

#### GitHub
- [ ] Push to GitHub: `gridworld-q-learning/` folder
- [ ] All files included (code + results + README)
- [ ] Clean git history (meaningful commits)

---

## 🤖 PROJECT 2: PyBullet Robot Manipulation with DQN (Weeks 2-3)

### PURPOSE
Implement Deep Q-Learning (DQN) for continuous control. Shows understanding of:
- Neural networks for function approximation
- Experience replay
- Deep RL for robot arm control

### CHECKLIST - MUST COMPLETE:

#### Environment Setup
- [ ] `robot_env.py` - Robot environment (PyBullet)
  - [ ] Robot arm (3-5 DOF minimum)
  - [ ] Task: Reach target position OR Grasp object
  - [ ] State space: joint angles + target position (continuous, 4-7D)
  - [ ] Action space: joint torques (continuous, 3-5D)
  - [ ] Rewards: distance to target, efficiency bonus
  - [ ] Functions: `step()`, `reset()`, `render()`
  - [ ] Collision detection (if grasping)

#### Neural Network
- [ ] `neural_network.py` - Simple Q-network
  - [ ] Architecture: Input → Hidden(128) → Hidden(64) → Output
  - [ ] Activation: ReLU for hidden, linear for output
  - [ ] Forward pass: state → Q-values for actions
  - [ ] Backward pass: gradient descent (no PyTorch!)
  - [ ] Or: Use PyTorch for network only (allowed)

#### DQN Agent
- [ ] `dqn_agent.py` - DQNAgent class
  - [ ] Q-network (current) + Target network
  - [ ] Experience replay buffer (store transitions)
  - [ ] `choose_action()` - ε-greedy with Q-network
  - [ ] `store_experience()` - Save (s, a, r, s', done)
  - [ ] `sample_batch()` - Random mini-batch from replay
  - [ ] `update_network()` - Gradient descent on batch
  - [ ] Target network update (copy weights every N steps)

#### Training
- [ ] `train.py` - Training loop
  - [ ] 500-1000 episodes
  - [ ] ε-greedy exploration (start 1.0, decay to 0.1)
  - [ ] Experience replay (batch size 32-64)
  - [ ] Track rewards per episode
  - [ ] Loss tracking (MSE between Q and target)
  - [ ] Save checkpoint (best model)

#### Evaluation
- [ ] `test.py` - Test learned policy
  - [ ] Test 50+ episodes (greedy, no exploration)
  - [ ] Average reward
  - [ ] Success rate (if task binary)
  - [ ] Compare vs random policy (random should be terrible)
  
#### Visualization
- [ ] `visualize.py` - Generate plots
  - [ ] Learning curve (rewards over episodes)
  - [ ] Loss curve (MSE over training)
  - [ ] Success rate over episodes
  - [ ] Save video/GIF of agent solving task
  - [ ] Save plots to `/results/`

#### Code Quality
- [ ] No external RL frameworks (stable-baselines forbidden)
- [ ] PyBullet only for physics
- [ ] Network can use PyTorch OR numpy (numpy cooler but harder)
- [ ] Clear comments, docstrings
- [ ] Modular design

#### Results
- [ ] Random policy: ~0% success or negative reward
- [ ] Learned policy (end): >50% success OR positive reward
- [ ] Learning curve shows improvement
- [ ] Video showing final agent behavior

#### Documentation
- [ ] `README.md` explaining:
  - DQN algorithm overview
  - Robot task (reaching/grasping)
  - Architecture (network, replay buffer)
  - Results achieved
  - How to run
  - Hyperparameters used
- [ ] Algorithm explanation (Bellman, target network, replay)
- [ ] Comparison: Random vs Learned

#### GitHub
- [ ] Push to GitHub: `robot-dqn/` folder
- [ ] All code + results + README
- [ ] Clean structure
- [ ] Video/GIF of final performance

---

## 📊 OVERALL PORTFOLIO CHECKLIST

### Before Sending Email:

#### Code Quality
- [ ] Both projects have NO external RL libraries (only PyBullet/PyTorch)
- [ ] All code is your own (no copy-paste)
- [ ] Algorithms implemented from scratch (understand every line)
- [ ] Code runs without errors
- [ ] All imports work (requirements.txt filled)

#### GitHub
- [ ] Repo: `RL-From-Scratch/` or `RL-Robot-Learning/`
- [ ] Structure: