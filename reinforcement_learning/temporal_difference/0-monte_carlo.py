#!/usr/bin/env python3
'''task 1'''
import numpy as np
import gym


def monte_carlo(env, V,
                policy,
                episodes=5000,
                max_steps=100,
                alpha=0.1, gamma=0.99):
    '''performs mc algo'''
    for _ in range(episodes):
        state, _ = env.reset()
        episode = []
        for _ in range(max_steps):
            action = policy(state)
            next_state, reward, done, _, _ = env.step(action)
            episode.append((state, action, reward))
            state = next_state
            if done:
                break

        G = 0
        for i in range(len(episode)-1, -1, -1):
            state, action, reward = episode[i]
            G = gamma * G + reward
            V[state] = V[state] + alpha * (G - V[state])

    return V
