import cv2
import numpy as np

def main():
    addTest()

def addTest():
    img = np.full((512,512), 200, dtype=np.uint8)

    img2 = np.zeros_like(img)
    img2[256:] = 56

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_add = img + img2
    cv2.imshow('add img', img_add)
    cv2.waitKey()
    cv2.destroyAllWindows()

    img_cvadd = cv2.add(img, img2)
    cv2.imshow('cv add img', img_cvadd)
    cv2.waitKey()
    cv2.destroyAllWindows()
    

if __name__ =='__main__':
    main()



