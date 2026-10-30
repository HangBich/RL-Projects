import numpy as np 
import torch

class Buffer:
    def __init__(self, state_dim, action_dim, max_size):
        self.ptr = 0
        self.size = 0
        self.state = np.zeros((max_size, state_dim))
        self.action = np.zeros((max_size, action_dim))
        self.reward = np.zeros((max_size, 1))
        self.next_state = np.zeros((max_size, state_dim))
        self.done = np.zeros((max_size, 1))
        self. state_dim = state_dim
        self.action_dim = action_dim
        self.max_size = max_size

    def add(self, state, action, reward, next_state, done):
        self.state[self.ptr] = state 
        self.action[self.ptr] = action 
        self.reward[self.ptr] = reward
        self.next_state[self.ptr] = next_state
        self.done[self.ptr] = done 
        self.ptr = (self.ptr+1) % self.max_size 
        self.size = min(self.size+1, self.max_size)

    def sample(self, batch_size):
        ind = np.random.randint(0, self.size, batch_size)
        return (
            torch.FloatTensor(self.state[ind]),
            torch.FloatTensor(self.action[ind]),
            torch.FloatTensor(self.reward[ind]),
            torch.FloatTensor(self.next_state[ind]),
            torch.FloatTensor(self.done[ind]),
            )

if __name__ == "__main__":
    buf = Buffer(state_dim=3, action_dim=1, max_size=50)
    for i in range(100):
        buf.add([i, i, i], [i], i, [i+1, i+1, i+1], 0)
    print(buf.size, buf.ptr)          # kỳ vọng: 50 0
    s, a, r, ns, d = buf.sample(32)
    print(s.shape, a.shape, r.shape)  # kỳ vọng: [32,3] [32,1] [32,1]