import cv2
import numpy as np

import matplotlib.pyplot as plt
from IP2_test1 import histStretching

def main():
    img_org = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
    img_dark = cv2.divide(img_org, 5)

    img_stretch = histStretching(img_dark)
    img_stretch = img_stretch.astype(np.uint8)

    img_equal, hist_equal = histEqualization(img_dark)

    x = np.arange(0, 256)
    
    plt.figure(figsize=(12,6))

    plt.subplot(2,3,1)
    plt.imshow(img_dark, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    plt.subplot(2,3,2)
    plt.imshow(img_stretch, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    plt.subplot(2,3,3)
    plt.imshow(img_equal, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    plt.subplot(2,3,4)
    y = getHistogram(img_dark)
    plt.bar(x, y, width=1)

    plt.subplot(2,3,5)
    y = getHistogram(img_stretch)
    plt.bar(x, y, width=1)

    plt.subplot(2,3,6)
    plt.bar(x, hist_equal, width=1)

    plt.show()

def histEqualization(img, max_intensity = 255):
    # calculate histogram
    hist = getHistogram(img, max_intensity)

    # calculate cumulative histogram 
    # don't use np.cumsum
    hist_cum = cumsum(hist)

    # divide cumulative value
    hist_norm = 'ToDo'

    # equalize histogram
    hist_equal = 'ToDo'

    # apply equalization    
    img_equal = 'ToDo'

    return img_equal, hist_equal

def cumsum(hist):
    """
    [input]
    hist : histogram 1D array ( shape : (256,) )

    [output]
    hist_c : Accumulated histogram 1D array ( shape : (256,) )
    """

    return hist_c

def getHistogram(img, max_intensity=255):
    """
    [input]
    img : image
    max_intensity : max intensity( default : 255 )

    [output]
    hist : histogram 1D array ( shape : (256,) )
    """

    return hist



if __name__=='__main__':
    main()