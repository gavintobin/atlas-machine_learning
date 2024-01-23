#!/usr/bin/env python3
'''task 1'''

import numpy as np

def policy(matrix, weight):
    '''computes policy'''
    exp_values = np.exp(weight * matrix.T)
    policy = exp_values / np.sum(exp_values, axis=1, keepdims=True)

    return policy

def policy_gradient(state, weight):
    '''comppute mc ppolicy gradient'''
    probabilities = policy(state, weight)
    action = np.random.choice(len(probabilities[0]), p=probabilities[0])
    gradient = state.T - np.sum(probabilities * state.T, axis=1, keepdims=True)

    return action, gradient


if __name__ == "__main__":
    import gym
    import numpy as np
    #from policy_gradient import policy_gradient

    env = gym.make('CartPole-v1')
    np.random.seed(1)

    weight = np.random.rand(4, 2)

    print(weight)
    print(state)
    state = env.reset()[None,:]
    action, grad = policy_gradient(state, weight)
    print(action)
    print(grad)

    env.close()


