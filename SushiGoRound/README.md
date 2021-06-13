# Sushi Go Round Bot

A simple program used to play sushi go round.

[Demo](https://www.youtube.com/watch?v=1PBlQ11OJVU)

## How it works

This program uses [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) to control mouse movement and [PIL (or pillow)](https://pypi.org/project/Pillow/) to scan for
images that match pngs that are stored in the same folder as the program.

PIL looks for different types of sushi orders, and sends click commands via PyAutoGUI to make the sushi. Occasionally, the clicker will clear the plates as well.
When there is a lack of ingredients, ingredients will be ordered.

## Usage

A lot of the mouse clicks are coded in a way that it works on my original machine, (i.e. the coordinates of mouse clicks) but you can measure the coordinates on
your machine yourself and change all the functions that require coordinates of mouse clicks to be provided.
