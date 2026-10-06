# Q-Learning on GridWorld

Tabular Q-learning implemented from scratch (no RL libraries).

## Environment

| | |
|---|---|
| Grid | 4×4 |
| Start | [0,0] |
| Goal | [3,3] |
| Step reward | -1 |
| Wall collision | -10 |
| Goal reward | 10 |
| Actions | 0=up, 1=down, 2=right, 3=left |

## Algorithm

- Q-table shape: (4,4,4)
- Policy: epsilon-greedy
- Update rule: Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') − Q(s,a)]
- Hyperparameters: α = 0.1, γ = 0.9, ε = 0.1

## Usage

```bash
pip install -r requirements.txt
python train.py
pytest test_environment.py
```

## Results

![learning curve](learning_curve.png)
- Converges after 20-30 episodes
- Reward stabilizes at +4 (6 steps x -1, plus +10 at goal)
- The large negative spike in early episodes (< -120) comes from
  zero-initialized Q-table: argmax always returns action 0, so the agent
  repeatedly hits the top wall. A 100-step cap prevents infinite episodes.
- The scattered spikes throughout training are caused by the fixed
  epsilon = 0.1: the agent keeps exploring after it has already learned
  the optimal path. Epsilon decay would remove these (not implemented yet).
