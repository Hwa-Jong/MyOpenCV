import cv2
import numpy as np

import os
import sys

# add path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from IP2.IP2_test1 import getHistogram

from IP3_test1 import threshold

def main():
    img = cv2.imread('rices.png', cv2.IMREAD_GRAYSCALE)

    thr_my, img_my = threshold_OTSU(img.copy())
    thr_cv, img_cv = cv2.threshold(img.copy(), -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    print('diff : ', (img_my.astype(np.float32) - img_cv.astype(np.float32)).sum())
    
    print('My  OTSU threshold value : ', thr_my)
    print('cv2 OTSU threshold value : ', thr_cv)
    cv2.imshow('my threshold', img_my)
    cv2.imshow('cv2 threshold', img_cv)
    cv2.waitKey()
    cv2.destroyAllWindows()

def threshold_OTSU(img):    
    '''
    img : image

    return : threshold value, threshold image
    '''
    level = 256
    eps = 1E-6 
    hist = getHistogram(img)
    hist_sum = hist.sum()

    c1 = np.zeros((level,), dtype=np.int32)
    c2 = np.zeros((level,), dtype=np.int32)

    o1 = np.zeros((level,), dtype=np.int32)
    o2 = np.zeros((level,), dtype=np.int32)

    muT1 = np.zeros((level,), dtype=np.float32)
    muT2 = np.zeros((level,), dtype=np.float32)

    mu1 = np.zeros((level,), dtype=np.float32)
    mu2 = np.zeros((level,), dtype=np.float32)

    sig1 = np.zeros((level,), dtype=np.float32)
    sig2 = np.zeros((level,), dtype=np.float32)  
    sigw = np.zeros((level,), dtype=np.float32)    

    img = threshold(img, thr)

    return thr, img

if __name__=='__main__':
    main()