import argparse
import sys
import os
from PIL import Image


def convert_byte(num):
	"""
	this function will convert bytes to MB.... GB... etc
	"""
	step_unit = 1024 # base the size

	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < step_unit:
			return "%3.1f %s" % (num, x)
		num /= step_unit

def info(img):
	"""
	info: function to get all info from image
	"""
	try:
		im=Image.open(img)
		print('Image:', img)
		print('Width:', im.width)
		print('Height:', im.height)
		print('Bands:', len(im.getbands()))
		print('Total size:', convert_byte(1))
		# do stuff
	except IOError as e:
		print('Invalid image file')


def run(args):
	"""
	run: function to get all info from image used by parser
	"""
	info(args.img)
		 

def main():
	if not sys.version_info >= (3, 6):
		sys.exit("ERROR: imgInfo needs Python 3.6 or later.")

	if len(sys.argv) == 1:
		print("imgInfo: imgInfo command line tools")
		print("imgInfo -h, --help")
		sys.exit()

	parser = argparse.ArgumentParser(prog='imgInfo', description='Get information abount given image file')
	parser.add_argument('img', help='image help')
	args = parser.parse_args()
	run(args)


if __name__ == '__main__':
	main()
