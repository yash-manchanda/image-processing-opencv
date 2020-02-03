import cv2

# Loading images
image =cv2.imread('images/people.jpeg')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey image', grey)
print(grey.shape)
cv2.waitKey()

temp = cv2.imread('images/find.jpeg',0)
cv2.imshow('target',temp)
cv2.waitKey()
dsize = temp.shape
print(dsize)
 
# changing the pixels of image
# can do with the same too.

resize = cv2.resize(temp, dsize, interpolation = cv2.INTER_CUBIC)
cv2.imshow('resizee',resize)
cv2.waitKey()
print(resize.shape)

# matching template and storing all the pixel points
res = cv2.matchTemplate(grey,resize,cv2.TM_CCOEFF)

min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)
# print(min_val)
# print(max_val)
# print(min_loc)
# print(max_loc)

# Setting the size of rectangle in which the image will be shown
down = max_loc[0]-100, max_loc[1]+100
cv2.rectangle(image,max_loc, down , (255,0,0) , 2)

cv2.imshow('object found',image)
cv2.waitKey(0)

cv2.destroyAllWindows() 