import pyautogui
print('Press Ctrl-C or Ctrl-Z to quit')

try:
    while True:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        position = f'X: {str(x).rjust(4)}, Y: {str(y).rjust(4)}'
        position += f' RGB: ({str(pixelColor[0]).rjust(3)}, {str(pixelColor[1]).rjust(3)}, {str(pixelColor[2]).rjust(3)})'
        print(position, end='')
        print('\b' * len(position), end='', flush=True)
except KeyboardInterrupt:
    print('OK')
