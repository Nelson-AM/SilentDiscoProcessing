import glob
import cv2

framedir = "/Users/Nelson/Desktop/ILLC_PhD_Presentation/PNG/"

video = cv2.VideoWriter('video.mov', -1, 1, (1920, 1080))

for image in sorted(glob.glob(framedir + "*.png")):
    
    img = cv2.imread(image)
    height, width, layers = img.shape
    
    video.write(img)

cv2.destroyAllWindows()
video.release()