import numpy as np
import random
from collections import deque
from model import LinearQNet, QTrainer
import torch

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0    
        self.gamma = 0.9  
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = LinearQNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game):
        head = game.head
        bl = [head[0]-20, head[1]]  
        br = [head[0]+20, head[1]]  
        bu = [head[0], head[1]-20]  
        bd = [head[0], head[1]+20]  

        dir_r = game.direction == "RIGHT"
        dir_l = game.direction == "LEFT"
        dir_u = game.direction == "UP"
        dir_d = game.direction == "DOWN"

        state = [
            (dir_r and game.is_collision(br)) or
            (dir_l and game.is_collision(bl)) or
            (dir_u and game.is_collision(bu)) or
            (dir_d and game.is_collision(bd)),

        
            (dir_u and game.is_collision(br)) or
            (dir_d and game.is_collision(bl)) or
            (dir_l and game.is_collision(bu)) or
            (dir_r and game.is_collision(bd)),

    
            (dir_d and game.is_collision(br)) or
            (dir_u and game.is_collision(bl)) or
            (dir_r and game.is_collision(bu)) or
            (dir_l and game.is_collision(bd)),

            
            dir_r, dir_l, dir_u, dir_d,

            
            game.food[0] < head[0],  
            game.food[0] > head[0],  
            game.food[1] < head[1],  # food up
            game.food[1] > head[1],  # food down
        ]
        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            sample = random.sample(self.memory, BATCH_SIZE)
        else:
            sample = self.memory
        states, actions, rewards, next_states, dones = zip(*sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # Explore vs exploit
        self.epsilon = 80 - self.n_games
        action = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
        else:
            state_t = torch.tensor(state, dtype=torch.float)
            pred = self.model(state_t)
            move = torch.argmax(pred).item()
        action[move] = 1
        return action