import cv2


img = cv2.imread('img/bus.jpg')
num_rows,num_cols = img.shape[:2]
for i in range(1, 361):
    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2,num_rows/2), i, 1) # 가운데를 중심점으로 30도 돌리고 스케일 요소 0.7
    img_rotation = cv2.warpAffine(img,rotation_matrix,(num_cols,num_rows))
    cv2.imwrite("img/result/rotate_img" + str(i) + ".jpg", img_rotation)

#cv2.imshow("Rotate result", img_rotation)
#cv2.waitKey(0)

