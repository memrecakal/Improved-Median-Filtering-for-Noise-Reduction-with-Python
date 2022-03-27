from medianfilter import median_filter
from medianfilter_improved import median_filter_improved
from divide import divide_x
from merger import merge_parts
import os
import cv2
import concurrent.futures

def main():
    part_number = os.cpu_count() + 1
    img = cv2.imread('testimages/salttest.jpg', cv2.IMREAD_GRAYSCALE)   

    parts = divide_x(img, part_number)
    new_parts = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(median_filter_improved, part, 3, copy_border=1) for part in parts]

        for f in concurrent.futures.as_completed(results):
            new_parts.append(f.result())


    whole = merge_parts(new_parts)
    
    cv2.imshow("whole", whole)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()