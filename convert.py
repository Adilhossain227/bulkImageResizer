import cv2
x=1
i=501
new_width = 481
new_height = 321
dim = (new_width, new_height)
while(x<i):
	img = cv2.imread("test/"+str(x)+".jpg", cv2.IMREAD_UNCHANGED)
	dresized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite('trainx/'+str(x)+'.jpg', dresized)
	x=x+1
