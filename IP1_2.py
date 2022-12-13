import cv2
import numpy as np

def main():
    showOverflow()
    showUnderflow()

def showOverflow():
    img = np.full((512,512), 255, dtype=np.uint8)
    cv2.imshow('255 image', img)

    cv2.waitKey()
    cv2.destroyAllWindows()

    img_over = img + 1
    cv2.imshow('overflow image', img_over)

    cv2.waitKey()
    cv2.destroyAllWindows()

def showUnderflow():
    img = np.zeros((512,512), dtype=np.uint8)
    cv2.imshow('zero image', img)

    cv2.waitKey()
    cv2.destroyAllWindows()

    img_under = img - 1
    cv2.imshow('underflow image', img_under)

    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ =='__main__':
    main()



