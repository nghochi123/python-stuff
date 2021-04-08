# Video to ASCII converter

A simple program used to convert images to ASCII. Free to use

[Demo](https://www.youtube.com/watch?v=7qHKRo7rqhQ)

## How it works

This program uses [PIL (or pillow)](https://pypi.org/project/Pillow/) to convert individual images into ASCII 'images' based on the grayscaled version of
the image. The image is 'converted' into a smaller resolution, with less pixels to compare. The darker the pixel, the more dense the character used
to fill the pixel space. It does this for all the frames in the video.

## Usage

Decompose a video into frames, based on how much space you want the frames to take up. Put all the images in the same file as av.py, and rename them in the
form scene00000.png. For example, for the 25th frame, we will rename the scene to scene00025.png. An easy way to do this is with VLC media player, where every
n frames are converted to png files in that format. The png files must have a fixed interval between the numbers (for example scene00025, scene00030,
scene00035 and so on).

### To be adjusted

Before running the program, you will need to adjust the following values:
* In av.py: On line 9, `for i in range(1,6752,6):`
* In toascii.py: Adjust width and height variables, and asciichars if needed.

After initial set up is done, you can just run av.py in the terminal.
