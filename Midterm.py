import random


# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  
  
def csumb(pic):
  # get width and height of photo to csumb-ify
  w, h = getWidth(pic), getHeight(pic)
  # create a gradient using the height and width dimensions
  gradient = makeEmptyPicture(w, h)
  makeGradient(gradient)
  # blend picture with gradient
  target = blend(pic, gradient)
  # Draw on the otter
  drawOtter(target)      
  #show(target)
  return target

def vhs(pic):
  # get width and height of photo to csumb-ify
  w, h = getWidth(pic), getHeight(pic)
  # create scanlines using the height and width dimensions
  overlay = scanlines(pic)
  target = blend(pic, overlay)
  show(target)
  return target
  
def blend(pic, pic2):
   w, h = getWidth(pic), getHeight(pic)
   target = makeEmptyPicture(w,h)
   for x in range(w):
    for y in range(h):
      px = getPixel(target, x, y)
      pic_px = getPixel(pic, x, y)
      pic2_px = getPixel(pic2, x, y)
      
      pic_r, pic_g, pic_b = getRed(pic_px), getGreen(pic_px), getBlue(pic_px)
      pic2_r, pic2_g, pic2_b =getRed(pic2_px), getGreen(pic2_px), getBlue(pic2_px)
      r = (pic_r + pic2_r) / 2
      g = (pic_g + pic2_g) / 2
      b = (pic_b + pic2_b) / 2
      setColor(px, makeColor(r,g,b))
   return target 

def makeGradient(canvas):
   widthCanvas = getWidth(canvas) 
   heightCanvas = getHeight(canvas)
   
   # bayBlue = makeColor(0, 42, 78)
   # define the red, green, blue starting values - bay blue
   r=0
   g=42
   b=78
   
   # valleyGreen = makeColor(8, 90, 55)
   # define the red, green, blue ending values - valley green
   r_final=8
   g_final=90
   b_final=55
   
   # define the width of each rectangle
   rectWidth = 2
   
   # define the color increment (amount to add) 
   # based on number of rectangles drawn on the canvas
   ratio = float(rectWidth)/widthCanvas
   ri = (0-8)*ratio
   gi = abs(42-90)*ratio
   bi = abs(78-55)*ratio
   

   for x in range(0, widthCanvas, rectWidth): 
       color=makeColor(r,g,b)     
       addRectFilled(canvas, x, 0, rectWidth, heightCanvas, color)
       if(r < r_final):
         r=r+ri
       if(g < g_final):
         g=g+gi  
       if(b < b_final):    
         b=b+bi
   return canvas
   
def drawOtter(pic):
  otter = getPic()
  x = getWidth(pic) - getWidth(otter)
  y = getHeight(pic) - getHeight(otter)
  for x1 in range(getWidth(otter)):
    for y1 in range(getHeight(otter)):
      if(getColor(getPixel(otter,x1,y1)) != white):
        setColor(getPixel(pic, x1 + x, y1 + y), getColor(getPixel(otter, x1,y1)))
        
  return pic

# Given a picture, produce a new picture
# With the same dimensions with scanlines.
# Return the scanline picture.   
def scanlines(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width, height)
  rectHeight = 1
  for y in range(0, height):
    if y % 4 ==0:
      addRectFilled(canvas, 0, y, width, rectHeight, black)
  return canvas
      
      
  