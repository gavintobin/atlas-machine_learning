#!/usr/bin/env python3
'''task 1'''
import tensorflow as tf


def flip_image(image):
    '''flip image'''
    flipped = tf.image.flip_left_right(image)
    return flipped
