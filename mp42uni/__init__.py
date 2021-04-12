from curses import wrapper
from os import system
from sys import argv
def play(window):
	for l in open(__file__.replace(".py", ".txt")):
		# time.sleep(x) # Use this to change the fps
		if l[0] == 'R': window.move(0,0)
		else:
			window.addstr(l)
			window.refresh()
def main():
	system(f"python3 {__file__.replace('__init__', 'process')} {argv[1]} > {__file__.replace('.py', '.txt')}")
	wrapper(play)
