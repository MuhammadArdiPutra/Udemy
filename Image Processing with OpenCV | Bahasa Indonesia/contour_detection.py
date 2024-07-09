# Import module.
import cv2
import numpy as np


# Load dan konversi menjadi gambar binary.
image = cv2.imread('resources/Shapes.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('image', image)
cv2.imshow('thresholded', thresholded)
cv2.waitKey(0)


# Mendeteksi contour pada gambar binary.
# Alternatif parameter kedua: cv2.RETR_TREE, cv2.RETR_LIST, cv2.RETR_EXTERNAL.
# Alternatif parameter ketiga: cv2.CHAIN_APPROX_SIMPLE, cv2.CHAIN_APPROX_NONE.
contours, hierarchies = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Menghitung jumlah contour yang terdeteksi.
print(len(contours))    # Output: 4


# Menampilkan koordinat penyusun contour objek ke-0 yang ditemukan.
print(contours[0])      
# Output:
# [[[284 203]]
#  [[283 204]]
#  [[283 302]] ...


# Menggambarkan titik-titik contour.
image_contour_points = image.copy()
for contour in contours:
    for point in contour:
        point = np.squeeze(point)
        cv2.circle(image_contour_points, point, 2, (255,0,255), -1)

cv2.imshow('image_contour_points', image_contour_points)
cv2.waitKey(0)


# Menggambar contour secara keseluruhan.
image_contour = image.copy()
cv2.drawContours(image_contour, contours, -1, (0,255,0), 2)

cv2.imshow('image_contour', image_contour)
cv2.waitKey(0)


# Menampilkan hierarchy.
print(hierarchies)
# Output: 
# [[[ 1 -1 -1 -1]
#   [ 3  0  2 -1]
#   [-1 -1 -1  1]
#   [-1  1 -1 -1]]]