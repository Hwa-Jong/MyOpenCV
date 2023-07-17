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

    cv2.imshow('image', viewer)
    cv2.imshow('image erosion', viewer_ero)
    cv2.waitKey()
    cv2.destroyAllWindows()



    



if __name__ =='__main__':
    main()