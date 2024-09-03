import cv2
import numpy as np
from IP6_1 import zero_padding
from IP6_test1 import replicate_padding
from IP6_test2 import mirror_padding


def filtering(img, kernel, padding=0, last_norm=True):
    h_org, w_org = img.shape[:2]
    
    # padding
    if padding > 0:
        img = zero_padding(img, padding)
    
    # filtering
    img = img.astype(np.float32) / 255.0
    img_filter = np.zeros_like(img, dtype=np.float32)
    
    h, w, c = img_filter.shape
    kh, kw = kernel.shape
    kh_half, kw_half = kh//2, kw//2

    print('filtering...')
    for row in range(padding, h-padding):
        for col in range(padding, w-padding):
            for ch in range(c):
                roi = img[row-kh_half:row+kw_half+1, col-kh_half:col+kw_half+1, ch]                
                value = 0
                for row_k in range(kh):
                    for col_k in range(kw):
                        value += roi[row_k, col_k] * kernel[row_k, col_k]
                
                img_filter[row, col, ch] = value
                
    img_filter = img_filter[padding:padding+h_org, padding:padding+w_org] 
    if last_norm:
        img_filter = np.clip(img_filter, 0, 1)
        img_filter = (img_filter * 255).astype(np.uint8)
                
    return img_filter

def main():
    img = cv2.imread('lena.png')
    
    kernel = np.full((3,3), 1/9)
    # kernel = np.full((3,3), 1/15)
    # kernel = np.full((3,3), 1/5)
    
    # kernel = np.full((9,9), 1/81)
    
    image_filt = filtering(img, kernel, padding=kernel.shape[0]//2)

    cv2.imshow('image', img)
    cv2.imshow('image_filt', image_filt)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
