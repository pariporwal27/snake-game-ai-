import torch 
print("Torch imported")
import matplotlib.pyplot as plt
from snake_game import SnakeGame
from agent import Agent


def plot(scores, mean_scores):
    plt.clf()
    plt.title("Snake AI Training")
    
    plt.plot(scores, label="Score")
    plt.plot(mean_scores, label="Mean Score")
    plt.legend()
    plt.pause(0.1)

def train():
    scores = []
    mean_scores = []
    total_score = 0
    best_score = 0

    agent = Agent()
    game = SnakeGame()
    plt.ion()  

    while True:
        state = agent.get_state(game)
        action = agent.get_action(state)
        reward, done, score = game.play_step(action)
        next_state = agent.get_state(game)

        agent.train_short_memory(state, action, reward, next_state, done)
        agent.remember(state, action, reward, next_state, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > best_score:
                best_score = score
                agent.model.save()

            print(f"Game: {agent.n_games} | Score: {score} | Best: {best_score}")

            scores.append(score)
            total_score += score
            mean_scores.append(total_score / agent.n_games)
            plot(scores, mean_scores)

if __name__ == "__main__":
    train()
