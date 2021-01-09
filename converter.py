import cv2
import pytesseract 


def ocr(image):
    text = pytesseract.image_to_string(image)
    return text


image = cv2.imread('convo.jpg')

def bw(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


def threshold(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

image = bw(image)
image = noise(image)
image = threshold(image)

print(ocr(image))

