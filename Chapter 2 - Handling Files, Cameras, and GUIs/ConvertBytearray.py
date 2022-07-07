import cv2
import numpy
import os

# Make an arry of 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400x300 grayscale image
#grayImage = flatNumpyArray.reshape(300, 400)
#grayImage = numpy.random.randint(0, 256, 120000).reshape(300, 400) #THIS IS AN ALTERNATIVE FOR THE BYTEARRAY OPTION ABOVE
cv2.imwrite('RandomGray.png', grayImage)

# Convert the array to make a 400x100 color image
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage) 
