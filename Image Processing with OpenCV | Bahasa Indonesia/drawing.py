# Import module.
import cv2


# Load & menampilkan gambar untuk canvas.
image = cv2.imread('resources/Pemandangan.jpg')
cv2.imshow('image', image)
cv2.waitKey(0)


# Membuat kotak dengan array slicing (mengubah warna pixel).
image[50:100, 200:250]  = 255, 0, 0
image[200:250, 50:100]  = 0, 200, 0
image[200:250, 120:170] = 0, 0, 150

cv2.imshow('image', image)
cv2.waitKey(0)


# Menggambar kotak dengan cv2.rectangle().
image = cv2.imread('resources/Pemandangan.jpg')

cv2.rectangle(img=image, pt1=(10,30), pt2=(200,400), color=(255,0,255), thickness=3)
cv2.rectangle(image, (100,100), (120,50), (255,0,0), -1)

cv2.imshow('image', image)
cv2.waitKey(0)


# Menggambar kotak dengan variabel xywh.
image = cv2.imread('resources/Pemandangan.jpg')

x = 100
y = 100
w = 200
h = 70
cv2.rectangle(image, (x,y), (x+y,w+h), (0,0,255), -1)

cv2.imshow('image', image)
cv2.waitKey(0)


# Menggambar lingkaran dengan cv2.circle().
image = cv2.imread('resources/Pemandangan.jpg')

cv2.circle(img=image, center=(image.shape[1]//2, image.shape[0]//2), radius=30, color=(150,255,150), thickness=6)

cv2.imshow('image', image)
cv2.waitKey(0)


# Menggambar garis dengan cv2.line().
image = cv2.imread('resources/Pemandangan.jpg')

cv2.line(img=image, pt1=(x,y), pt2=(x+w,y+h), color=(255,10,10), thickness=6)

cv2.imshow('image', image)
cv2.waitKey(0)


# Membuat tulisan dengan cv2.putText() dengan kotak sebagai backgroundnya.
image = cv2.imread('resources/Pemandangan.jpg')

cv2.rectangle(image, (10,10), (250,90), (0,0,0), -1)
cv2.putText(img=image, text='Hallo', org=(10,80), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=3, 
            color=(255,255,255), thickness=2)

cv2.imshow('image', image)
cv2.waitKey(0)


'''
Alternatif fontFace untuk cv2.putText():
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7
'''
