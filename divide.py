import numpy as np
from part import Part
import cv2


def divide_x(t, part_count):
    for i in range(t.shape[0],0, -1):
        if i % (part_count - 1) == 0: 
            end_point = i
            break
        
    part_size = int(end_point / (part_count - 1))
    
    x_ = []
    for x in range((end_point//part_size)):
        x_.append([x*part_size, (x+1)*part_size-1])
    
    x_.append([end_point, t.shape[0]])

    image_parts = []
    for x in x_:
        part = Part(t[x[0]:x[1],], x)
        image_parts.append(part)

    return np.array(image_parts)


def main():
    img = cv2.imread('testimages/salttest.jpg', cv2.IMREAD_GRAYSCALE)

    x_ = divide_x(img, 5)

    print(x_)

    image_parts = []
    for x in x_:
        part = img[x[0]:x[1],]
        image_parts.append(part)

    new = image_parts[0]
    for part in image_parts[1:]:
        new = np.vstack((new, part))
        cv2.imshow("a", part)
        cv2.imshow("merged", new)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    

if __name__ == "__main__":
    main()