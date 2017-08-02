import cv2

img = None

def onMouse(event, x, y, flags, param):
    img2 = img.copy()
    text = '{0}, {1}'.format(x, y)
    cv2.putText(img2, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0))
    cv2.imshow('Image', img2)

img = cv2.imread('../FaceCourse_py3/cv4facesCode/data/images/hillary_clinton.jpg')
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', onMouse, img)
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyWindow('Image')

