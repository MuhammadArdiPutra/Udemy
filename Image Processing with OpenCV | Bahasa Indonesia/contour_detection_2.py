# Import module.
import cv2
import numpy as np

# Load gambar, preprocessing, dan mencari contour.
image = cv2.imread('resources/Shapes.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
contours, hierarchies = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Menghitung luas contour.
for contour in contours:
    area = cv2.contourArea(contour)
    print(area)

# Output:
# 5294.0
# 12285.0
# 2096.0
# 9012.0


# Menghitung keliling contour.
for contour in contours:
    perimeter = cv2.arcLength(contour, closed=True)
    print(perimeter)

# Output:
# 341.4213515520096
# 452.0
# 182.5096652507782
# 355.3624790906906


# Menghitung jumlah sudut.
polygons = []

for contour in contours:
    perimeter = cv2.arcLength(contour, closed=True)
    epsilon = 0.04 * perimeter

    polygon = cv2.approxPolyDP(contour, epsilon, closed=True)
    polygons.append(polygon)

for polygon in polygons:
    print(len(polygon))

# Output:
# 3
# 4 
# 5
# 8


# Menampilkan sudut yang terdeteksi.
image_corners = image.copy()

for polygon in polygons:
    for corner in polygon:
        corner = np.squeeze(corner)
        cv2.circle(image_corners, corner, 2, (0,0,0), -1)

cv2.imshow('image_corners', image_corners)
cv2.waitKey(0)


# Filtering contour berdasarkan jumlah sudut (hanya mendeteksi lingkaran).
image_corners = image.copy()

for i, (polygon, contour) in enumerate(zip(polygons, contours)):
    if len(polygon) < 7:
        pass

    else:
        image_corners = cv2.drawContours(image_corners, contours, i, (0,255,0), 2)
        for corner in polygon:
            corner = np.squeeze(corner)
            cv2.circle(image_corners, corner, 2, (0,0,0), -1)

cv2.imshow('image_corners', image_corners)
cv2.waitKey(0)


# Filtering contour berdasarkan area (hanya mendeteksi contour kecil).
image_corners = image.copy()

for i, (polygon, contour) in enumerate(zip(polygons, contours)):

    area = cv2.contourArea(contour)
    
    if area < 6000:

        image_corners = cv2.drawContours(image_corners, contours, i, (0,255,0), 2)
        for corner in polygon:
            corner = np.squeeze(corner)
            cv2.circle(image_corners, corner, 2, (0,0,0), -1)

cv2.imshow('image_corners', image_corners)
cv2.waitKey(0)