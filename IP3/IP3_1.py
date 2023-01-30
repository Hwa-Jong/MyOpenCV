import cv2
import numpy as np

def main():
    img_127 = np.full((256,256), 127, dtype=np.uint8)
    img_128 = np.full((256,256), 128, dtype=np.uint8)
    thr, img_127 = cv2.threshold(img_127, 127, 255, cv2.THRESH_BINARY)
    thr, img_128 = cv2.threshold(img_128, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('img_127', img_127)
    cv2.imshow('img_128', img_128)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__=='__main__':
    main()