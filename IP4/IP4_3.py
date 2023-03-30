import cv2
import numpy as np

def main():
    img = cv2.imread('lena.png')

    rate = 0.05
    noisy_img = getSaltNPepperNoise(img, rate)
    
    cv2.imshow('Original Image', img)
    cv2.imshow('Noisy Image', noisy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getSaltNPepperNoise(img, rate):    
    noise = np.random.uniform(0, 1, size=img.shape[:2])

    pepper = noise < rate
    salt = noise > 1-rate

    noisy_img = img.copy()
    noisy_img[pepper] = 0
    noisy_img[salt] = 255
    return noisy_img



if __name__=='__main__':
    main()