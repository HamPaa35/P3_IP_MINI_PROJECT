import numpy as np
import cv2

image = cv2.imread("flowers.jpg")
height, width,  channels = image.shape

outputForHValue = np.zeros((height, width, channels), np.uint8)
outputForSValue = np.zeros((height, width, channels), np.uint8)
outputForIValue = np.zeros((height, width, channels), np.uint8)

cv2.imwrite('outputHValue.jpg', outputForHValue)

imageData = np.asarray(image)

def calculateH():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            outputForHValue[i, j, 0] = pixel[0]+50
            outputForHValue[i, j, 1] = pixel[1]+50
            outputForHValue[i, j, 2] = pixel[2]+50


def calculateS():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            outputForSValue[i, j, 0] = pixel[0]+20
            outputForSValue[i, j, 1] = pixel[1]+20
            outputForSValue[i, j, 2] = pixel[2]+20


def calculateI():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            outputForIValue[i, j, 0] = pixel[0]+40
            outputForIValue[i, j, 1] = pixel[1]+40
            outputForIValue[i, j, 2] = pixel[2]+40


calculateH()
calculateS()
calculateI()

cv2.imwrite('outputHValue.jpg', outputForHValue)
cv2.imwrite('outputSValue.jpg', outputForSValue)
cv2.imwrite('outputIValue.jpg', outputForIValue)
