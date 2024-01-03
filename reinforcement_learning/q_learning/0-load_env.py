#!/usr/bin/env python3
'''task 1'''
import gym
from gym.envs.registration import register


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    '''load frozen lake'''
    if desc is not None and map_name is not None:
        raise ValueError("Only one of desc or map_name should be provided")

    # rgister the custom environment if desc is provided
    if desc is not None:
        register(
            id='FrozenLakeCustom-v0',
            entry_point='gym.envs.toy_text:FrozenLakeEnv',
            kwargs={'map_name': '8x8', 'desc': desc,
                    'is_slippery': is_slippery},
            max_episode_steps=100,
            reward_threshold=0.74,  # match the default settings of fl env
        )
        env = gym.make('FrozenLakeCustom-v0')

    # load the pre-made map if map_name is provided
    elif map_name is not None:
        env = gym.make(f'FrozenLake-{map_name}-v0')

    # load a randomly generated 8x8 map if neither desc nor mn provided
    else:
        env = gym.make('FrozenLake-v1', is_slippery=is_slippery)

    return env
