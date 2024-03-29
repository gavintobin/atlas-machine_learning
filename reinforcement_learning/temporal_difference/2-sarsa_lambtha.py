#!/usr/bin/env python3
'''task 3'''
import gym
import numpy as np


def sarsa_lambtha(env,
                  Q,
                  lambtha,
                  episodes=5000,
                  max_steps=100,
                  alpha=0.1,
                  gamma=0.99,
                  epsilon=1,
                  min_epsilon=0.1,
                  epsilon_decay=0.05):
    '''performs SAQRSA'''
    for episode in range(episodes):
        state, _ = env.reset()
        action = epsilon_greedy(Q, state, epsilon)
        eligibility_trace = np.zeros_like(Q)

        for step in range(max_steps):
            next_state, reward, done, _, _ = env.step(action)
            next_action = epsilon_greedy(Q, next_state, epsilon)

            delta = reward + gamma * Q[next_state, next_action] - Q[state, action]
            eligibility_trace[state, action] += 1

            for s in range(Q.shape[0]):
                for a in range(Q.shape[1]):
                    Q[s, a] = Q[s, a] + alpha * delta * eligibility_trace[s, a]
                    eligibility_trace[s, a] *= gamma * lambtha

            state, action = next_state, next_action

            if done:
                break

        epsilon = max(min_epsilon, epsilon - epsilon_decay)

    return Q

def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(Q.shape[1])
    else:
        return np.argmax(Q[state, :])

