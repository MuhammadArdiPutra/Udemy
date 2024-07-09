# Import module.
import cv2


# Load gambar & konversi ke grayscale
image = cv2.imread('resources/Stop.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Membandingkan gambar grayscale dengan channel merah.
b, g, r = cv2.split(image)

cv2.imshow('r', r)
cv2.imshow('gray', gray)
cv2.waitKey(0)


# Thresholding channel r dan g.
# Gunakan cv2.THRESH_BINARY_INV untuk meng-inverse warna.
thresh, binary_r = cv2.threshold(r, 240, 255, cv2.THRESH_BINARY)
thresh, binary_g = cv2.threshold(g, 150, 255, cv2.THRESH_BINARY)

cv2.imshow('binary_r', binary_r)
cv2.imshow('binary_g', binary_g)
cv2.waitKey(0)


# Mengatur threshold dengan trackbar.
def skip(x):
    pass

cv2.namedWindow('Threshold Adjustment')
cv2.resizeWindow('Threshold Adjustment', 400, 30)

cv2.createTrackbar('threshold', 'Threshold Adjustment', 128, 255, skip)

while True:
    image = cv2.imread('resources/Stop.jpg')
    b, g, r = cv2.split(image)

    threshold = cv2.getTrackbarPos('threshold', 'Threshold Adjustment')

    thresh, binary_r = cv2.threshold(r, threshold, 255, cv2.THRESH_BINARY)

    cv2.imshow('r', r)
    cv2.imshow('binary_r', binary_r)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break