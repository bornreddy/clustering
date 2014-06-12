import numpy as np
from PIL import Image
import random
import color as cl

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
  random_centroids = random.sample(range(0,255), k)
  print random_centroids
  clusters = {}
  for c in random_centroids:
    clusters[c] = []
  #got through pixels and assign to the right clusters as tuples
  distances = []
  for x in range(0,image.size[0]):
    for y in range(0,image.size[1]):
      min_distance = 250000000
      intensity = image.getpixel((x,y))
      print intensity
      for c in random_centroids:
        distance = abs(c-intensity)
        if distance < min_distance:
          min_distance = distance
          right_cluster = c
      clusters[right_cluster].append((x,y))
  change_colors(clusters, image)
 
def change_colors(dict, image):
  image = image.convert("RGB")
  color_index = 0
  for x in dict.keys():
    color = cl.list[color_index]
    for y in dict[x]:
      image.putpixel(y, color)
    color_index += 1
  image.show()
    
img = Image.open("images/tiger.jpg")
img.load()
img = img.convert('L')
kmeans(img, 4)




       

  
    



  
