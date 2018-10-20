import math
import numpy as np
import cv2

# This code converts RGB to HSI using the method and math discussed in the IP book:
# Introduction to Video and Image Processing by Thomas B. Moeslund, Appendix D: Conversion Between RGB and HSI

# Here the code imports the image that the algorithm will use.
image = cv2.imread("flowers.jpg")
# The dimensions of the image is stored in different variables
height, width, channels = image.shape

# Three empty arrays are made, for the output images
outputForHValueBook = np.zeros((height, width, channels), np.uint64)
outputForSValueBook = np.zeros((height, width, channels), np.uint64)
outputForIValueBook = np.zeros((height, width, channels), np.uint64)
outputForHSIValueBook = np.zeros((height, width, channels), np.uint64)

# The data from the imported image is stored in a numpy array
imageData = np.asarray(image)


# This function calculates the Hue in the HSI color space
def calculateHBook(R, G, B):
    # Here the code will try to perform the calculation of the theta, but if an error happens, like a division by zero
    # the code will set the theta to 0 and move on.
    try:
        # The math(from the book) for calculating the theta is implemented in this line of code.
        hAngle = math.degrees(math.acos(0.5 * (((R - G) + (R - B)) / math.sqrt((R - G) * (R - G) + (R - B) * (G - B)))))
    except:
        hAngle = 0

    # Here the code checks the value of the Blue and the green channel, this will have an effect on the final Hue value
    hValue = 0
    if B <= G:
        hValue = hAngle
    else:
        hValue = 360 - hAngle
    return hValue


# This is the main function in the programme, this converts the RGB values to HSI
def calculateHSIBook():
    # This nested for-loop goes through the columns and rows of the imported image
    # The i value goes through the rows and the j value each of the columns in the i rows
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):

            # The color values are imported for each pixel in the loop
            pixel = imageData[i][j]
            B = float(pixel[0] / 255)
            G = float(pixel[1] / 255)
            R = float(pixel[2] / 255)

            # Here the Intensity is calculated, and put into the output image, in grey scale.
            iValue = (R + G + B) / 3.0
            outputForIValueBook[i, j, 0] = iValue * 255
            outputForIValueBook[i, j, 1] = iValue * 255
            outputForIValueBook[i, j, 2] = iValue * 255

            # Here the Saturation is calculated, and the value is them again put into the output image, in grey scale
            try:  # Another try, in case of division by zero errors
                sValue = 1.0 - (3.0 * ((min(R, G, B)) / (R + G + B)))
            except:
                sValue = 0

            outputForSValueBook[i, j, 0] = sValue * 255
            outputForSValueBook[i, j, 1] = sValue * 255
            outputForSValueBook[i, j, 2] = sValue * 255

            # Here the Hue is calculated, simply by calling the previously declared function, with the current pixels
            # RGB values. The calculated values are once again put into the output image in grey scale.
            try:  # Another try, in case of division by zero errors
                hValue = calculateHBook(R, G, B)
            except:
                hValue = 0
            outputForHValueBook[i, j, 0] = (hValue / 360) * 255
            outputForHValueBook[i, j, 1] = (hValue / 360) * 255
            outputForHValueBook[i, j, 2] = (hValue / 360) * 255

            # Here the HSI values are put into the same output image, this has no real purpose,
            # and is mostly just interesting to look at :)
            outputForHSIValueBook[i, j, 0] = (hValue / 360) * 255
            outputForHSIValueBook[i, j, 1] = sValue * 255
            outputForHSIValueBook[i, j, 2] = iValue * 255


# The main function is called
calculateHSIBook()

# The the previously blank images are saved to the hard drive and can now be view outside this programme
cv2.imwrite('outputHValueBook.jpg', outputForHValueBook)
cv2.imwrite('outputSValueBook.jpg', outputForSValueBook)
cv2.imwrite('outputIValueBook.jpg', outputForIValueBook)
cv2.imwrite('outputHSIValueBook.jpg', outputForHSIValueBook)

# Simple debug message
print('The code from the book completed')

# Try to implement this math http://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/
# Some problems may be the fact that it does not work with pure black and white
