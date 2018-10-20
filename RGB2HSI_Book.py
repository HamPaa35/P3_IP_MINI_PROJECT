import math

import numpy as np
import cv2

image = cv2.imread("flowers.jpg")
height, width,  channels = image.shape

outputForHValueBook = np.zeros((height, width, channels), np.uint64)
outputForSValueBook = np.zeros((height, width, channels), np.uint64)
outputForIValueBook = np.zeros((height, width, channels), np.uint64)
outputForHSIValueBook = np.zeros((height, width, channels), np.uint64)

imageData = np.asarray(image)

def calculateHBook(R, G, B):
    try:
        hAngle = math.degrees(math.acos(0.5 * (((R - G) + (R - B)) / math.sqrt((R-G)*(R-G) + (R - B) * (G - B)))))
    except:
        hAngle = 0
    # if hAngle < 0:
    #     hAngle *= -1

    hValue = 0
    if B <= G:
        hValue = hAngle
    else:
        hValue = 360 - hAngle
    print(hAngle, hValue)
    return hValue
    #thetaBeforeCos = (0.5 * (((R - G) + (R - B)) / math.sqrt((R-G)*(R-G) + (R - B) * (G - B))))

    #hAngle = 0

    # if thetaBeforeCos > 1:
    #     hAngle = math.degrees(math.acos(thetaBeforeCos))
    #
    # elif thetaBeforeCos < -1:
    #     hAngle = math.degrees(math.acos(thetaBeforeCos))
    #
    # else:
    #     hAngle = math.degrees(math.acos(thetaBeforeCos))

    #if R<0 and G<0 and B<0 or R>1 and G>1 and B>1:
    #    return 0
    #else:

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


def calculateHSIBook():
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):
            pixel = imageData[i][j]
            B = float(pixel[0]/255)
            G = float(pixel[1]/255)
            R = float(pixel[2]/255)

            iValue = (R+G+B)/3.0
            outputForIValueBook[i, j, 0] = iValue * 255
            outputForIValueBook[i, j, 1] = iValue * 255
            outputForIValueBook[i, j, 2] = iValue * 255

            try:
                sValue = 1.0-(3.0*((min(R, G, B))/(R+G+B)))
            except:
                sValue = 0
            print(sValue)
            outputForSValueBook[i, j, 0] = sValue * 255
            outputForSValueBook[i, j, 1] = sValue * 255
            outputForSValueBook[i, j, 2] = sValue * 255

            try:
                hValue = calculateHBook(R, G, B)
            except:
                hValue=0
            # if hValue < 0:
            #     hValue = (hValue*60)+360
            # else:
            #     hValue = hValue*60
            #if np.isnan(hValue):
            #    hValue = 0
            outputForHValueBook[i, j, 0] = (hValue / 360) * 255
            outputForHValueBook[i, j, 1] = (hValue / 360) * 255
            outputForHValueBook[i, j, 2] = (hValue / 360) * 255

            #print(hValue, sValue, iValue)

            outputForHSIValueBook[i, j, 0] = (hValue / 360) * 255
            outputForHSIValueBook[i, j, 1] = sValue * 255
            outputForHSIValueBook[i, j, 2] = iValue * 255


calculateHSIBook()

cv2.imwrite('outputHValueBook.jpg', outputForHValueBook)
cv2.imwrite('outputSValueBook.jpg', outputForSValueBook)
cv2.imwrite('outputIValueBook.jpg', outputForIValueBook)
cv2.imwrite('outputHSIValueBook.jpg', outputForHSIValueBook)
print('The code completed book')

#Try to implement this math http://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/
# Some problems may be the fact that it does not work with pure balck and white


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


