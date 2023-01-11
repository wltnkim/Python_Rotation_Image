import cv2
import glob
import os

input_files = glob.glob('img/*.jpg')

for input_file in input_files:
    input_filename = input_file[4:-4]
    img = cv2.imread(input_file)

    folder_directory = "result/" + str(input_filename)
    if not os.path.exists(folder_directory):
        os.makedirs(folder_directory)


    num_rows,num_cols = img.shape[:2]
    for i in range(1, 361):
        #print(input_file, i)
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2,num_rows/2), i, 1)
        img_rotation = cv2.warpAffine(img,rotation_matrix,(num_cols,num_rows))


        filename = folder_directory + "/"+ str(input_filename) + "_" + str(i) + ".jpg"
        #print(filename)
        cv2.imwrite(filename, img_rotation)

'''
for i in range(1, 361):
    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2,num_rows/2), i, 1)
    img_rotation = cv2.warpAffine(img,rotation_matrix,(num_cols,num_rows))
    cv2.imwrite("result/rotate_img" + str(i) + ".jpg", img_rotation)
'''
#cv2.imshow("Rotate result", img_rotation)
#cv2.waitKey(0)

