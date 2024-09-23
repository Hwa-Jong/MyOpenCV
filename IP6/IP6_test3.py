import cv2
import numpy as np
from IP6_1 import zero_padding
from IP6_test1 import replicate_padding
from IP6_test2 import mirror_padding
from IP6_2 import filtering as filtering_old


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
    kernel = kernel[..., np.newaxis]
    kh_half, kw_half = kh//2, kw//2

    print('filtering...')
    for row in range(padding, h-padding):
        for col in range(padding, w-padding):
            img_filter[row, col] = 
                
    img_filter = img_filter[padding:padding+h_org, padding:padding+w_org] 
    if last_norm:
        img_filter = np.clip(img_filter, 0, 1)
        img_filter = (img_filter * 255).astype(np.uint8)
                
    return img_filter

def main():
    img = cv2.imread('lena.png')
    
    kernel = np.full((3,3), 1/9)
    
    #image_filt = filtering(img, kernel, padding=kernel.shape[0]//2)
    image_filt = filtering_old(img, kernel, padding=kernel.shape[0]//2)

    cv2.imshow('image', img)
    cv2.imshow('image_filt', image_filt)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
