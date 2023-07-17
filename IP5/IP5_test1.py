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

    img_ero = cv2.erode(img, kernel)
    viewer_ero = cv2.resize(img_ero, dsize=(256,256), interpolation=cv2.INTER_NEAREST)

    img_dil = cv2.dilate(img, kernel)
    viewer_dil = cv2.resize(img_dil, dsize=(256,256), interpolation=cv2.INTER_NEAREST)

    img_opening = opening(img, kernel)
    img_closing = closing(img, kernel)
    viewer_opening = cv2.resize(img_opening, dsize=(256,256), interpolation=cv2.INTER_NEAREST)
    viewer_closing = cv2.resize(img_closing, dsize=(256,256), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('image', viewer)
    cv2.imshow('image erosion', viewer_ero)
    cv2.imshow('image dilation', viewer_dil)
    cv2.imshow('image opening', viewer_opening)
    cv2.imshow('image closing', viewer_closing)
    cv2.waitKey()
    cv2.destroyAllWindows()

def opening(img, kernel):
    # erode -> dilate
    img_ero = erode(img, kernel)
    img_opening = dilate(img_ero, kernel)
    return img_opening

def closing(img, kernel):
    # dilate -> erode
    img_dil = dilate(img, kernel)
    img_closing = erode(img_dil, kernel)
    return img_closing

def erode(img, kernel):
    dst = np.zeros_like(img)
    h, w = img.shape
    h_k, w_k = kernel.shape

    h_res = h_k//2
    w_res = w_k//2

    for row in range(h_res, h-h_res):
        for col in range(w_res, w-w_res):
            pass

    return dst

def dilate(img, kernel):
    dst = np.zeros_like(img)
    h, w = img.shape
    h_k, w_k = kernel.shape

    h_res = h_k//2
    w_res = w_k//2

    for row in range(h_res, h-h_res):
        for col in range(w_res, w-w_res):
            pass

    return dst

if __name__ =='__main__':
    main()