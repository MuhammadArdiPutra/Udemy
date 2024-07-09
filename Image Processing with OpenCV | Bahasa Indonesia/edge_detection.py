# Import module.
import cv2
import numpy as np


# Load gambar & konversi ke grayscale.
image = cv2.imread('resources/Bill Gates.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Laplacian edge detection.
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

cv2.imshow('gray', gray)
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)


# Sobel edge detection.
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_xy = cv2.magnitude(sobel_x, sobel_y)


# Sobel edge sebelum normalisasi.
cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)
cv2.imshow('sobel_xy', sobel_xy)
cv2.waitKey(0)


# Normalisasi fitur edge sobel agar nilai pixel ada di rentang 0-255.
sobel_x_normalized = np.uint8(np.absolute(sobel_x))
sobel_y_normalized = np.uint8(np.absolute(sobel_y))
sobel_xy_normalized = np.uint8(np.absolute(sobel_xy))

cv2.imshow('sobel_x_normalized', sobel_x_normalized)
cv2.imshow('sobel_y_normalized', sobel_y_normalized)
cv2.imshow('sobel_xy_normalized', sobel_xy_normalized)
cv2.waitKey(0)


# Prewitt edge detection.
prewitt_kernel_x = np.array([[-1, 0, 1], 
                             [-1, 0, 1], 
                             [-1, 0, 1]])

prewitt_kernel_y = np.array([[-1, -1, -1], 
                             [0, 0, 0], 
                             [1, 1, 1]])

prewitt_x = cv2.filter2D(gray, cv2.CV_64F, prewitt_kernel_x)
prewitt_y = cv2.filter2D(gray, cv2.CV_64F, prewitt_kernel_y)

prewitt_xy = cv2.magnitude(prewitt_x, prewitt_y)
prewitt_xy_normalized = np.uint8(np.absolute(prewitt_xy))

cv2.imshow('prewitt_xy_normalized', prewitt_xy_normalized)
cv2.waitKey(0)


# Roberts edge detection.
roberts_kernel_x = np.array([[1, 0], 
                             [0, -1]], dtype=np.float32)

roberts_kernel_y = np.array([[0, 1], 
                             [-1, 0]], dtype=np.float32)

roberts_x = cv2.filter2D(gray, cv2.CV_64F, roberts_kernel_x)
roberts_y = cv2.filter2D(gray, cv2.CV_64F, roberts_kernel_y)

roberts_xy = cv2.magnitude(roberts_x, roberts_y)
roberts_xy_normalized = np.uint8(np.absolute(roberts_xy))

cv2.imshow('roberts_xy_normalized', roberts_xy_normalized)
cv2.waitKey(0)