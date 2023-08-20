#this script generates the images based on certain specs
# that will later be turned into frames of a video

#density

#imports
from PIL import Image
import numpy
import random
import ffmpeg
import hashlib
import glob




#hashing function
def hash_file(filename):

    h = hashlib.sha256()

    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()


#making the images
def rando_pics(frames):
    


    for i in range(frames):

        counter = str(i)
        #the 300's in the below line are the dimensinos of the output images, change at will
        arr = numpy.random.randint(low = 0, high = 255, size = (1080, 1920, 3))
        im = Image.fromarray(arr.astype('uint8'))
        
        message = im.tobytes()
        message_ = message.hex()

        message2 = open("path for text file","r")
        message2_ = hashlib.sha256(message2)

        if message_ in message2_:
            print("collision")
            im.save("path for picture store" + counter + ".png")
            f = open("path for text file","a")
            f.write('\n' + "---COLLISION AT:" + message_)
            break
        else:
            im.save("path for picture store" + counter + ".png")
        
            print("saved random image")
            
            f = open("path for text file","a")
            f.write('\n')

            f.write(message_ + "---" + counter)
            f.close()
            print("updated log" +"---" + counter)
            print('\n')
        

#20 million runs of a 1 by 1 pixel array should get a collision in theory      

rando_pics(1)       

#density
