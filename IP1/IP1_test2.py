import cv2
import numpy as np

def main():
    img = cv2.imread('lena.png')
    cv2.imshow('original img', img)

    red = BGR2Red(img.copy())
    cv2.imshow('red img', red)

    green = BGR2Green(img.copy())
    cv2.imshow('green img', green)

    blue = BGR2Blue(img.copy())
    cv2.imshow('blue img', blue)

    cv2.waitKey()
    cv2.destroyAllWindows()

def BGR2Red(img):
    """
    [input]
    img : color image

    [output]
    img : red image
    """
    
    return img

def BGR2Green(img):
    """
    [input]
    img : color image

    [output]
    img : green image
    """
    
    return img

def BGR2Blue(img):
    """
    [input]
    img : color image

    [output]
    img : blue image
    """
    
    return img
    
if __name__ =='__main__':
    main()



