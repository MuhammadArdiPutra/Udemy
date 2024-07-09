# Import module.
import cv2


# Load gambar noisy.
image = cv2.imread('resources/Harimau.jpg')

 
# Average smoothing.
image_avg0 = cv2.blur(image, (3,3))
image_avg1 = cv2.blur(image, (7,7))
image_avg2 = cv2.blur(image, (15,15))

cv2.imshow('image', image)
cv2.imshow('image_avg0', image_avg0)
cv2.imshow('image_avg1', image_avg1)
cv2.imshow('image_avg2', image_avg2)
cv2.waitKey(0)


# Gaussian smoothing.
image_gaussian0 = cv2.GaussianBlur(image, (3,3), 0)
image_gaussian1 = cv2.GaussianBlur(image, (7,7), 0)
image_gaussian2 = cv2.GaussianBlur(image, (15,15), 0)

cv2.imshow('image', image)
cv2.imshow('image_gaussian0', image_gaussian0)
cv2.imshow('image_gaussian1', image_gaussian1)
cv2.imshow('image_gaussian2', image_gaussian2)
cv2.waitKey(0)


# Median smoothing.
image_median0 = cv2.medianBlur(image, 3)
image_median1 = cv2.medianBlur(image, 7)

cv2.imshow('image', image)
cv2.imshow('image_median0', image_median0)
cv2.imshow('image_median1', image_median1)
cv2.waitKey(0)


# Perbandingan ketiga algoritma smoothing untuk menghilangkan detail.
image = cv2.imread('resources/Bill Gates.jpg')
image_avg = cv2.blur(image, (3,3))
image_gaussian = cv2.GaussianBlur(image, (3,3), 0)
image_median = cv2.medianBlur(image, 3)

cv2.imshow('image', image)
cv2.imshow('image_avg', image_avg)
cv2.imshow('image_gaussian', image_gaussian)
cv2.imshow('image_median', image_median)
cv2.waitKey(0)