import cv2
import numpy as np

def main():
    img = cv2.imread('lena.png')
    cv2.imshow('original img', img)

    gray = BGR2Gray1(img)
    cv2.imshow('gray img', gray.astype(np.uint8))

    cv2.waitKey()
    cv2.destroyAllWindows()

def BGR2Gray1(img):
    #img = img.astype(np.float32)
    gray = (img[..., 0] + img[..., 1] + img[..., 2]) / 3
    return gray

def BGR2Gray2(img):
    gray = img[..., 0]
    return gray

def BGR2Gray3(img):
    gray = img[..., 1]
    return gray

def BGR2Gray4(img):
    gray = img[..., 2]
    return gray

if __name__ =='__main__':
    main()



