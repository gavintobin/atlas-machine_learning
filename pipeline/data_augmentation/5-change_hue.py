#!/usr/bin/env python3
'''task 5'''
import tensorflow as tf


def change_hue(image, delta):
    '''change hue of image'''
    hue = tf.image.adjust_hue(image=image, delta=delta)
    return hue
