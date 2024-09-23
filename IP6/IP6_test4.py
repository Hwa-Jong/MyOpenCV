import cv2
import numpy as np
from IP6_2 import filtering

def get_gaussian_kernel(size, sigma):
    # hint : np.arange, np.reshape, np.tile
    x = 
    y = 
    
    kernel = 
    kernel = kernel / kernel.sum()
    
    return kernel

def main():
    img = cv2.imread('lena.png')
    kernel_size = 3
    kernel = get_gaussian_kernel(kernel_size, 1.0)
    image_filt = filtering(img, kernel, padding=kernel_size//2)
    
    cv2.imshow('image', img)
    cv2.imshow('image_filt', image_filt)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
