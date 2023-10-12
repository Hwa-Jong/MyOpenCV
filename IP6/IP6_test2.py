import cv2
import numpy as np

def mirror_padding(img, pad):
    return img_pad

def main():
    img = cv2.imread('lena.png')
    img_pad = mirror_padding(img, 50)

    cv2.imshow('image', img)
    cv2.imshow('image_pad', img_pad)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
