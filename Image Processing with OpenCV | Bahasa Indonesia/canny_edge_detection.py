# Import module.
import cv2
import numpy as np


# Load gambar dan preprocessing.
image = cv2.imread('resources/Leaf.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (5,5))


# Gambar original dan sesudah preprocessing (grayscale conversion & blurring).
cv2.imshow('image', image)
cv2.imshow('blur', blur)
cv2.waitKey(0)


# Canny edge detection dengan rasio threshold 1:2 dan 1:3.
canny0 = cv2.Canny(blur, 50, 100)
canny1 = cv2.Canny(blur, 50, 150)

cv2.imshow('canny0', canny0)
cv2.imshow('canny1', canny1)
cv2.waitKey(0)


# Perbandingan Canny dengan Sobel.
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel_xy = cv2.magnitude(sobel_x, sobel_y)
sobel_xy_normalized = np.uint8(np.absolute(sobel_xy))

cv2.imshow('sobel_xy_normalized', sobel_xy_normalized)
cv2.imshow('canny0', canny0)
cv2.waitKey(0)


# Contoh hasil Canny jika tidak melalui tahap smoothing.
canny = cv2.Canny(gray, 50, 100)

cv2.imshow('canny', canny)
cv2.waitKey(0)


# Penentuan threshold menggunakan nilai median.
med = np.median(blur)
lower_thresh = int((1.0 - 0.33) * med)
upper_thresh = int((1.0 + 0.33) * med)

print(med)              # Output: 133.0
print(lower_thresh)     # Output: 89
print(upper_thresh)     # Output: 176

canny = cv2.Canny(blur, lower_thresh, upper_thresh)
cv2.imshow('canny', canny)
cv2.waitKey(0)


# Menggunakan trackbar untuk mengatur threshold.
def skip(x):
    pass

cv2.namedWindow('Threshold Adjustment')
cv2.resizeWindow('Threshold Adjustment', 400, 60)

cv2.createTrackbar('Upper', 'Threshold Adjustment', 100, 255, skip)
cv2.createTrackbar('Lower', 'Threshold Adjustment', 50, 255, skip)

while True:
    image = cv2.imread('resources/Leaf.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (5,5), 0)

    upper_thresh =  cv2.getTrackbarPos('Upper', 'Threshold Adjustment')
    lower_thresh = cv2.getTrackbarPos('Lower', 'Threshold Adjustment')

    canny = cv2.Canny(blur, lower_thresh, upper_thresh)

    cv2.imshow('blur', blur)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break