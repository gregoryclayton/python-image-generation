
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

#constants
counter = 0
hashdick = {}

#hashing stuff
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
    
    counter = 0
    for i in range(frames):

        #the 300's in the below line are the dimensinos of the output images, change at will
        arr = numpy.random.randint(low = 0, high = 255, size = (300, 300, 3))
        im = Image.fromarray(arr.astype('uint8'))
        stringcounter = str(counter)

        counter = counter + 1

        im.save("picutreStore/picture" + stringcounter + ".png")
        
        print("saved random pick",counter)

        hashthePics()
        
#more hashing stuff
def hashthePics():

    counter = 0
    stringcounter = str(counter)
    # the file path for the picture store
    for filename in glob.iglob('picutreStore' + '*/*.png'):
        mess = hash_file("picutreStore/picture" + stringcounter + ".png")
        messstring = str(mess)
        # this filepath is missing in this version, ork needs ot beb done on the hasgin side
        filly = open('hashedPics' + stringcounter + '.txt','a')
        filly.write(messstring)
        filly.close()
        counter = counter + 1
        print("hashed")



#enter the number of images you want to output into the below function
rando_pics()

#density

