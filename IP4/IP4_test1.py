import cv2
import numpy as np

from IP4_2 import  getGaussianNoiseImg

def main():
    img = cv2.imread('lena.png')
    
    noisy_imgs = []
    for i in range(24):
        noisy_imgs.append(getGaussianNoiseImg(img, mu=0.0, sig=50.0))

    denoising = gaussianNoiseReduction(noisy_imgs)

    cv2.imshow('Original Image', img)
    cv2.imshow('Noisy Image', noisy_imgs[0])
    cv2.imshow('Noise Reduction', denoising)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gaussianNoiseReduction(noisy_imgs):
    imgs = np.array(noisy_imgs)
    # Todo
    imgs = 
    return imgs.astype(np.uint8)
    



if __name__=='__main__':
    main()