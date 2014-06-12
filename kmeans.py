import numpy as np
from PIL import Image

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

  
