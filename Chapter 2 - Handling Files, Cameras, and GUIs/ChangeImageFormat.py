import cv2

#image = cv2.imread('dices.png')
#cv2.imwrite('new_image.jpg', image)
image = cv2.imread('dices.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('my_dices.png', image)
