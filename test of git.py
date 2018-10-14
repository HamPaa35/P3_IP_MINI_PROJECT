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
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            hValue= 200
            outputForHValue[i, j, 0] = hValue
            outputForHValue[i, j, 1] = hValue
            outputForHValue[i, j, 2] = hValue


def calculateS():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            sValue = 255-(3*min(R, G, B))
            outputForSValue[i, j, 0] = sValue
            outputForSValue[i, j, 1] = sValue
            outputForSValue[i, j, 2] = sValue


def calculateI():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            iValue = (R+G+B)/3
            outputForIValue[i, j, 0] = iValue
            outputForIValue[i, j, 1] = iValue
            outputForIValue[i, j, 2] = iValue


calculateH()
calculateS()
calculateI()

cv2.imwrite('outputHValue.jpg', outputForHValue)
cv2.imwrite('outputSValue.jpg', outputForSValue)
cv2.imwrite('outputIValue.jpg', outputForIValue)
