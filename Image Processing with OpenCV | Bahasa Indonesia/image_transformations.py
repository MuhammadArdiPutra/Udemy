# Import module.
import cv2
import numpy as np


# Load gambar.
image = cv2.imread('resources/Bill Gates.jpg')


# Cropping.
cropped = image[60:220, 80:220]

cv2.imshow('image', image)
cv2.imshow('cropped', cropped)
cv2.waitKey(0)


# Resizing (ukuran output bebas).
resized = cv2.resize(image, (450,300))

cv2.imshow('image', image)
cv2.imshow('resized', resized)
cv2.waitKey(0)


# Resizing (ukuran output proporsional).
scale = 0.6
height = image.shape[0]
width = image.shape[1]

resized = cv2.resize(image, (int(width*scale),int(height*scale)))

cv2.imshow('image', image)
cv2.imshow('resized', resized)
cv2.waitKey(0)


# Pyramid down & up.
down = cv2.pyrDown(image)
up = cv2.pyrUp(image)

print(image.shape)      # Output: (485, 320, 3)
print(down.shape)       # Output: (243, 160, 3)
print(up.shape)         # Output: (970, 640, 3)

cv2.imshow('image', image)
cv2.imshow('down', down)
cv2.imshow('up', up)
cv2.waitKey(0)


# Flip.
flipped_v = cv2.flip(image, 0)
flipped_h = cv2.flip(image, 1)
flipped_both = cv2.flip(image, -1)

cv2.imshow('image', image)
cv2.imshow('flipped_v', flipped_v)
cv2.imshow('flipped_h', flipped_h)
cv2.imshow('flipped_both', flipped_both)
cv2.waitKey(0)


# Rotate.
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('image', image)
cv2.imshow('rotated_90', rotated_90)
cv2.imshow('rotated_180', rotated_180)
cv2.imshow('rotated_270', rotated_270)
cv2.waitKey(0)