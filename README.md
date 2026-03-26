#  Snake Game AI – Reinforcement Learning Project

##  Project Overview

This project is a Snake Game powered by Artificial Intelligence using Reinforcement Learning (Deep Q-Learning). The AI agent learns to play the classic snake game by interacting with the environment and improving its performance over time by learning from past game experience.



##  Problem Statement

In many real-world scenarios, agents must learn optimal decisions through experience rather than predefined rules. This project demonstrates how an AI agent can learn to play the Snake game without being explicitly programmed with strategies.



##  Solution Approach

The solution uses:

* Deep Q-Learning (DQN) for decision making
* A neural network to predict best actions
* Experience replay (memory) for stable learning
* Reward-based feedback system

The agent learns by:

1. Observing the current state
2. Taking an action
3. Receiving a reward or penalty
4. Updating its knowledge over time
5. Using the knowledge for future game 


## 🛠️ Technologies Used

* **Python**
* **PyTorch**
* **Pygame**
* **NumPy**
* **Matplotlib**

---

## 🚀 Features

* 🤖 Fully autonomous Snake AI
* 📈 Real-time training graph (score vs games)
* 💾 Model saving on best performance
* ⚡ Efficient training using replay memory

---

## 📂 Project Structure

```
snake-ai/
│── train.py        # Training loop + plotting
│── agent.py        # AI agent logic
│── model.py        # Neural network (DQN)
│── snake_game.py   # Game environment
│── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install pygame torch numpy matplotlib
```

### 2. Run training

```
python train.py
```

---

## 📊 Training Details

* State Space: 11 features
* Actions: 3 (straight, right turn, left turn)
* Memory Size: 100,000
* Learning Rate: 0.001
* Discount Factor (Gamma): 0.9

---

## 📈 Results

* The AI starts with random moves
* Learns progressively through rewards
* Performance improves with more training
* Best score increases over time

---

## ⚠️ Challenges Faced

* Balancing exploration vs exploitation
* Debugging game loop and collisions
* Ensuring stable training
* Integrating AI with game environment

---

## 📚 Learnings

* Practical understanding of Reinforcement Learning
* Implementation of Deep Q-Networks
* Working with PyTorch models
* Handling real-time training and visualization

---

## 👤 Author

**Pari Porwal**

---

## 📌 Future Improvements

* Improve reward system for faster learning
* Enhance model architecture
* Add model loading for inference
* Optimize training performance

---

## ⭐ Conclusion

This project demonstrates how an AI agent can learn intelligent behavior through trial and error using reinforcement learning, without being explicitly programmed.

---
