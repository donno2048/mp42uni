from curses import wrapper
from os import system
from sys import argv
try: from PIL.Image import open
except: from Image import open
from cv2 import VideoCapture, imwrite, resize
def play(window):
	vidcap = VideoCapture(argv[1])
	success, image = vidcap.read()
	while success:
		imwrite(__file__.replace(".py", ".jpg"), resize(image, (144, 108), interpolation = 3))
		for l in I2T(__file__.replace(".py", ".jpg")).split("\n"):
			# time.sleep(x) # Use this to change the fps
			window.addstr(l + "\n")
			window.refresh()
		window.move(0, 0)
		success, image = vidcap.read()
def I2T(File):
	text = ""
	im = open(File)
	counter = 0
	field = True
	for pixel in list(im.convert("1").getdata()):
		if field:
			if pixel > 127: text += "*"
			else: text += " "
		counter += 1
		if counter >= im.size[0]:
			counter = 0
			if field: text += "\n"
			field = not field
	return text
def main(): wrapper(play)