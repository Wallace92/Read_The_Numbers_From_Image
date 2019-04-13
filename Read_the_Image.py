import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
# src_path = "E:/Lab/Python/Project/OCR/"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint16)
    print(kernel)
    img = cv2.dilate(img, kernel, iterations=200)
    img = cv2.erode(img, kernel, iterations=2000)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 131, 10)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres.png"))

    # Remove template file
    #os.remove(temp)

    return result


# print('--- Start recognize text from image ---')
# print(get_string("1.png"))

wczytane_dane = get_string("2.png")

wczytane_dane = wczytane_dane.split('\n')
wczytane_dane = wczytane_dane[58:len(wczytane_dane)]
# print(wczytane_dane)
V1_Bp_Ip = wczytane_dane[0].split(' ')[1:5]
V2_Bp_Im = wczytane_dane[1].split(' ')[1:5]
V3_Bm_Im = wczytane_dane[2].split(' ')[1:5]
V4_Bm_Ip = wczytane_dane[3].split(' ')[1:5]
print(V1_Bp_Ip)
print(V2_Bp_Im)
print(V3_Bm_Im)
print(V4_Bm_Ip)
# print("------ Done -------")
