import cv2
import numpy as np

from IP4_3 import  getSaltNPepperNoise

def main():
    img = cv2.imread('lena.png')
    
    noisy_img = getSaltNPepperNoise(img, 0.05)

    denoising = SaltNPepperNoiseReduction(noisy_img)

    cv2.imshow('Original Image', img)
    cv2.imshow('Noisy Image', noisy_img)
    cv2.imshow('Noise Reduction', denoising)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def SaltNPepperNoiseReduction(noisy_imgs):
    h, w, c = noisy_imgs.shape
    denoising = noisy_imgs.copy()

    for row in range(1, h-1):
        print('\r%03d%%...'%(int(row/(h-2)*100)), end='')
        for col in range(1, w-1):
            # Todo
            denoising = 
    return denoising



if __name__=='__main__':
    main()