import cv2


image =cv2.imread('images/img1.jpeg')
print(image.shape)
cv2.imshow('images/hello world',image)
cv2.waitKey()

#Showing nuber of pixels 
print(image.shape[0] * image.shape[1],'pixels')

#creating and saving new image 
cv2.imwrite('output.jpeg', image)

#grey_scale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grey.shape)
cv2.imshow('grey image', grey)
cv2.waitKey()

#converting image to hsv format
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image',hsv_image)

#creating various format of images with hsv image
cv2.imshow('Hue channel',hsv_image[:,:,0])
cv2.imshow('saturation channel',hsv_image[:,:,1])
cv2.imshow('value channel',hsv_image[:,:,2])
cv2.waitKey()


#splitting all colours into RBG:
B,G,R=cv2.split(image)
cv2.imshow("Red",R)
cv2.waitKey()
cv2.imshow("Green",G)
cv2.waitKey()
cv2.imshow("Blue",B)
cv2.waitKey()
merged=cv2.merge([B,G,R])
cv2.imshow("merged",merged)
cv2.waitKey()
cv2.destroyAllWindows()
