from os.path import join
from os import listdir
import os

counter = 5
for fn in listdir("image") :
    os.rename(join("image", fn), join("image", str(counter)+'.jpg'))
    counter = counter + 1