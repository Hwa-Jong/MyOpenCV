import cv2
import numpy as np
from IP6_3 import get_gaussian_kernel, get_sharpening_kernel, get_sobel_filter

def normalize(filter):
    filter -= filter.min()
    filter /= filter.max()
    filter *= 1
    return filter

def show_filter_2d(filter, norm=False):
    if norm:
        filter = normalize(filter)    
    cv2.imshow('show filter', filter)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
# pip install matplotlib
def show_filter_3d(filter, norm=False):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    if norm:
        filter = normalize(filter)
        
    # 3D 플롯 설정
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 그래프 그리기
    h, w = filter.shape[:2]
    x, y = np.meshgrid(range(w), range(h))
    ax.plot_surface(x, y, filter, cmap='viridis')

    # 그래프 보여주기
    plt.show()

def main():
    kernel_size = 3
    kernel = get_gaussian_kernel(kernel_size, 1.0)    
    show_filter_2d(kernel)
    
    # kernel_resize = cv2.resize(kernel, (300, 300), interpolation=cv2.INTER_NEAREST)
    # show_filter_2d(kernel_resize)
    
    # kernel_resize = cv2.resize(kernel, (300, 300))
    # show_filter_2d(kernel_resize, norm=True)
    
    # kernel_size = 300
    # kernel_large = get_gaussian_kernel(kernel_size, 1.0)    
    # show_filter_2d(kernel_large)
    
    # show_filter_2d(kernel_large, norm=True)
    
    # kernel_large = get_gaussian_kernel(kernel_size, 50.0)        
    # show_filter_2d(kernel_large, norm=True)
    
    # pip install matplotlib
    # kernel_size = 300
    # kernel_3d = get_gaussian_kernel(kernel_size, 50.0)    
    # show_filter_3d(kernel_3d)
    
    
    # kernel_size = 11
    # kernel = get_sharpening_kernel(kernel_size)
    # # kernel = np.array([[0, -1, 0],
    # #                    [-1, 5, -1],
    # #                    [0, -1, 0],])
    # show_filter_2d(kernel)
    # show_filter_3d(kernel)

if __name__ =='__main__':
    main()
