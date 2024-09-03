import cv2
import numpy as np
from IP6_2 import filtering

def get_box_kernel(size):
    kernel = np.full((size,size), 1/(size**2))
    return kernel

def calc_gaussian_value(x, y, sigma):
    return 1/(2*np.pi*(sigma*sigma)) * np.exp( - ((x*x + y*y) / (2*(sigma*sigma))) )

def get_gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size))
    
    h, w = kernel.shape
    
    for row in range(h):
        for col in range(w):
            y = row - h//2
            x = col - w//2
            kernel[row, col] = calc_gaussian_value(x, y, sigma)
            
    kernel = kernel / kernel.sum()
    
    return kernel

def get_sharpening_kernel(size):
    kernel = np.full((size, size), -1.0)
    kernel[size//2, size//2] = (size * size)
    return kernel

def get_sobel_filter():
    gx = np.array([ [-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1] ])
    
    gy = np.array([ [-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1] ])
    
    return gx, gy

def main():
    img = cv2.imread('lena.png')
    kernel_size = 3
    # kernel = get_box_kernel(kernel_size)
    kernel = get_gaussian_kernel(kernel_size, 1.0)
    # kernel = get_sharpening_kernel(kernel_size)
    image_filt = filtering(img, kernel, padding=kernel_size//2)

    # sobel_x, sobel_y = get_sobel_filter()
    # image_filt_x = filtering(img, sobel_x, padding=sobel_x.shape[0]//2, last_norm=False)
    # image_filt_y = filtering(img, sobel_y, padding=sobel_y.shape[0]//2, last_norm=False)
        
    # image_filt = np.abs(image_filt_x + image_filt_y)
    # image_filt = np.clip(image_filt, 0, 1)
    # image_filt = (image_filt * 255).astype(np.uint8)
    
    cv2.imshow('image', img)
    cv2.imshow('image_filt', image_filt)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
