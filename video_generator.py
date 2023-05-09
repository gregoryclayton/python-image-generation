# this script turns the images in the picture store file into
# a mkv file

#density

#imports
import cv2
import os

#change these to the desired filepaths
image_folder = 'picutreStore filepath'
video_name = 'video filepath'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#the 1 in the below line is the frame duration, the higher the number the shorter the duration, change at will
video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

#density