#!/usr/bin/env python3
'''task 5'''
import numpy as np
import gym


def play(env, Q, max_steps=100):
    '''play time'''
    state, _ = env.reset()
    total_rewards = 0

    for step in range(max_steps):
        #  exploitation to chose action
        action = np.argmax(Q[state, :])

        # take action and observe the next state, reward, done, and info
        next_state, reward, done, _, _  = env.step(action)

        # display the current state of the board
        env.render()

        total_rewards += reward
        state = next_state

        if done:
            break

    return total_rewards
