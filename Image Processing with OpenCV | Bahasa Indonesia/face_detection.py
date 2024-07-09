# Import module.
import cv2


# Load gambar dan model pre-trained Haar Cascade classifier.
image = cv2.imread('resources/Kennedy Space Center.jpg')
haar_cascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')


# Mendeteksi wajah dengan model pre-trained.
faces_rect = haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)


# Menampilkan koordinat wajah yang terdeteksi.
print(faces_rect)
# Output:
# [[563  94  78  78]
#  [244  93  74  74]
#  [407 104  65  65]]


# Menggambarkan dan menampilkan bounding box berdasarkan koordinat tadi.
image_bbox = image.copy()
for x, y, w, h in faces_rect:
    cv2.rectangle(image_bbox, (x,y), (x+w,y+h), (255,0,255), 2)

cv2.imshow('image_bbox', image_bbox)
cv2.imshow('image', image)
cv2.waitKey(0)