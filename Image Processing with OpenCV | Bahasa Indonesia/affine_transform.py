# Import module.
import cv2
import numpy as np


# Load gambar dan ambil dimensinya.
image = cv2.imread('resources/Waterfall.jpg')
height = image.shape[0]
width  = image.shape[1]


# Rescale/resize.
scale_x = 1.7
scale_y = 0.7

matrix = np.array([[scale_x, 0, 0], 
                   [0, scale_y, 0]], dtype='float32')

scaled = cv2.warpAffine(image, matrix, (int(width*scale_x), int(height*scale_y)))

cv2.imshow('image', image)
cv2.imshow('scaled', scaled)
cv2.waitKey(0)


# Shear.
shear_x = 0.3
shear_y = 0

matrix = np.array([[1, shear_x, 0], 
                   [shear_y, 1, 0]], dtype='float32')

sheared = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow('image', image)
cv2.imshow('sheared', sheared)
cv2.waitKey(0)


# Translate.
translate_x = 20
translate_y = 100

matrix = np.array([[1, 0, translate_x], 
                   [0, 1, translate_y]], dtype='float32')

translated = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow('image', image)
cv2.imshow('translated', translated)
cv2.waitKey(0)


# Flip (horizontal).
matrix = np.array([[-1, 0 , width], 
                   [0, 1, 0]], dtype='float32')

flipped_h = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow('image', image)
cv2.imshow('flipped_h', flipped_h)
cv2.waitKey(0)


# Flip (vertical).
matrix = np.array([[1, 0 , 0], 
                   [0, -1, height]], dtype='float32')

flipped_v = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow('image', image)
cv2.imshow('flipped_v', flipped_v)
cv2.waitKey(0)


# Flip (both).
matrix = np.array([[-1, 0 , width], 
                   [0, -1, height]], dtype='float32')

flipped_both = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow('image', image)
cv2.imshow('flipped_both', flipped_both)
cv2.waitKey(0)


# Rotate.
center = (width//2, height//2)
angle = 45
scale = 1

matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow('image', image)
cv2.imshow('rotated', rotated)
cv2.waitKey(0)


# Banyak transformasi sekaligus (shear, translate, rescale).
matrix = np.array([[1.2, 0,  30], 
                   [0.1, 0.8, 40]], dtype='float32')

transformed = cv2.warpAffine(image, matrix, (width+180,height+50))

cv2.imshow('image', image)
cv2.imshow('transformed', transformed)
cv2.waitKey(0)