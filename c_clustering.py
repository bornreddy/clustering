import numpy as np
from PIL import Image
import random
import color as cl
import os, sys
import datetime 

'''IMPORTANT!!!!!!! getting weird error in recompute_reassign - list remove says that p is not in clusters[c]. what's going on???'''


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

def least_diff(rgb,centers):
  minDistance = 50000000000
  x = tuple()
  for x in centers:
    distance = color_distance(rgb,x)
    if distance < minDistance:
      minDistance = distance
      newcenter = x
  return x

def initial_assign(centroids, img):
  clusters = {}
  for c in centroids:
    clusters[c] = []
  for x in range(0,img.size[0]):
    for y in range(0,img.size[1]):
      color = img.getpixel((x,y))
      minDistance = 50000000
      right_center = tuple()
      for c in centroids:
        distance = color_distance(color,c)
        if (distance < minDistance):
          minDistance = distance
          right_center = c
      '''add location of each pixel to the correct random centroid'''
      clusters[right_center].append((x,y))
  return clusters 

'''given a list of clusters and an image, compute the average color of each cluster and make that the new centroid; then change the pixels to fit their new clusters; return the new clusters and whether or not any single pixels have changed'''

def recenter(clusters, img):
  changed = False
  new_centers = []
  for c in clusters.keys():
    r, g, b = 0, 0, 0
    num = len(clusters[c])
    if num == 0:
      continue
    for x in clusters[c]:
      p = img.getpixel((x[0],x[1]))
      r += p[0]
      g += p[1]
      b += p[2]
    r /= num
    g /= num
    b /= num
    if (r,g,b) != c:
      changed = True
    new_centers.append((r,g,b))
  print new_centers
  return changed, new_centers


def reassign(centers,img):
  clusters = {}
  for c in centers:
    clusters[c] = []
  changed = False
  for x in range(0,img.size[0]):
    for y in range(0,img.size[1]):
      color = img.getpixel((x,y))
      center = least_diff(color,centers)
      clusters[c].append((x,y))
  return clusters

def kmeans(k, img):
  '''initial centroids'''
  centroids = random_rgb(k)
  clusters = initial_assign(centroids,img)
  changed = True
  while changed == True:
    changed,centers = recenter(clusters,img)
    clusters = reassign(centers,img)
  return clusters

def change_colors(dict,img):
  img = img.convert('RGB')
  color_index = 0
  for x in dict.keys():
    color = cl.muted[color_index]
    for y in dict[x]:
      img.putpixel(y,color)
    color_index += 1
  img.show()

def print_pretty_dict(dict):
  for x in dict.keys():
    print x,": "
    for c in dict[x]:
      print c
           
def main():
  img = Image.open("images/tiger.jpg")
  a = datetime.datetime.now()
  clusters = kmeans(8,img)
  b = datetime.datetime.now()
  print "kmeans time: ", b-a
  change_colors(clusters, img)
  '''
  img = Image.open(sys.argv[1])
  img.show()
  color_cluster(k, img)
  img.show()
  '''
  
main()





