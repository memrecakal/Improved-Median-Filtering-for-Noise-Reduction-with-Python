import numpy as np

class Part:
    def __init__(self, img, index_in_orj_image):
        self.img = img
        self.index = index_in_orj_image 

    def shape(self):
        return np.shape(self.img)