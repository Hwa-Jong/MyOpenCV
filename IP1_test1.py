import cv2
import numpy as np

def main():
    img = cv2.imread('lena.png')
    cv2.imshow('original img', img)

    gray = BGR2Gray(img)
    cv2.imshow('gray img', gray.astype(np.uint8))

    cv2.waitKey()
    cv2.destroyAllWindows()

def BGR2Gray(img):
    """
    [input]
    img : color image

    [output]
    gray : gray image
    """
    
    return gray
    
if __name__ =='__main__':
    main()



