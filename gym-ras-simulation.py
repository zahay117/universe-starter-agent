import gym
import time

env = gym.make("SpaceInvaders-v0")
env.reset()
env.render()
game_over = False
while not game_over:
        action = env.action_space.sample()
        game_over = env.step(action)[2]
        time.sleep(0.1)
        env.render()
