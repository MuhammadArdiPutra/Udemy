# Import module.
import cv2
import numpy as np


# Membuat gambar 'vertical' dan 'horizontal'.
vertical = np.zeros((500,500), dtype='uint8')
horizontal = np.zeros((500,500), dtype='uint8')

cv2.rectangle(vertical, (140,50), (240,450), 255, -1)
cv2.rectangle(horizontal, (120,230), (420,300), 255, -1)


# Implementasi operator bitwise.
image_or  = cv2.bitwise_or(vertical, horizontal)
image_and = cv2.bitwise_and(vertical, horizontal)
image_xor = cv2.bitwise_xor(vertical, horizontal)
image_not = cv2.bitwise_not(vertical)


# Implementasi bitwise AND untuk masking.
image = cv2.imread('resources/Pemandangan.jpg')
image = image[:500, :500]
masked = cv2.bitwise_and(image, image, mask=image_xor)


# Menampilkan gambar.
cv2.imshow('vertical', vertical)
cv2.imshow('horizontal', horizontal)
cv2.imshow('image_or', image_or)
cv2.imshow('image_and', image_and)
cv2.imshow('image_xor', image_xor)
cv2.imshow('image_not', image_not)
cv2.imshow('image', image)
cv2.imshow('masked', masked)
cv2.waitKey(0)