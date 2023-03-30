import cv2
import numpy as np

def main():
    img = cv2.imread('lena.png')
    
    #noisy_img = getUniformNoiseImg(img, strength=50)
    noisy_img = getGaussianNoiseImg(img, mu=0.0, sig=50.0)

    cv2.imshow('Original Image', img)
    cv2.imshow('Noisy Image', noisy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getUniformNoiseImg(img, strength):
    uniform_noize = np.random.uniform(low=-strength, high=strength, size=img.shape)
    noisy_img = np.clip(img + uniform_noize, 0, 255).astype(np.uint8)
    return noisy_img

def getGaussianNoiseImg(img, mu=0.0, sig=1.0):
    uniform_noize = np.random.normal(mu,sig, size=img.shape)
    noisy_img = np.clip(img + uniform_noize, 0, 255).astype(np.uint8)
    return noisy_img


if __name__=='__main__':
    main()