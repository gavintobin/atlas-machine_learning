#!/usr/bin/env python3
'''task 5'''
import tensorflow as tf


def change_brightness(image, max_delta):
    '''changes brightness'''
    change = tf.image.random_brightness(image=image, max_delta=max_delta)
    return change
