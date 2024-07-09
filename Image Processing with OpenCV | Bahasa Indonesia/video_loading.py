# Import module.
import cv2

# Load file video (atau angka '0' jika mau ambil dari webcam).
capture = cv2.VideoCapture('resources/Drone Video.webm')


# Loop untuk membaca frame satu per satu.
while True:
    frame_exist, frame = capture.read()

    # Error handler ketika frame habis.
    if frame_exist == False:
        break
    
    # Menampilkan frame.
    cv2.imshow('frame', frame)

    # Jika huruf 'q' ditekan, playback akan berhenti.
    # cv2.waitKey() untuk mengatur kecepatan playback.
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


# Menghapus video dari variabel 'capture'.
capture.release()
cv2.destroyAllWindows()