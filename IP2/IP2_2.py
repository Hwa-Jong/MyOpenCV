import cv2
import numpy as np

def main():
    img_org = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
    img_div5 = img_org.astype(np.float32)
    img_div5 = img_div5 / 5
    #img_div5 = cv2.divide(img_div5, 5)
    img_div5 = np.clip(img_div5, 0, 255)
    
    img_mul2 = img_org.astype(np.float32)
    img_mul2 = img_mul2 * 2
    #img_mul2 = cv2.multiply(img_mul2, 2)
    img_mul2 = np.clip(img_mul2, 0, 255)
    
    img_trunc = img_org.astype(np.float32)
    img_trunc = img_trunc / 2 + 64
    img_trunc = np.clip(img_trunc, 0, 255)

    cv2.imshow('image org', img_org)
    cv2.imshow('image / 5', img_div5.astype(np.uint8))
    cv2.imshow('image * 2', img_mul2.astype(np.uint8))
    cv2.imshow('image / 5 + 64', img_trunc.astype(np.uint8))
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__=='__main__':
    main()