# Import module.
import cv2


# Load gambar & split channel warna.
image = cv2.imread('resources/Stop.jpg')
b, g, r = cv2.split(image)


# Membandingkan hasil thresholding manual dengan Otsu (global).
thresh, binary_r, = cv2.threshold(r, 240, 255, cv2.THRESH_BINARY)
thresh_otsu, binary_r_otsu, = cv2.threshold(r, None, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print('Manual threshold\t:', thresh)
print('Otsu threshold\t\t:', thresh_otsu)

cv2.imshow('binary_r', binary_r)
cv2.imshow('binary_r_otsu', binary_r_otsu)
cv2.waitKey(0)


# Adaptive local thresholding.
# Alternatif: cv2.ADAPTIVE_THRESH_GAUSSIAN_C.
image = cv2.imread('resources/Book.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 10)
cv2.imshow('binary', binary)
cv2.waitKey(0)