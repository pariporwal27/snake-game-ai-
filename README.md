#  Snake Game AI – Reinforcement Learning Project

##  Project Overview

Artificial Intelligence Snake Game using Reinforcement Learning (Deep Q-Learning) The AI agent interacts with the environment and improves its performance over time by learning from past game experience.



##  Problem Statement

In many real-world scenarios, agents must learn optimal decisions through experience rather than predefined rules. This project demonstrates how an AI agent can learn to play the Snake game without being explicitly programmed with strategies.

##  Solution Approach

The solution employs the following:

* Deep Q-Learning (DQN)
* Neural network for predicting the best action
* Experience replay (memory)
* Reward-based feedback system

The agent learns through:

1. Observation of the current state
2. Execution of an action
3. Receiving a reward or penalty
4. Update of knowledge over time
5. Utilization of the knowledge for the game


##  Technologies Used

* Python
* PyTorch
* Pygame
* NumPy
* Matplotlib



##  Features

*  Fully autonomous Snake AI
*  Real-time training graph (score vs games)
*  Model saving on best score
*  Efficient training using past memory



##  Project Structure

snake-ai<br>
│── train.py       
│── agent.py      
│── model.py      
│── snake_game.py   
│── README.md

##  How to Run

### 1. Install Libraries

pip install pygame torch numpy matplotlib

### 2. Run 

python train.py

##  Results

* The AI starts with random moves
* Learns progressively through rewards
* improves with more training
* Best score increases over time

## Output screenshot
<br>
<img width="651" height="526" alt="Screenshot 2026-03-27 005940" src="https://github.com/user-attachments/assets/ba39eae7-96a0-4b7f-b735-36e67acf7d4f" />
<br>
<img width="800" height="686" alt="Screenshot 2026-03-24 192656" src="https://github.com/user-attachments/assets/6de16bbf-05f7-43f9-82ce-da4d049e2ecc" />


##  Challenges Faced

* Balancing exploration and exploitation
* Debugging the game loop and collisions
* Ensuring stability in the training process
* Integrating the AI with the game environment

##  Learnings

* Practical knowledge of Reinforcement Learning
* Implementation of Deep Q-Networks
* Working with PyTorch-based models
* Real-time training and visualization


##  Future Improvements

* Improve reward system for faster learning
* Enhance model architecture
* Add model loading for inference
* Optimize training performance


##  Conclusion

The project has shown the capability of an AI agent to learn intelligent behavior through trial and error by using reinforcement learning.


