# ud036_StarterCode
Source code for a Movie Trailer website.

## Requirements
This program requires Pythin 2.7 to be installed. 
Get it [here](https://www.python.org/downloads/).

## Instructions
To summerise the instructions in one line: 
Download, extract, run entertainment_center.py.
If you need further instructions, don't worry- just keep reading.

First download these files by clicking the green button on GitHub that says 
Clone or download, then click Download Zip.
Next, you'll need to extract the zip file you downloaded. It will be named 
ud036_StarterCode.zip.

  ### Windows Users:
  -Open Windows Explorer (or any folder) and browse to the location you 
  downloaded ud036_StarterCode.zip to. 
  -Right-click ud036_StartCode.zip and then left-click "Extract All...".
  (A new window will pop up that says "Extract Compressed (Zipped) Folders" 
  at the top.) 
  -Click the button that says "Extract" at the bottom.
  This will make a new folder called ud036_StarterCode (without the .zip at
  the end).
  You can now delete the .zip folder as it is no longer needed.
  -Open the ud036_StartCode folder.
  At this point you can either double-click entertainment_center.py to run the 
  program or right-click entertainment_center.py and choose "Edit with IDLE".
  From within IDLE, click "Run", then "Run Module", or use the hotkey F5.
  
  ### Mac Users:
  -Open The Finder and search for ud036_StarterCode or browse to where you 
  downloaded it.
  -Select the zip file and click "Unzip" at the top center of The Finder window. 
  (If you don't see "Unzip"), then...
  -Right-click the file ud036_StartCode.zip
  -left-click "Open With...",
  -left-click "Archive Utility".
  At this point you can either double-click entertainment_center.py to run the 
  program or right-click entertainment_center.py and choose "Edit with IDLE".
  From within IDLE, click "Run", then "Run Module", or use the hotkey F5.
  
  ### Terminal Users (Linux, Mac, or Windows):
  -Open Terminal.
  -Navigate to the directory where you downloaded or cloned ud036_StarterCode.
  (Use cd to change directory and ls or dir to list what's in your current 
  directory.)
  -Once your in the ud036_StarterCode directory, just type 
  "entertainment_center.py" to run the program.
  
  -Alternatively, you can type "idle2.7" to open IDLE's GUI interface, 
  then click file, open file.
  -Browse to where you downloaded ud036_StarterCode, then select the file 
  named entertainment_center.py
  -To run the program from IDLE, click "Run", then "Run Module", 
  or use the hotkey F5.
  
## Notes
entrtainment_center.py defines six instances of Movie class found in media.py and 
initiates them with a movie title, storyline, poster image url, and youtube movie 
trailer url. Then entertainment_center.py creates an array called movies with the
six Movie instance names and passes it as an argument to a function called 
open_movies_page in fresh_tomatoes.py. 

fresh_tomatoes.py creates fresh_tomatoes.html to show the six movies poster image, 
title, and when clicked plays the youtube movie trailer.

## Credits
fresh_tomatoes.py was provided by Udacity and forked from 
[this repository](https://github.com/Udacity/ud036_StarterCode).

## License
MIT Licesne found [here](LICENSE.md)
