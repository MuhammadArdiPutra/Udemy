# Import module.
import cv2
import numpy as np


# Load & preprocess gambar (grayscaling, binarization, opening).
image = cv2.imread('resources/Scan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
opened = cv2.erode(thresholded, kernel, iterations=1)
opened = cv2.dilate(opened, kernel, iterations=1)

cv2.imshow('image', image)
cv2.imshow('gray', gray)
cv2.imshow('thresholded', thresholded)
cv2.imshow('opened', opened)
cv2.waitKey(0)


# Deteksi & menampilkan contour.
contours, hierarchy = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

image_contour = image.copy()
cv2.drawContours(image_contour, contours, -1, (0,255,0), 2)

cv2.imshow('image_contour', image_contour)
cv2.waitKey(0)


# Mencari koordinat sudut contour besar.
for contour in contours:
    area = cv2.contourArea(contour)

    if area > 1000:
        epsilon = 0.05 * cv2.arcLength(contour, closed=True)
        polygon = cv2.approxPolyDP(contour, epsilon, closed=True)

print(polygon)
# Output:
# [[[190 162]]
#  [[ 25 381]]
#  [[292 464]]
#  [[416 210]]]


# Menghighlight sudut contour besar satu per satu (belum terurut).
image_corner = image.copy()
for corner in polygon:
    corner = np.squeeze(corner)
    cv2.circle(image_corner, corner, 7, (230,255,0), -1)
    cv2.imshow('image_corner', image_corner)
    cv2.waitKey(0)


# Mengurutkan koordinat corner (kiri atas, kanan atas, kiri bawah, kanan bawah).
def sort_coords(polygon):
    polygon = np.squeeze(polygon)
    rect_coords = np.zeros((4, 2))

    add = polygon.sum(axis=1)
    rect_coords[0] = polygon[np.argmin(add)]    # Kiri atas
    rect_coords[3] = polygon[np.argmax(add)]    # Kanan bawah

    subtract = np.diff(polygon, axis=1)
    rect_coords[1] = polygon[np.argmin(subtract)]    # Kanan atas
    rect_coords[2] = polygon[np.argmax(subtract)]    # Kiri bawah
    
    return rect_coords.astype('float32')

points_src = sort_coords(polygon)
print(points_src)
# Output: 
# [[190. 162.]
#  [416. 210.]
#  [ 25. 381.]
#  [292. 464.]]


# Menghighlight sudut contour besar satu per satu (sudah terurut).
image_corner = image.copy()
for corner in points_src:
    corner = np.squeeze(corner).astype('int')
    cv2.circle(image_corner, corner, 7, (230,255,0), -1)
    cv2.imshow('image_corner', image_corner)
    cv2.waitKey(0)


# Membuat transformation matrix untuk perspective transform.
width_dst  = 432
height_dst = 632

points_dst = np.array([[0,0], [width_dst,0], [0,height_dst], [width_dst,height_dst]], dtype='float32')

matrix = cv2.getPerspectiveTransform(points_src, points_dst)
print(matrix)
# Output:
# [[ 2.25619976e+00  1.69987653e+00 -7.04057954e+02]
#  [-8.24071554e-01  3.88000357e+00 -4.71986983e+02]
#  [ 1.51008755e-04  1.45896313e-03  1.00000000e+00]]


# Mengubah perspektif gambar menggunakan transformation matrix tadi.
transfromed = cv2.warpPerspective(image, matrix, (width_dst, height_dst))

cv2.imshow('image', image)
cv2.imshow('transfromed', transfromed)
cv2.waitKey(0)