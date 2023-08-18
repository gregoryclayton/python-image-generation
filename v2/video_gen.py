
#imports
import cv2
import os

#change these to the desired filepaths
image_folder = 'C:/Users/grego/Desktop/pros2/image_gen/videoFrameStorage'
video_name = 'C:/Users/grego/Desktop/pros2/image_gen/video.mkv'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#the 1 in the below line is the frame duration, the higher the number the shorter the duration, change at will
video = cv2.VideoWriter(video_name, 0, 24, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

#density