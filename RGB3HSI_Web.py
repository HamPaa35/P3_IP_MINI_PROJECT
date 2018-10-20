import math

import numpy as np
import cv2

image = cv2.imread("flowers.jpg")
height, width,  channels = image.shape

outputForHValueWeb = np.zeros((height, width, channels), np.uint64)
outputForSValueWeb = np.zeros((height, width, channels), np.uint64)
outputForIValueWeb = np.zeros((height, width, channels), np.uint64)
outputForHSIValueWeb = np.zeros((height, width, channels), np.uint64)

imageData = np.asarray(image)

def calculateHWeb(R, G, B, max, dif, sValue):

    hValue = 0

    if sValue is not 0:
        if max == R:
            if dif == 0:
                dif = 1
            hValue = (60*(G-B)/dif)
        elif max == G:
            hValue = (60*(B-R)/dif+120)
        elif max == B:
            hValue = (60*(R-G)/dif+240)
        if hValue < 0:
            hValue = (60*(B-R)/dif+120)
    else:
        hValue = -1

    return hValue

def calculateSWeb(iValue, sum, dif):
    if sum == 0:
        sum = 1
    if iValue < 128:
        return 255*(dif/sum)
    else:
        return 255*(dif/(510-sum))


def calculateIWeb(sum):
    return sum/2



def calculateHSIWeb():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            B = pixel[0]
            G = pixel[1]
            R = pixel[2]

            nImax = max(R, B)
            nImax = max(nImax, G)
            nImin = min(R, B)
            nImin = min(nImin, G)
            nSum = nImin + nImax
            nDifference = nImax - nImin

            if R<0 and G<0 and B<0 or R>255 and G>255 and B >255:
                hValue=sValue=iValue=0

                outputForIValueWeb[i, j, 0] = iValue
                outputForIValueWeb[i, j, 1] = iValue
                outputForIValueWeb[i, j, 2] = iValue

                outputForSValueWeb[i, j, 0] = sValue
                outputForSValueWeb[i, j, 1] = sValue
                outputForSValueWeb[i, j, 2] = sValue

                outputForHValueWeb[i, j, 0] = hValue
                outputForHValueWeb[i, j, 1] = hValue
                outputForHValueWeb[i, j, 2] = hValue

                outputForHSIValueWeb[i, j, 0] = hValue
                outputForHSIValueWeb[i, j, 1] = sValue
                outputForHSIValueWeb[i, j, 2] = iValue
            else:
                iValue = calculateIWeb(nSum)
                outputForIValueWeb[i, j, 0] = iValue
                outputForIValueWeb[i, j, 1] = iValue
                outputForIValueWeb[i, j, 2] = iValue

                sValue = calculateSWeb(iValue, nSum, nDifference)
                outputForSValueWeb[i, j, 0] = sValue
                outputForSValueWeb[i, j, 1] = sValue
                outputForSValueWeb[i, j, 2] = sValue

                hValue = calculateHWeb(R, G, B, nImax, nDifference, sValue)
                if hValue>255:
                    hValue=255
                elif hValue<0:
                    hValue = 0
                outputForHValueWeb[i, j, 0] = hValue
                outputForHValueWeb[i, j, 1] = hValue
                outputForHValueWeb[i, j, 2] = hValue
                print(hValue, sValue, iValue)
                outputForHSIValueWeb[i, j, 0] = hValue
                outputForHSIValueWeb[i, j, 1] = sValue
                outputForHSIValueWeb[i, j, 2] = iValue


calculateHSIWeb()

cv2.imwrite('outputHValueWeb.jpg', outputForHValueWeb)
cv2.imwrite('outputSValueWeb.jpg', outputForSValueWeb)
cv2.imwrite('outputIValueWeb.jpg', outputForIValueWeb)
cv2.imwrite('outputHSIValueWeb.jpg', outputForHSIValueWeb)
print('The code completed Web')

#Try to implement this math http://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/
# Some problems may be the fact that it does not work with pure balck and white