#!/usr/bin/env python2
'''task2'''
import gym
import numpy as np

def q_init(env):
    '''q init'''
    states = env.observation_space.n
    actions = env.action_space.n

    # Initialize  with zeros
    q_table = np.zeros((states, actions))

    return q_table
