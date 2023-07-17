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

    img_dil = cv2.dilate(img, kernel)
    viewer_dil = cv2.resize(img_dil, dsize=(256,256), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('image', viewer)
    cv2.imshow('image dilation', viewer_dil)
    cv2.waitKey()
    cv2.destroyAllWindows()



    



if __name__ =='__main__':
    main()