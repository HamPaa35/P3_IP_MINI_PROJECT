import math

import numpy as np
import cv2

image = cv2.imread("flowers.jpg")
height, width,  channels = image.shape

outputForHValue = np.zeros((height, width, channels), np.uint8)
outputForSValue = np.zeros((height, width, channels), np.uint8)
outputForIValue = np.zeros((height, width, channels), np.uint8)
outputForHSIValue = np.zeros((height, width, channels), np.uint8)

imageData = np.asarray(image)

# def calculateH():
#     for i in range(len(imageData)):
#         for j in range(len(imageData[0])):
#             pixel = imageData[i][j]
#             B = pixel[0]
#             G = pixel[1]
#             R = pixel[2]
#              test1 = (R-G)+(R-B)
#              if test1 > 0:
#                  test1 = test1 / 2
#              else:
#                  test1 = 1
#                  test1 = test1 / 2
#              if test1 > 0 and math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B)) > 0:
#                  test1 = test1 / math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B))
#              else:
#                  test1 = 1
#                  test1 = test1 / (math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B))+1)
#              if test1 > 0:
#                  test1 = test1/360
#              else:
#                  test1 = 1
#                  test1 = test1 / 360
#
#              hAngle = math.degrees(math.acos(test1))
#
#
#              hValue= 0
#              if B <= G:
#                  hValue = hAngle
#              elif G<B:
#                  hValue = 360-hAngle
#              else:
#                  hValue = 0
#             outputForHValue[i, j, 0] = hValue
#             outputForHValue[i, j, 1] = hValue
#             outputForHValue[i, j, 2] = hValue
#
#
# def calculateS():
#     for i in range(len(imageData)):
#         for j in range(len(imageData[0])):
#             pixel = imageData[i][j]
#             B = pixel[0]
#             G = pixel[1]
#             R = pixel[2]
#             sValue = 1-(3*min(R, G, B))
#             outputForSValue[i, j, 0] = sValue
#             outputForSValue[i, j, 1] = sValue
#             outputForSValue[i, j, 2] = sValue
#
#
# def calculateI():
#     for i in range(len(imageData)):
#         for j in range(len(imageData[0])):
#             pixel = imageData[i][j]
#             B = pixel[0]
#             G = pixel[1]
#             R = pixel[2]
#             iValue = (R+G+B)/3
#             outputForIValue[i, j, 0] = iValue
#             outputForIValue[i, j, 1] = iValue
#             outputForIValue[i, j, 2] = iValue
#
#
# calculateH()
# calculateS()
# calculateI()
#math.acos(((R - G) + (R - B) / 2) / (math.sqrt(math.pow(R - G, 2) + ((R - B) * (G - B)))))


def calculateH(R, G, B):
    test1 = (R - G) + (R - B)
    if test1 > 0:
        test1 = test1 / 2
    else:
        test1 = 1
        test1 = test1 / 2
    if test1 > 0 and math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B)) > 0:
        test1 = test1 / math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B))
    else:
        test1 = 1
        test1 = test1 / (math.sqrt(math.pow(R - G, 2) + (R - B) * (G - B)) + 1)
    if test1 > 0:
        test1 = test1 / 360
    else:
        test1 = 1
        test1 = test1 / 360

    hAngle = math.degrees(test1)
    hValue = hAngle
    # if B <= G:
    #     hValue = hAngle
    # elif G < B:
    #     hValue = 360 - hAngle
    # else:
    #     hValue = 0

    return hValue

    # if s == 0:
    #     return 0
    #
    # elif rgbMax == R:
    #     return (G-B)/(rgbMax-rgbMin)
    #
    # elif rgbMax == G:
    #     return 2.0 + (B-R)/(rgbMax-rgbMin)
    #
    # elif rgbMax == B:
    #     return 4.0 + (R-G)/(rgbMax-rgbMin)
    #
    # else:
    #     return 0


# def calculateS(i, rgbMin, rgbMax):
#     if rgbMin == rgbMax:
#         return 0
#
#     elif i < 0.5:
#         return (rgbMax-rgbMin)/(rgbMax+rgbMin)
#
#     elif i > 0.5:
#         return (rgbMax-rgbMin)/(2.0-rgbMax-rgbMin)
#
#     else:
#         return 0


def calculateHSI():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            B = pixel[0]/255
            G = pixel[1]/255
            R = pixel[2]/255

            iValue = (R+G+B)/3
            outputForIValue[i, j, 0] = iValue*255
            outputForIValue[i, j, 1] = iValue*255
            outputForIValue[i, j, 2] = iValue*255

            sValue = 1-((3*min(R, G, B))/(R+G+B))
            if np.isnan(sValue):
                sValue = np.nan_to_num(sValue)
            outputForSValue[i, j, 0] = sValue*255
            outputForSValue[i, j, 1] = sValue*255
            outputForSValue[i, j, 2] = sValue*255

            hValue = calculateH(R, G, B)
            # if hValue < 0:
            #     hValue = (hValue*60)+360
            # else:
            #     hValue = hValue*60
            outputForHValue[i, j, 0] = hValue*255
            outputForHValue[i, j, 1] = hValue*255
            outputForHValue[i, j, 2] = hValue*255

            print(hValue, sValue, iValue)

            outputForHSIValue[i, j, 0] = hValue
            outputForHSIValue[i, j, 1] = sValue*255
            outputForHSIValue[i, j, 2] = iValue*255


calculateHSI()

cv2.imwrite('outputHValue.jpg', outputForHValue)
cv2.imwrite('outputSValue.jpg', outputForSValue)
cv2.imwrite('outputIValue.jpg', outputForIValue)
cv2.imwrite('outputHSIValue.jpg', outputForHSIValue)
print('The code got to here')

#Try to implement this math http://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/
