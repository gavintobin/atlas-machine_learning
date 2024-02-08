#!/usr/bin/env python3
'''task 3'''
import tensorflow as tf


def rotate_image(image):
    '''rotate image'''
    rot = tf.image.rot90(image=image)
    return rot
