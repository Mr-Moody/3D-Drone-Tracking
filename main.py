import cv2 as cv
import numpy as np

from src.window import Window

def main():
    window = Window()
    image = np.linspace(0, 255, 256*256).reshape((256, 256)).astype(np.uint8)
    window.show_image(image)
    cv.waitKey(0)
    window.close()

if __name__ == "__main__":
    main()
