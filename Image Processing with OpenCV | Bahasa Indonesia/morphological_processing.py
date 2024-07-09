# Import module.
import cv2
import numpy as np


# Load gambar & konversi ke binary image.
image = cv2.imread('resources/Sign.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('image', image)
cv2.imshow('thresholded', thresholded)
cv2.waitKey(0)


# 3 cara membuat kernel.
kernel = np.ones((3,3), np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

kernel = np.array([[1,1,1], 
                   [1,1,1], 
                   [1,1,1]], np.uint8)


# Dilation.
dilated = cv2.dilate(thresholded, kernel, iterations=1)
dilated0 = cv2.dilate(thresholded, kernel, iterations=2)
dilated1 = cv2.dilate(thresholded, kernel, iterations=3)
dilated2 = cv2.dilate(thresholded, kernel, iterations=4)

cv2.imshow('dilated', dilated)
cv2.imshow('dilated0', dilated0)
cv2.imshow('dilated1', dilated1)
cv2.imshow('dilated2', dilated2)
cv2.waitKey(0)


# Erosion.
eroded = cv2.erode(thresholded, kernel, iterations=1)
eroded0 = cv2.erode(thresholded, kernel, iterations=2)
eroded1 = cv2.erode(thresholded, kernel, iterations=3)
eroded2 = cv2.erode(thresholded, kernel, iterations=4)

cv2.imshow('eroded', eroded)
cv2.imshow('eroded0', eroded0)
cv2.imshow('eroded1', eroded1)
cv2.imshow('eroded2', eroded2)
cv2.waitKey(0)


# Closing.
closed = cv2.dilate(thresholded, kernel, iterations=1)
closed = cv2.erode(closed, kernel, iterations=1)


# Opening.
opened = cv2.erode(thresholded, kernel, iterations=1)
opened = cv2.dilate(opened, kernel, iterations=1)


# Membandingkan gambar hasil keempat morphological processing (dengan iterations=1).
cv2.imshow('thresholded', thresholded)
cv2.imshow('dilated', dilated)
cv2.imshow('eroded', eroded)
cv2.imshow('closed', closed)
cv2.imshow('opened', opened)
cv2.waitKey(0)