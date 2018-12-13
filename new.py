

import cv2
img_data=cv2.imread('deepu.jpeg')
print (img_data)
cv2.imwrite('newd.jpeg',img_data-30)
cv2.imshow('qwe',img_data-30)
cv2.waitKey(0)
cv2.destroyAllWindows()

