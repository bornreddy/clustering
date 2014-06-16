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
  print k
  random_centroids = random.sample(range(0,255), k)
  print random_centroids
  clusters = {}
  for c in random_centroids:
    clusters[c] = []
  #got through pixels and assign to the right clusters as tuples
  
  for x in range(0,image.size[0]):
    for y in range(0,image.size[1]):
      min_distance = 250000000
      intensity = image.getpixel((x,y))
     # print intensity
      for c in random_centroids:
        distance = abs(c-intensity)
        if distance < min_distance:
          min_distance = distance
          right_cluster = c
      clusters[right_cluster].append((x,y))
  #recompute centroids and rename categories
  for c in clusters.keys():
    new_center = average_intensity_given_tuples(clusters[c], image)
    clusters[new_center] = clusters.pop(c)    
  #reassign pixels and check for cross-cluster movement
  changed = True
  while changed == True:
#    print "recomputing center"
    changed, clusters = reassign(clusters, image)
  change_colors(clusters, image)
 

def reassign(dict, image):
#  print "inside reassign function"
  changed = False
  for x in dict.keys():
    for y in dict[x]:
      intensity = image.getpixel((y[0],y[1]))
      new_key = least_diff(intensity, dict.keys())
      if (new_key != x):
        changed = True
        dict[x].remove((y[0],y[1]))
        dict[new_key].append((y[0],y[1]))
#  print "returning from reassign function"
  return changed, dict
      

def average_intensity_given_tuples(list_tup, image):
  sum = 0
  for x in range(0,(len(list_tup)-1)):
    sum += image.getpixel(list_tup[x])
  return sum/len(list_tup)

def least_diff(intensity, keys):
  min_distance = abs(keys[0] - intensity)
  closest_key = keys[0]
  for x in keys[1:]:
    distance = abs(x - intensity)
    if distance < min_distance:
      min_distance = distance
      closest_key = x
  return closest_key
    

#handle this with an arbitray number of k. as in, have more tuples available in each palette or randomly create them in this algorithm. 
def change_colors(dict, image):
  image = image.convert("RGB")
  color_index = 0
  for x in dict.keys():
    color = cl.neon[color_index]
    for y in dict[x]:
      image.putpixel(y, color)
    color_index += 1
  image.show()


img = Image.open("images/tiger.jpg")
img.load()
img = img.convert('L')
kmeans(img, 4)


