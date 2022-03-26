import numpy as np

from part import Part

def sort_parts(image_parts):
    part_dict = {}
    i = 0
    for part in image_parts:
        part_dict[i] = (part.img, part.index)
        i += 1

    sorted_dict = {k: v for k, v in sorted(part_dict.items(), key=lambda item: item[1][1][1])}
    
    sorted_parts = []
    for dict_key in sorted_dict:
        new_part = Part(sorted_dict[dict_key][0],sorted_dict[dict_key][1])
        sorted_parts.append(new_part)

    return sorted_parts


def merge_parts(image_parts):
    parts = sort_parts(image_parts)

    new = parts[0].img
    for part in parts[1:]:
        new = np.vstack((new, part.img))

    return new