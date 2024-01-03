#!/usr/bin/env python3
'''task 3'''
import numpy as np
import gym as gym


def epsilon_greedy(Q, state, epsilon):
    '''epsilon greedy'''
    num_actions = Q.shape[1]

    if np.random.uniform() < epsilon:
        # explore and choose a random action
        action = np.random.randint(num_actions)
    else:
        # exploit and choose the action with the highest Q-value for
        # the current state
        action = np.argmax(Q[state, :])

    return action
