import cv2

def main():
    #img = cv2.imread('lena.png')
    img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

    cv2.imshow('image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ =='__main__':
    main()



