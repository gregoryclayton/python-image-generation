# random-image-generation
An experiment in unique image generation inspired by Devs<br><br>


Alex Garland's 2020 show Devs is great, high recommend it if you haven;t already checked it out.<br>
Beyond just being a great show, its very inspiring<br>
for those trying to operate in the nexus between art and technology.

The tech shown off in the show gets pretty fantastic but is ultimately rooted in reality.<br>
The intro features simulations of protien-folding prediction<br>
a problem Openai has make great strides on with thier Alphafold project.

SPOILERS AHEAD!<br>
the main simulation machine uses "quantum computing" in an attempt<br>
to siumate the entirety of esistence from the very beginning<br>
in order to recreate a madman's lost love one's<br>
its quite a site to behold<br>
At one point they simulate jesus on the cross<br>

While the idea of actually simulating and recreating reality down<br>
to its atomic scale still seems far off (at least for me), the idea<br>
seems like it could translate to a basic pixel matrix<br><br><br>


ThE IDEA:<br>
- generate a pixel matrix with each pixel value randomly assigned
- hash the resulting pixel matrix and save the hash in a log
- generate a new pixel matrix and check it's hash against existsing hashes
- if there's a collision, generate a new image. This will keep<br> 
the ersults from repeating, even if its just one pixel difference.<br>

in theory, a large enough pixel matrix genrating images with enough timebr>
will create an image of every possilbe pixel combination, from all black <br>
to all white and everything inbetween, from homer to shakespeare<br>

- randomImageGenerator.py accomplishes this image generation, just open it and adjust the variables to your desired file paths.

these are the results, generate as many as you desire.

- video_generator.py turns the generated images into frames of a video and outputs the result as an mkv file.

the result looks something like this, pretty happy with it<br>
Staring at the center has quite the psychadelic, mandalla-like effect, pretty cool<br>
Hard to miss the similarities with the static from a telvision set resulting from<br>
the comsic background radiation, also pretty cool.<br><br>

BUGS AND IMPROVEMNTS<br>
 - an obvious idea would be a seperate _init_ file to execute both files without have to<br>
 access them manually.<br>
 - the output is only mkv format right now, different ones woulbe be ideal
 - the hashing function is broken the log just repeats desipte the images being<br>
 different. This means images are not neccessarily unique, although resuls thus far<br>
 have yet to repeat.<br>
 
 -density

