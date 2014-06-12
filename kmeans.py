import numpy as np
from PIL import Image
import random

#must take in a grayscale image
def histogramify(image):
  intensity_array = []
  for x in range(0,image.size[0]):
    for y in range(0,image.size[1]):
      intensity = image.getpixel((x,y))
      intensity_array.append(intensity)
  hist = np.histogram(intensity_array, range(0,257))
  print hist
  return hist

def kmeans(image, k):
  #set up dictionary with random centroids
  for i in range(0,k):
    random_centroids = random.sample(range(0,255), k)
    print random_centroids
    clusters = {}
    for c in random_centroids:
      clusters[c] = []
  #got through pixels and assign to the right clusters as tuples
  distances = []
  min_distance = 255000000
  for x in range(0,image.size[0]):
    for y in range(0,image.size[1]):
      intensity = image.getpixel((x,y))
      for c in random_centroids:
        distance = abs(c-intensity)
        if distance < min_distance:
          min_distance = distance
          right_cluster = c
      print right_cluster
      clusters[right_cluster].append((x,y))
  print clusters


img = Image.open("images/tiger.jpg")
img.load()
img = img.convert('L')
kmeans(img, 4)



       

  
    



  
