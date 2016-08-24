from ProcessVideo import *
from ProcessImage import *

imname = "/Users/Nelson/Desktop/Bromo.jpg"

image = read_image(imname)
print image.shape

# print image.shape
# print len(image.shape)
# print range(image.shape[1])

otsuim = otsu_threshold_test(imname)

show_image(image)
show_image(otsuim)