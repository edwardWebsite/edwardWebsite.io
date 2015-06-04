
import os
from PIL import Image
import ExifTags

def GenerationImageThumbnail(folderName):

	MAXWIDTH = 200.0;
	for infile in os.listdir(folderName):
		outfile = os.path.splitext(infile)[0] + "thumbnail.JPG"
		if infile != outfile:
			try:
				im = Image.open(folderName+infile)
				s = im.size
				ratio = MAXWIDTH/s[0];
				# print(ratio)
				im.thumbnail((int(round(s[0]*ratio)), int(round(s[1]*ratio))), Image.ANTIALIAS)
				im.save(folderName+outfile, "JPEG")
			except IOError:
				print "cannot create thumbnail for '%s'" % infile


GenerationImageThumbnail("./Saragosse/")