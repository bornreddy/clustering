import numpy as np
from PIL import Image
import random
import color as cl
import os, sys

'''return x unique random rgb tuples as a list'''
def random_rgb(x):
  rand_tups = []
  rs = random.sample(range(0,255),x)
  bs = random.sample(range(0,255),x)
  gs = random.sample(range(0,255),x)
  for i in range(0,x):
    rand_tups.append((rs[i], bs[i], gs[i]))
  return rand_tups

'''find the weighted euclidean distance between two colors'''
def color_distance(rgb1,rgb2):
  r1, g1, b1 = rgb1[0], rgb1[1], rgb1[2]
  r2, g2, b2 = rgb2[0], rgb2[1], rgb2[2]
  d = ((r2-r1)*0.3)**2 + ((g2-g1)*0.59)**2 + ((b2-b1)*0.11)**2
  return d


'''FIX'''
'''intially, given the list of pixel location data and a the random centroids, assign the pixels to the closest centroids.'''
def initial_assign(centroids, img):
  clusters = {}
  for c in centroids:
    clusters[c] = []
  total_pix = img.size[0] * img.size[1]
  
  for x in total_pix:
    min_distance = 50,000,000
    right_cluster = centroids[0]
    pix_color = img.getpixel((pixel_list[x][0], pixel_list[x][1]))
    for y in centroids:
      distance = color_distance(pix_color, centroids[y])
      if distance < min_distance:
        min_distance = distance
        right_cluster = centroids[y]
    clusters[right_cluster].append(pixel_list[x])
  return clusters
  
    
 
  
     
  




def main():
  #print random_rgb(2)
  #print color_distance((255,255,255),(0,0,0))
  print initial_assign(
  '''
  img = Image.open(sys.argv[1])
  img.show()
  color_cluster(k, img)
  img.show()
  '''
  
main()





