import numpy as np
from PIL import Image
import random
import color as cl
import os, sys
import datetime 


def random_rgb(x):
  rand_tups = []
  rs = random.sample(range(0,255),x)
  bs = random.sample(range(0,255),x)
  gs = random.sample(range(0,255),x)
  for i in range(0,x):
    rand_tups.append((rs[i], bs[i], gs[i]))
  return rand_tups

def color_distance(rgb1,rgb2):
  r1, g1, b1 = rgb1[0], rgb1[1], rgb1[2]
  r2, g2, b2 = rgb2[0], rgb2[1], rgb2[2]
  d = ((r2-r1)*0.3)**2 + ((g2-g1)*0.59)**2 + ((b2-b1)*0.11)**2
  return d

def least_diff(rgb,centers):
  minDistance = 50000000000
  x = tuple()
  new_center = tuple()
  for x in centers:
    distance = color_distance(rgb,x)
    if distance < minDistance:
      minDistance = distance
      new_center = x
  return new_center

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
      clusters[right_center].append((x,y))
  return clusters 

def recenter(clusters, img):
  done = False
  old_centers = clusters.keys()
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
    new_centers.append((r,g,b))
  if old_centers == new_centers:
    done = True
  return done, new_centers


def print_pretty_dict(dict):
  for x in dict.keys():
    print x,": "
    for c in dict[x]:
      print c

def reassign(centers,img):
  groups = {}
  for c in centers:
    groups[c] = []
  for x in range(0,img.size[0]):
    for y in range(0,img.size[1]):
      color = img.getpixel((x,y))
      center = least_diff(color,centers)
      groups[center].append((x,y))
  return groups

def kmeans(k, img):
  centroids = random_rgb(k)
  clusters = initial_assign(centroids,img)
  changed = True
  while True:
    done, centers = recenter(clusters,img)
    if done == True:
      change_colors(clusters,img)
      break
    clusters = reassign(centers,img)
  return clusters

def change_colors(dict,img):
  a = datetime.datetime.now()
  img = img.convert('RGB')
  color_index = 0
  for x in dict.keys():
    color = cl.neon[color_index]
    for y in dict[x]:
      img.putpixel(y,color)
    color_index += 1
  b = datetime.datetime.now()
  print "time of change_color: ", b-a
  img.show()

def print_pretty_dict(dict):
  for x in dict.keys():
    print x,": "
    for c in dict[x]:
      print c
           
def main():
  filename = raw_input("please enter an image to segment: ")
  k = int(raw_input("please enter a k value: "))
  img = Image.open(filename)
  a = datetime.datetime.now()
  clusters = kmeans(k,img)
  b = datetime.datetime.now()
  print "kmeans time: ", b-a
  '''
  img = Image.open(sys.argv[1])
  img.show()
  color_cluster(k, img)
  img.show()
  '''
  
main()





