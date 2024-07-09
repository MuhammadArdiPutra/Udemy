# Import module.
import cv2
import numpy as np


# Import gambar train dan query.
image_train = cv2.imread('resources/book_train1.png', cv2.IMREAD_GRAYSCALE)
image_query = cv2.imread('resources/book_query1.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image_train', image_train)
cv2.imshow('image_query', image_query)
cv2.waitKey(0)


# Inisialisasi keypoint detector.
detector = cv2.ORB_create(nfeatures=500)


# Mendeteksi keypoint dan descriptor menggunakan keypoint detector tadi.
keypoints_t, descriptors_t = detector.detectAndCompute(image_train, None)
keypoints_q, descriptors_q = detector.detectAndCompute(image_query, None)


# Menampilkan beberapa atribut yang tersimpan di objek keypoint ke-0.
print(keypoints_t[0].pt)        # Output: (180.0, 154.0)
print(keypoints_t[0].size)      # Output: 31.0
print(keypoints_t[0].angle)     # Output: 260.89959716796875


# Menampilkan shape dari descriptor.
print(descriptors_t.shape)      # Output: (500, 32)


# Inisialisasi brute force matcher.
# Alternatif parameter: cv2.NORM_HAMMING, cv2.NORM_L1, cv2.NORM_L2.
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)


# Mencocokkan keypoint pada gambar query dan train dengan brute force matcher tadi.
matches = matcher.match(descriptors_q, descriptors_t)


# Menampilkan beberapa atribut pasangan keypoint ke-0.
print(matches[0].queryIdx)      # Output: 0
print(matches[0].trainIdx)      # Output: 197
print(matches[0].distance)      # Output: 57.0


# Mengurutkan pasangan keypoints berdasarkan atribut distance dan 
# menampilkan distance dari 15 pasangan teratas.
matches = sorted(matches, key=lambda x: x.distance)
for match in matches[:15]:
    print(match.distance)


# Menggambarkan 20 pasangan keypoints yang paling mirip.
image_matches = cv2.drawMatches(image_query, keypoints_q, image_train, keypoints_t, matches[:20], None, 
                                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('image_matches', image_matches)
cv2.waitKey(0)