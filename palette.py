from PIL import Image
import os, sys
import kmeans

try:
  filename = sys.argv[1]
except IndexError:
  filename = raw_input("Enter a filename: ")
  
try:
  img = Image.open(filename)
except IOError:
  print "Unable to read file - check spelling."
  sys.exit()

bw = img.convert('L')
k = raw_input("enter a k value: ")
kmeans.kmeans(bw,k)

