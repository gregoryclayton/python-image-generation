# random-image-generation
An experiment in unique image generation with python inspired by Devs<br><br>

<h3>UPDATE</h3>
<p><i>okay so I finally got around to writing a ersion of this code that actually logs each generated image in orderto check<br>
gainst future genratons to enureorginality. the new versions are in the file v2.<br>
 I couldnt quite get hashlib to work so the lg just outputs a hex readout of the image binary.<br> 
 Works great but gets slow quick and the log file gets huge quick. Will revisit soon to add a hash function.<br></i></p>
<img src="https://github.com/gregoryclayton/python-image-generation/blob/main/readmePics/devs.png?raw=true" style="height:300px;">

Alex Garland's 2020 show <a href="https://en.wikipedia.org/wiki/Devs">Devs</a> is great, highly recommend it if you haven't  checked it out yet.<br>
Beyond just being a great show, its very inspiring<br>
for those trying to operate in the nexus between art and technology.

The tech shown off in the show gets pretty fantastic at times,<br> 
but its rooted in reality, for the most part...<br><br>
<b><i>SPOILERS AHEAD!</i></b><br><br>
The intro features simulations of protien-folding predictions,<br>
a problem the Alphafold project has made great strides in since the show's release.<br>

the main machine uses "quantum computing" in an attempt<br>
to simulate the entirety of existence from the very beginning<br>
in order to recreate a madman's lost love one's<br>
its quite the site to behold<br>

<img src="https://github.com/gregoryclayton/python-image-generation/blob/main/readmePics/devs1.png?raw=true">

At one point they even simulate jesus on the cross<br>

<img src="https://github.com/gregoryclayton/python-image-generation/blob/main/readmePics/devs2.jpg?raw=true" style="height:300px;">

While the idea of actually simulating and recreating reality down<br>
to its atomic scale is still a little far off (at least for me), the idea<br>
seems like it could translate well to a basic pixel matrix.<br><br>


<i><b>THE IDEA:</b></i><br>
- generate a pixel matrix with each pixel value randomly assigned
- hash the resulting pixel matrix and save the hash in a log
- generate a new pixel matrix and check it's hash against existing hashes
- if there's a collision, generate a new image. This will keep<br> 
the results from repeating, even if it's just one pixel difference.<br>

In theory, a large enough pixel matrix genrating images with enough time
will create an image of every possilbe pixel combination, from all black <br>
to all white and everything inbetween, from rembrant to homer.<br>

- randomImageGenerator.py is a script I wrote that accomplishes this image generation, <br>
- just open it and adjust the variables to your desired file paths, and pixel array size. <br>

these are the typical results, generate as many as you desire.

<img src="https://github.com/gregoryclayton/python-image-generation/blob/main/readmePics/picture3.png?raw=true">

- video_generator.py turns the generated images into frames of a video and outputs the result as an mkv file.

the result looks something like this, pretty happy with it<br>

<img src="https://github.com/gregoryclayton/python-image-generation/blob/main/readmePics/Video1.gif?raw=true">

- Staring at the center has quite the psychadelic, mandalla-like effect, pretty cool.<br>
- It's hard to miss the similarities with the static from a telvision set <br>
- resulting from the comsic background radiation, also pretty cool.<br><br>

<b><i>BUGS AND IMPROVEMNTS</i></b><br>
 - an obvious idea would be a seperate _init_ file to execute both files without having to<br>
 access them manually.<br>
 - the output is only mkv format right now, other options would be ideal.<br>
 - the hashing function is broken,
   the log just repeats the hash for the first image generated regardless of how many are called by the function.<br>
    This means images are not neccessarily unique, although results I've got thus far<br>
   have yet to repeat, but they have also yet to generate anything other than random color really.<br>
 
 <b><i> density</b></i>

