from ProcessVideo import *
from ProcessImage import *

imname = "/Users/Nelson/Desktop/Mountains/Bromo.jpg"

image = read_image(imname)
print image.shape

# print image.shape
# print len(image.shape)
# print range(image.shape[1])

testim = (imname)

show_image(image)
show_image(testim[:,:,0])
show_image(testim[:,:,1])
show_image(testim[:,:,2])



"""
for i in range(10):
    rng = random.randint(1, 3229)
    
    image = '/Volumes/SAMSUNG/ESCOM/Frames/TX-BACK UP_21_' + str(rng) + '.png'
    print image

    find_contours_multi(image, mask)
"""