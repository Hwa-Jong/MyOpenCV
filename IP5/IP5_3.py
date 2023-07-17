import cv2
import numpy as np

def main():
    img = [
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,1,1,1,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,1,0],
    ]
    img = np.array(img, dtype=np.uint8)*255

    viewer = cv2.resize(img, dsize=(256,256), interpolation=cv2.INTER_NEAREST)

    kernel = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1],
    ], dtype=np.uint8) * 255

    img_opening = opening(img, kernel)
    img_closing = closing(img, kernel)
    viewer_opening = cv2.resize(img_opening, dsize=(256,256), interpolation=cv2.INTER_NEAREST)
    viewer_closing = cv2.resize(img_closing, dsize=(256,256), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('image', viewer)
    cv2.imshow('image opening', viewer_opening)
    cv2.imshow('image closing', viewer_closing)
    cv2.waitKey()
    cv2.destroyAllWindows()


def opening(img, kernel):
    # erode -> dilate
    img_ero = cv2.erode(img, kernel)
    img_opening = cv2.dilate(img_ero, kernel)
    return img_opening


def closing(img, kernel):
    # dilate -> erode
    img_dil = cv2.dilate(img, kernel)
    img_closing = cv2.erode(img_dil, kernel)
    return img_closing

    



if __name__ =='__main__':
    main()