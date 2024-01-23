#!/usr/bin/env python3
'''task 4'''
import numpy as np

def train(env, nb_episodes, alpha=0.000045, gamma=0.98):
    '''train usiing policy gradienton env'''
    weights = np.random.rand(env.observation_space.shape[0], env.action_space.n)
    scores = []

    for episode in range(nb_episodes):
        state = env.reset()[None, :]
        episode_score = 0

        while True:
            action, policy_grad = policy_gradient(state, weights)
            next_state, reward, done, _ = env.step(action)

            # update weights using policy gradient and the reward signal
            weights += alpha * policy_grad * reward

            episode_score += reward
            state = np.array(next_state)[None, :]

            if done:
                break

        scores.append(episode_score)

        # print current episode number and score on the same line
        print(f"Episode: {episode + 1}/{nb_episodes}, Score: {episode_score}", end="\r", flush=True)

    return scores

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
