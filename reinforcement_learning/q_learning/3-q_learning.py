#!/usr/bin/env python3
'''task 4'''
import gym
import numpy as np


def train(env, Q, episodes=5000,
          max_steps=100, alpha=0.1,
          gamma=0.99, epsilon=1,
          min_epsilon=0.1,
          epsilon_decay=0.05):
    '''q learning model'''
    total_rewards = []

    for _ in range(episodes):
        state, _  = env.reset()
        episode_reward = 0

        for step in range(max_steps):
           if np.random.rand() < epsilon:
                action = env.action_space.sample()
           else:
                action = np.argmax(Q[state, :])
           next_state, reward, done, _, _ = env.step(action)

            # next value using the Q-learning update rule
           Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]))

           #  cumulative episode reward
           episode_reward += reward

           #  next state
           state = next_state

            # see if done
           if done:
            break

        #exploration-exploitation trade-off
        epsilon = max(min_epsilon, epsilon - epsilon_decay)

        total_rewards.append(episode_reward)

    return Q, total_rewards


def epsilon_greedy(Q, state, epsilon):
    '''epsilon greedy'''
    num_actions = Q.shape[1]

    if np.random.uniform() < epsilon:
        # choose  random action
        action = np.random.randint(num_actions)
    else:
        # exploit and choose the action with the highestvalue
        action = np.argmax(Q[state, :])

    return action

