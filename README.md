# PanoramaStitching

Computer Vision Project Idea – Have you ever use the panorama mode in your smartphones?
Once you dive into computer vision, then you can build your own panorama app and it is very interesting to understand how panorama works.

Input images:

![alt text](images/pair1/1.jpg)
![alt text](images/pair1/2.jpg)


### 1. StitcherStandart.py  -> cv2.Stitcher().create(cv2.STITCHER_PANORAMA) 
#### Results

Output image:

![alt text](images/results/pano_pair1.jpg)


### 2. SIFTStitcher.py  -> Stitch with Keypoints from SIFT, then findHomography and warpPerspective
#### Results


Output image:

![alt text](images/results/panorama.jpg)
![alt text](images/results/matching.jpg)
