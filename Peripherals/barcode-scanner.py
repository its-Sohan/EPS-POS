import cv2 as cv
from pyzbar.pyzbar import decode

def read_barcode():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        barcodes = decode(frame)
        if barcodes:
            data = barcodes[0].data.decode('utf-8')
            print(data)  # This goes to stdout
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_barcode()
