# Improved Median Filtering for Noise Reduction with Python

Although the median filter is suitable for eliminating noise in images, it is an expensive algorithm in processing time. This repository aims to try new, fast median filtering algorithms developed in the paper named ["An Improved Median Filtering Algorithm for Image Noise Reduction" by Youlian Zhu and Cheng Huang](https://www.sciencedirect.com/science/article/pii/S1875389212005494).

For now, I wrote a median filter from scratch without using any image manipulation library (other than image loading and display). It was slow at first, but later on, using the "concurrent.futures" library and setting the code to run on multiprocessors, I increased the speed of the code by 4x. Of course, it still doesn't work as fast as a cv2.medianBlur, but it's honest work, and I'm still working on it. I'm also planning to implement the algorithms in Youlian Zhu and Cheng Huang's paper very soon.

Here is an example:

![3x3](https://user-images.githubusercontent.com/42466646/160256800-2ca35a2d-c6e5-4790-8426-0ff132338188.png)
