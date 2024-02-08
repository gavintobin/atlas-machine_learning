#!/usr/bin/env python3
'''task3'''
import tensorflow as tf


def shear_image(image, intensity):
    '''randomly shears'''
     shear_x = tf.random.uniform([], -shear_intensity, shear_intensity)
    shear_y = tf.random.uniform([], -shear_intensity, shear_intensity)

    # Create the affine transformation matrix
    affine_matrix = tf.constant([[1.0, shear_x, 0.0],
                                [shear_y, 1.0, 0.0]])

    # Apply the shear transformation using tf.image.transform
    sheared_image = tf.image.transform(image, affine_matrix)

    return sheared_image
