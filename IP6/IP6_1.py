import cv2
import numpy as np

def zero_padding(img, pad):
    h, w, c = img.shape
    img_pad =np.zeros((h+pad*2, w+pad*2, c), dtype=img.dtype)

    img_pad[pad:pad+h, pad:pad+w] = img
    return img_pad

def main():
    img = cv2.imread('lena.png')
    img_pad = zero_padding(img, 50)

    cv2.imshow('image', img)
    cv2.imshow('image_pad', img_pad)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
