import cv2

img = cv2.imread('dices.png')

img[0, 0] = [255, 255, 255] #accessing pixel at [0,0] (top left corner) and setting it to white

img.itemset((120, 120, 0), 255) #accessing pixel at [120,120] and setting the blue channel [0] to 255. 
                                #It is important to note that the order of the parameters is [y, x, channel], and the channels are BGR. 

#itemset is faster than accessing individual pixels as I did in the previous snippet

img[:, :, 1] = 0 #accessing all pixels from the image and setting the green channel [1] to 0. 
                 #I'm using array slicing to do this, which is more efficient than accessing individual pixels.

my_roi = img[50:100, 0:100] #accessing a region of interest (ROI) from the image, also using the array slicing method.
img[30:80, 10:110] = my_roi

print(img.shape) #shape: describes the shape of the array. It contains (in order) the height, width, and the number of channels (for colorful images). 
                 #For grayscale images, the len(shape) == 2, whereas for colorful images is len(shape) == 3.

print(img.size) #size: describes the number of elements in the array. 
                #For grayscale images, this is the number of pixels. For colorful images, this is the number of pixels times the number of channels.

print(img.dtype) #dtype: describes the data type of the array. For an 8-bit-per-channel image, the datatype is numpy.uint8.

cv2.imshow("image",img)
cv2.waitKey(0)