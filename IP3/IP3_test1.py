import cv2
import numpy as np

def main():
    img = cv2.imread('rices.png', cv2.IMREAD_GRAYSCALE)
    threshold_value = 127
    img_my = threshold(img.copy(), threshold_value)
    thr_cv, img_cv = cv2.threshold(img.copy(), threshold_value, 255, cv2.THRESH_BINARY)

    print('diff : ', (img_my.astype(np.float32) - img_cv.astype(np.float32)).sum())
    
    cv2.imshow('my threshold', img_my)
    cv2.imshow('cv2 threshold', img_cv)
    cv2.waitKey()
    cv2.destroyAllWindows()


def threshold(img, thresh):
    '''
    img : image
    thresh : threshold value

    return : threshold image
    '''
    return img


if __name__=='__main__':
    main()