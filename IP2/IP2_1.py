import cv2
import numpy as np

def main():
    img_uint8 = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
    img_float32 = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE).astype(np.float32)

    cv2.imshow('image uint8', img_uint8)
    cv2.imshow('image float32', img_float32)
    cv2.imshow('image float32 / 255', img_float32/255)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__=='__main__':
    main()