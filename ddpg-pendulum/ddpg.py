import torch
import numpy as np
import torch.nn.functional as F 
import torch.optim as optim


from networks import Actor, Critic

class DDPG:
    def __init__(self, state_dim, action_dim, max_action, gamma=0.99, tau=0.005):
        self.actor = Actor(state_dim, action_dim, max_action)
        self.critic = Critic(state_dim, action_dim)
        self.gamma = gamma 
        self.tau = tau 
        self.max_action = max_action

        self.actor_target = Actor(state_dim, action_dim, max_action)   
        self.critic_target = Critic(state_dim, action_dim)

        self.actor_target.load_state_dict(self.actor.state_dict())
        self.critic_target.load_state_dict(self.critic.state_dict())

        self.actor_opt = torch.optim.Adam(self.actor.parameters(), lr=1e-4)
        self.critic_opt = torch.optim.Adam(self.critic.parameters(), lr=1e-3)
    
    def select_action(self, state):
        state = torch.FloatTensor(state).reshape(1, -1)
        action = self.actor(state).detach().numpy().flatten()
        return  action


    def soft_update(self, net, target_net):
        for param, target_param in zip(net.parameters(), target_net.parameters()):
            target_param.data.copy_(self.tau*param.data + (1-self.tau)*target_param.data)

    def update(self, buffer, batch_size):
        state, action, reward, next_state, done = buffer.sample(batch_size)
         
        with torch .no_grad():
            next_action = self.actor_target(next_state)
            next_Q = self.critic_target(next_state, next_action)
            target =  reward + self.gamma * next_Q *(1-done)

        current_Q = self.critic(state, action)
        loss = F.mse_loss(current_Q, target)

        self.critic_opt.zero_grad()
        loss.backward()
        self.critic_opt.step()

        actor_loss = -self.critic(state, self.actor(state)).mean()

        self.actor_opt.zero_grad()
        actor_loss.backward()
        self.actor_opt.step()

        self.soft_update(self.actor, self.actor_target)
        self.soft_update(self.critic, self.critic_target)