# Import module.
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Import gambar (flags=0 gambar di-load sebagai grayscale, flags=1 BGR).
image = cv2.imread('resources/Bebek.jpg', flags=1)


# Konversi color space.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow('image', image)
cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)
cv2.imshow('hsv', hsv)
cv2.imshow('hls', hls)
cv2.imshow('lab', lab)
cv2.waitKey(0)


# Menampilkan gambar dengan Matplotlib.
plt.imshow(rgb)
plt.show()


# Split dan menampilkan channel warna BGR secara terpisah.
image = cv2.imread('resources/Red Car.jpg')
b, g, r = cv2.split(image)

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey(0)


# Menggabungkan channel warna.
black = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')
b = cv2.merge([b,black,black])
g = cv2.merge([black,g,black])
r = cv2.merge([black,black,r])

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey(0)


# Menampilkan channel warna HSV secara terpisah.
image = cv2.imread('resources/Red Car.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)
cv2.waitKey(0)