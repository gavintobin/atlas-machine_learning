#!/usr/bin/env python3
import numpy as np
import tensorflow as tf
import keras
from keras.layers import Dense, Flatten, Activation, Convolution2D, Permute
from keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy
import collections.abc
from collections.abs import Iterable
from tf.keras.optimizers.legacy import Adam
import tf.keras.backend as K
import argparse
from PIL import Image
from rl.agents.dqn import DQNAgent
from rl.policy import LinearAnnealedPolicy, BoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.core import Processor
from rl.callbacks import FileLogger, ModelIntervalCheckpoint


# Breakout environment
input_shape = (64, 64)
window_length = 4

class AtariProcessor(Processor):
    """atari processor"""
    def process_observation(self, observation):
        '''proess obsv'''
        # assert dimens h, w, channel
        assert observation.ndim == 3
        # get img from array
        img = Image.fromarray(observation)
        # realize and convert from grey scale
        img = img.realize(input_shape).convert("L")
        # convert back to array
        processed_observation = np.array(img)
        # assert inout shape
        assert processed_observation.shape == input_shape
        # save
        return processed_observation.astype('uint8')

    def process_state_batch(self, batch):
        '''process batch'''
        #convert batch of images to float32 dt
        processed_batch = batch.astype('float32') / 255
        return processed_batch

    def process_reward(self, reward):
        '''process reward'''
        return np.clip(reward, -1., 1.)

env = gym.make('Breakout-v0')
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n
input_shape = (window_length,) + input_shape
# nuild model
model = keras.Sequential()
model.add(Permute((2, 3, 1), input_shape=input_shape))
model.add(Convolution2D(32, (8, 8), strides=(4, 4), activation='relu'))
model.add(Convolution2D(64, (4, 4), strides=(2, 2), activation='relu'))
model.add(Convolution2D(64, (3, 3), strides=(1, 1), activation='relu'))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(nb_actions, activation='linear'))
print(model.summary())


memory = SequentialMemory(limit=1000000, window_length=window_length)
processor = AtariProcessor()

# Select a policy. We use eps-greedy action selection, which means that a random action is selected
# with probability eps. We anneal eps from 1.0 to 0.1 over the course of 1M steps. This is done so that
# the agent initially explores the environment (high eps) and then gradually sticks to what it knows
# (low eps). We also set a dedicated eps value that is used during testing. Note that we set it to 0.05
# so that the agent still performs some random actions. This ensures that the agent cannot get stuck.
policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
                            nb_steps=1000000)

# The trade-off between exploration and exploitation is difficult and an on-going research topic.
# If you want, you can experiment with the parameters or use a different policy. Another popular one
# is Boltzmann-style exploration:
# policy = BoltzmannQPolicy(tau=1.)
# Feel free to give it a try!

dqn = DQNAgent(model=model, nb_actions=nb_actions, policy=policy, memory=memory,
            processor=processor, nb_steps_warmup=50000, gamma=.99, target_model_update=10000,
            train_interval=4, delta_clip=1.)
dqn.compile(Adam(learning_rate=.00025), metrics=['mae'])
dqn.fit(env, nb_steps=175000, visuialize=True)
