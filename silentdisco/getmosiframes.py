#!/usr/bin/env python

# Extract MOSI-frame
import VideoProcessing.ProcessImage as pi
import VideoProcessing.ProcessVideo as pv

# vidin = "/Volumes/SAMSUNG/MOSI_JR/video/2015-05-23_1100.mov"
imin = "~/Documents/SilentDiscoProcessing/silentdisco/29001.png"
# mask = "/Volumes/SAMSUNG/MOSI/masks/mask_4.png"

# for i in range(1, 75000, 1000):
#    pv.save_frame_frame(vidin, i)

pi.save_contours_multi(imin, "4001_contours_masked") #, mask)