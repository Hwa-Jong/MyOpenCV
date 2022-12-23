import cv2
import numpy as np

import matplotlib.pyplot as plt

def main():
    img_org = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
    img_dark = cv2.divide(img_org, 5)

    img_stretching = histStretching(img_dark)
    img_stretching = img_stretching.astype(np.uint8)

    x = np.arange(0, 256)
    
    plt.figure(figsize=(12,6))

    plt.subplot(2,3,1)
    plt.imshow(img_org, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    plt.subplot(2,3,2)
    plt.imshow(img_dark, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    plt.subplot(2,3,3)
    plt.imshow(img_stretching, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    plt.subplot(2,3,4)
    y = getHistogram(img_org)
    plt.bar(x, y, width=1)

    plt.subplot(2,3,5)
    y = getHistogram(img_dark)
    plt.bar(x, y, width=1)

    plt.subplot(2,3,6)
    y = getHistogram(img_stretching)
    plt.bar(x, y, width=1)

    plt.show()

def histStretching(img):    
    """
    [input]
    img : image

    [output]
    img : stretched image
    """
    return img

def getHistogram(img):
    """
    [input]
    img : image

    [output]
    hist : histogram 1D array ( shape : (256,) )
    """
    return hist

if __name__=='__main__':
    main()