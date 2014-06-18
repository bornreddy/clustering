import kmeans
from PIL import Image
import os, sys
import color
import datetime


file_name = sys.argv[1]
k = int(sys.argv[2])

if (k > 5):
  print "please enter a k value less than 4"
  sys.exit()

try:
  img = Image.open(file_name)
  img.load()
  img = img.convert('L')
  #img.show()
  time1 = datetime.datetime.now()
  kmeans.kmeans(img,k)
  time2 = datetime.datetime.now()
  print time2-time1
except IOError:
  print "Unable to read file. Check spelling or try another format."
