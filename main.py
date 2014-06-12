import kmeans
from PIL import Image
import os, sys

file_name = sys.argv[1]
try:
  img = Image.open(file_name)
  img.load()
  img = img.convert('L')
  img.show()
  kmeans.histogramify(img)
except IOError:
  print "Unable to read file. Check spelling or try another format."
