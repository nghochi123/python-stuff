import os
import PIL.Image as p


fp = "C:\\Users\\nghoc\\Desktop\\GitHub\\python-stuff\\ascii-video"


asciichars = "$@B%8&WM#*oahkwmZO0QLCJUYXzcvxrjft/\|()1[]?-_+~<>i!lI;:,^`.      "
asciiarr = list(asciichars)[::-1] # 66 shades of grey; asciiarr[0] is darkest, ascii[65] is lightest

#One line can have up to 215 characters
#Height is 125 characters
#Trying height 125, width 230; around 16:9 ratio ---> I was wrong, '\n's take much more space; more like 63 or 64 height. 144 is for a different video
#Images are all 1920/1080; similar size.
#Video is 275s long, 1134 images. 4fps.
#Grayscale moves from 0 to 255; 66 shades of grey, so /3.85. Added more spaces at the end so lighter shades of white are still blank.
width = 230
height = 63

gray_divisor = 4 #Only can be integer.

def gs(img):
    return(img.convert("L"))

def pta(gs_img):
    pixels = gs_img.getdata()
    #characters = "".join([asciiarr])

def resize(image, new_width=width, new_height=height):
    return image.resize((new_width, new_height))

def img_str(img):
    image = gs(p.open(img))
    rs_img = resize(image)
    pixels = rs_img.getdata()
    new_pixels = "".join([asciiarr[pixel_value//gray_divisor] for pixel_value in pixels])
    return new_pixels #This will be a string. To do now is to split for every 230 characters.



#The final function to convert an image to an ascii format.
def to_ascii(img):
    os.chdir(fp)
    np = img_str(img)
    ascii_img = [np[index:index+int(width)] for index in range(0, len(np), int(width))]
    return '\n'.join(ascii_img)