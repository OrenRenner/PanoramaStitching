import cv2
import numpy as np
import os

images_path = os.listdir("images/pair1")
image_list = []

for im in images_path:
    img = cv2.imread(f'images/pair1/{im}')
    image_list.append(img)

stitcher = cv2.Stitcher().create(cv2.STITCHER_PANORAMA)
status, pano = stitcher.stitch(image_list)

if status is cv2.STITCHER_OK:
    cv2.namedWindow("Pano", 0)
    cv2.imshow("Pano", pano)
    cv2.waitKey(0)
    cv2.imwrite("images/results/pano_pair1.jpg", pano)
