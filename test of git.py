import math

import numpy as np
import cv2

image = cv2.imread("flowers.jpg")
height, width,  channels = image.shape

outputForHValue = np.zeros((height, width, channels), np.uint8)
outputForSValue = np.zeros((height, width, channels), np.uint8)
outputForIValue = np.zeros((height, width, channels), np.uint8)

imageData = np.asarray(image)

def calculateH():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            B = pixel[0]
            G = pixel[1]
            R = pixel[2]
            test1 = (R-G)+(R-B)
            if test1 > 0:
                test1 = test1 / 2
            else:
                test1 = 1
                test1 = test1 / 2
            if test1 > 0 and math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B)) > 0:
                test1 = test1 / math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B))
            else:
                test1 = 1
                test1 = test1 / (math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B))+1)
            if test1 > 0:
                test1 = test1/360
            else:
                test1 = 1
                test1 = test1 / 360

            hAngle = math.degrees(math.acos(test1))


            hValue= 0
            if B <= G:
                hValue = hAngle
            elif G<B:
                hValue = 360-hAngle
            else:
                hValue = 0
            outputForHValue[i, j, 0] = hValue
            outputForHValue[i, j, 1] = hValue
            outputForHValue[i, j, 2] = hValue


def calculateS():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            B = pixel[0]
            G = pixel[1]
            R = pixel[2]
            sValue = 255-(3*min(R, G, B))
            outputForSValue[i, j, 0] = sValue
            outputForSValue[i, j, 1] = sValue
            outputForSValue[i, j, 2] = sValue


def calculateI():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            B = pixel[0]
            G = pixel[1]
            R = pixel[2]
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
