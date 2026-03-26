import pygame
import random
import numpy as np

# Constants
BLOCK = 20
SPEED = 40
W, H = 640, 480

WHITE = (255, 255, 255)
RED   = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Snake AI")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = "RIGHT"
        self.head = [W//2, H//2]
        self.snake = [
            self.head[:],
            [self.head[0]-BLOCK, self.head[1]],
            [self.head[0]-2*BLOCK, self.head[1]]
        ]
        self.score = 0
        self.food = self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randrange(0, W, BLOCK)
        y = random.randrange(0, H, BLOCK)
        if [x, y] in self.snake:
            return self._place_food()
        return [x, y]

    def play_step(self, action):
        self.frame_iteration += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self._move(action)
        self.snake.insert(0, self.head[:])

        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        if self.head == self.food:
            self.score += 1
            reward = 10
            self.food = self._place_food()
        else:
            self.snake.pop()

        self._update_ui()
        self.clock.tick(SPEED)
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt[0] >= W or pt[0] < 0 or pt[1] >= H or pt[1] < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def _move(self, action):
        clock_wise = ["RIGHT", "DOWN", "LEFT", "UP"]
        idx = clock_wise.index(self.direction)

        if action == [1, 0, 0]:
            self.direction = clock_wise[idx]
        elif action == [0, 1, 0]:
            self.direction = clock_wise[(idx+1) % 4]
        else:
            self.direction = clock_wise[(idx-1) % 4]

        if self.direction == "RIGHT": self.head[0] += BLOCK
        elif self.direction == "LEFT": self.head[0] -= BLOCK
        elif self.direction == "DOWN": self.head[1] += BLOCK
        elif self.direction == "UP":   self.head[1] -= BLOCK

    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, GREEN,
                           pygame.Rect(pt[0], pt[1], BLOCK, BLOCK))
        pygame.draw.rect(self.display, RED,
                        pygame.Rect(self.food[0], self.food[1], BLOCK, BLOCK))
        font = pygame.font.SysFont("arial", 25)
        text = font.render(f"Score: {self.score}", True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()