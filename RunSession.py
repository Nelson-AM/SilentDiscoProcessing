# RunSession

from ProcessImage import *
from ProcessVideo import *

# time_start = 0
# time_step = 60000
# time_total = (14780 * 1000) + 1

frame_start = 0
frame_step = 1
frame_total = (14780 * 25) + 1

for i in range(frame_start, frame_total, frame_step):
    process_video_frame('/Volumes/SAMSUNG/TX-BACK UP_21.mov', i, 'Frames')

# total = 660000 + 1
# for i in range(start, total, step):
#     session.ProcessVideoPerSec('~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_21_120-130.mov',
#                                i)

# for i in range(start, total, step):
#    session.process_video_time('/Volumes/SAMSUNG/TX-BACK UP_21.mov', i, '~/Documents/PYTHON/SilentDiscoData/Frames/')

# ProcessImage = ProcessImage()

# img = ProcessImage.read_image('~/Documents/PYTHON/SilentDiscoData/original_r.png', cv2.IMREAD_GRAYSCALE)
# ProcessImage.show_image(img)



# session = ProcessImage()

# session.otsu_threshold('~/Documents/PYTHON/SilentDiscoData/original_b.png')
# session.otsu_threshold('~/Documents/PYTHON/SilentDiscoData/original_g.png')
# session.otsu_threshold('~/Documents/PYTHON/SilentDiscoData/original_r.png')

# session.find_centres_masked('~/Documents/PYTHON/SilentDiscoData/original_b_otsu_gaussian.png', '~/Documents/PYTHON/SilentDiscoData/TX_MASK.png')
# session.find_centres_masked('~/Documents/PYTHON/SilentDiscoData/original_g_otsu_gaussian.png', '~/Documents/PYTHON/SilentDiscoData/TX_MASK.png')
# session.find_centres_masked('~/Documents/PYTHON/SilentDiscoData/original_r_otsu_gaussian.png', '~/Documents/PYTHON/SilentDiscoData/TX_MASK.png')



# maskin = '~/Documents/PYTHON/SilentDiscoData/Frames/TX-BACK UP_0_MASK.png'

# session.find_centres()

# Stuff I might want to put into the class:
#
# def runsession(self, imagename):
#    """ Runs an image processing session.
#    """
#
#    self.separate_colours(imagename)

# session.ProcessVideoPerSec('~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_21_120-130.mov', 20000)
# session.read_video('~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_10s.mov')