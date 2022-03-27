import numpy as np
import sys
from part import Part

def median_filter(part, mask, copy_border=1):
    img = part.img
    row, column = img.shape
    final_image = np.zeros((row, column), dtype=np.uint8)

    # handle borders
    margin_size = int((mask.shape[0] - 1) / 2)                                          # assuming square mask

    #   1) zero border
    new_img = np.zeros((row + 2*margin_size, column + 2*margin_size), dtype=np.uint8)
    new_img[margin_size : -margin_size, margin_size : -margin_size] = img

    if copy_border:
        #   2) copy border
        #       First left and right columns, then upper and lower rows.

        #       a) left column
        for left_column in range(margin_size):
            column2copy = img[:,0]
            new_img[margin_size:-margin_size,left_column] = column2copy

        #       b) left column
        for right_column in range(-1,-margin_size-1,-1):
            column2copy = img[:,-1]
            new_img[margin_size:-margin_size,right_column] = column2copy #BU İKİSİ TEK FOR'A İNER DÜŞÜNMEK LAZIM

        #       c) upper row
        for upper_row in range(margin_size):
            row2copy = new_img[margin_size,:]
            new_img[upper_row,:] = row2copy

        #       d) lower row
        for lower_row in range(-1,-margin_size-1,-1):
            row2copy = new_img[-margin_size-1,:]
            new_img[lower_row,:] = row2copy


    # now, we can start median filtering

    for i in range(row):
        for j in range(column):
            scope = []
            for x in range(i, i + mask.shape[0]):
                for y in range(j, j + mask.shape[1]):
                    scope.append(new_img[x][y])
            median = np.median(scope)
            final_image[i][j] = median

        progress = i * j / (row * column) * 100 
        sys.stdout.write("\r{0:.2f} %".format(progress))
        sys.stdout.flush()

    return Part(final_image, part.index)
     


