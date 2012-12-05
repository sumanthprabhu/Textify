"""
	Author : Sumanth Prabhu <sumanthprabhu.104@gmail.com> 
"""
from PIL import Image,ImageFont,ImageDraw

import random
import textwrap
import sys


#check for valid input
def validity(argv):
	if len(argv) != 3:
		return [False,"Missing arguments"]
	try:
   		with open(sys.argv[1]) as f: 
   			#check if it's an image file
   			if not sys.argv[1].endswith(('.png','.jpg','.jpeg')):
   				return [False,"Please enter'png','jpg' or'jpeg' files only"]
	except IOError as e:
   		return [False, str(e)]
   	else:
		return [True]


#textify the image
def textify(input_file,text_file):

	#Open the input image
	input_img = Image.open(input_file)
	text_img = Image.new(input_img.mode,input_img.size,"white")
	draw = ImageDraw.Draw(text_img)

	#Generate image containing text
	width = text_img.size[0]
	height = text_img.size[1]

	with open(text_file,'r') as f:
		input_txt = f.read()
		
	text = input_txt * (width*height/len(input_txt))
	lines = textwrap.wrap(text,width=width)	

	fontsize = 9
	
	#windows
	if sys.platform.startswith('win'):
		font = ImageFont.truetype("ARIALN.TTF",fontsize)
        elif sys.platform.startswith('darwin'):
                font = ImageFont.truetyoe("~/Library/Fonts/Arial.ttf",fontsize)
	else:
		font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", fontsize)

	h = 0

	for line in lines:
		draw.text((0,h),line,font=font,fill="black")		
		h += fontsize


	#Create output image
	output_img = input_img.copy()

	for i, px in enumerate(text_img.getdata()):
		if px[:3] == (255,255,255) :
			y = i / width
			x = i % width
			output_img.putpixel((x, y), (255, 255, 255))


	output_img.save("output.jpg")

	#Display output image
	output_img.show()


def main():
	resp = validity(sys.argv)
	if resp[0]: #valid input
		textify(sys.argv[1],sys.argv[2])
	else:
		print "Error : " + resp[1]

if __name__ == "__main__":
	main()
