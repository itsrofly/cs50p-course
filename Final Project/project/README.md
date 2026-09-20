# Tverbs
#### Video Demo:  <https://youtu.be/kQ1sskd_DBI>
#### Description:

My project was created with the aim of training irregular verbs, so I first started getting the verbs from the json file in my github repository using [requests](https://requests.readthedocs.io/en/latest/), and then print the list of verbs using [pandas](https://pandas.pydata.org) for check everything is ok, after I create the base of application using [tkinter](https://docs.python.org/3/library/tkinter.html), setting the resolution, minimum size, and icon.

Now I just need the frames, so in the frame.py file, I created the frames in class with their widgets and places, then I leave the initial frame starded and others not, to be able to open the other frames with the buttons, after that it was just program what buttons do.

So I passed the verbs to the class to get access to them with the frame quiz, enabling me to check and show the verb, and when all verbs are used, just stop and remove the next button. And finally I added the option to be random or sorted, and the about frame for some info and credits of images.

As for the design I tried to do something more modern, and creating my own color palette, images to match that I got Flaticon for free, made by Freepik, and I just needed to add the credits, and this is my palette:

* Primary (Dark but not black) - #2C2F33
* Secondary (bitween Blue and Purple) - #1F0164
* Tertiary (Full White) - #FFFFFF

Why did i choose tkinter?
I used tkinter because I can create an executable, and maybe leave it on as an open source application, but before using tkinter, I was doing it with pyside2 but for some reason I had problems running the application and decided to pause and do in tkinter but I think pyside2 would be better because create application not only for windows but also for android, ios and others