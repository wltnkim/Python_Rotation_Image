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
    for i in range(0, 361, 90):
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2,num_rows/2), i, 1)
        img_rotation = cv2.warpAffine(img,rotation_matrix,(num_cols,num_rows))

        filename = folder_directory + "/"+ str(input_filename) + "_" + str(i) + ".jpg"
        cv2.imwrite(filename, img_rotation)
