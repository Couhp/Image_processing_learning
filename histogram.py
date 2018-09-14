import cv2
import numpy as np
from matplotlib import pyplot as plt
# from sklearn.metrics.pairwise import cosine_similarity
import math
from os import listdir
from os.path import join

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


def zip_hist (hist) :
    """ hist : [blue, green, red]
        per color : shape (256 x 1)    (Ex [[12], [156], [10000],....]) """
    def normalize(vector) :
        summary = np.sum(vector)
        return [element/summary for element in vector]

    new_hist = []
    RANGE = 8 
    for color in hist :
        new_color = []
        for i in range(int(256/RANGE)) :
            temp = np.mean([color[_][0] if not np.isnan(color[_][0]) else 0 for _ in range(i*RANGE, i*RANGE + RANGE)])
            new_color.append(temp)
            
        new_hist.append(normalize(new_color))
    return new_hist


def get_hist (img) :
    color = ('b','g','r')
    hist = []
    for i,col in enumerate(color):
        hist.append (cv2.calcHist([img],[i],None,[256],[0,256]))
    return hist
    

#===============================================
def main () :
    img_1 = cv2.imread('image/1.jpg')
    hist_1 = zip_hist (get_hist(img_1))    

    list_img = [join("image",e) for e in listdir("image")]
    for img_file in list_img :
        img = cv2.imread(img_file)
        hist = zip_hist(get_hist(img))      

        print (np.mean([cosine_similarity(hist[i], hist_1[i]) for i in range(3)]))


    

#=== RUN -====
main()
    
    



# show histogram
    # plt.plot(histr,color = col)
    # plt.xlim([0,256])
# plt.show()

