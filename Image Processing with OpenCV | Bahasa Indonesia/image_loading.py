# Import module.
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Cek versi module.
print(cv2.__version__)          # Output: 4.9.0
print(np.__version__)           # Output: 1.26.4
print(matplotlib.__version__)   # Output: 3.8.4


# Load & menampilkan gambar.
image = cv2.imread('resources/Bill Gates.jpg')
cv2.imshow(winname='Gambar', mat=image)
cv2.waitKey(0)


# Best practice menampilkan gambar (tanpa 'winname' dan 'mat').
image = cv2.imread('resources/Bill Gates.jpg')
print(image.shape)      # Output: (485, 320, 3)
cv2.imshow('image', image)
cv2.waitKey(0)


# Load sebagai gambar grayscale.
image = cv2.imread('resources/Bill Gates.jpg', flags=0)
print(image.shape)      # Output: (485, 320)
cv2.imshow('image', image)
cv2.waitKey(0)


# Membuat gambar hitam dan putih.
black = np.zeros((150,300))
white = np.ones((150,300))
cv2.imshow('black', black)
cv2.imshow('white', white)
cv2.waitKey(0)


# Vertical stack.
bw = np.vstack((black, white))
print(bw.shape)         # Output: (300, 300)
cv2.imshow('bw', bw)
cv2.waitKey(0)


# Horizontal stack.
bw = np.hstack((white, black, white))
print(bw.shape)         # Output: (150, 900)
cv2.imshow('bw', bw)
cv2.waitKey(0)