#!/usr/bin/env python3
'''task2'''
import tensorflow as tf


def crop_image(image, size):
    '''crop image'''
    cropped = tf.image.random_crop(image=image, size=size)
    return cropped
