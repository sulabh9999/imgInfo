import argparse
import sys
import os
from PIL import Image
import collections


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
		ImgDtls = collections.namedtuple('ImgDtls',['height','width','bands', 'size']) 
		return ImgDtls(im.height, im.width, len(im.getbands()), convert_byte(os.path.getsize(img))) 
	except IOError as e:
		print(f'Invalid image file: "{img}"')
		return None


def run(args):
	"""
	run: function to get all info from image used by parser
	"""
	imgDtls = info(args.imgName)
	if imgDtls:
		print('Image:', os.path.basename(args.imgName))
		print('Width:', imgDtls.width)
		print('Height:', imgDtls.height)
		print('Bands:', imgDtls.bands)


def main():
	if not sys.version_info >= (3, 5):
		sys.exit("ERROR: imgInfo needs Python 3.5 or later.")

	if len(sys.argv) == 1:
		print("imgInfo: imgInfo command line tools")
		print("imgInfo -h, --help")
		sys.exit()

	parser = argparse.ArgumentParser(prog='imgInfo', description='Get information abount given image file')
	parser.add_argument('imgName', help='Name of an image')
	# parser.add_argument('-s', action='store_true', help='To show image shape as tupple')
	args = parser.parse_args()
	run(args)


if __name__ == '__main__':
	main()
