# Sara Kazemi and Cody Young
# CST 205 Midterm

# CSUMB filter and VHS filter


import random
import datetime


# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  
#--------------------------------------------------------------------------------#   
# CSUMB: 
# Create a gradient effect on the original photo, from bay blue to valley green 
# and superimposes an image of a pixelated otter at the bottom of the photo.   
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

  
#--------------------------------------------------------------------------------#    
# VHS:
# First under or overexposes by lightening and darkening pixels based on luminance
# values. Then, writes the current date and time to the bottom left corner of
# the photo. Finally, generates a picture of programmatically generated scanlines
# and blends the two photos together.
def vhs(pic):
  # get width and height of photo to csumb-ify
  w, h = getWidth(pic), getHeight(pic)
  # create scanlines using the height and width dimensions
  lofi(pic)
  setTimeAndDate(pic)
  overlay = scanlines(pic)
  target = blend(pic, overlay)
  show(target)
  return target

  
# VHS Filter 
# Adds a vintage VHS effect to an image. Looks lo fi on purpose.
def lofi(pic):
  pixels = getPixels(pic)
  for p in pixels:
    #Desaturate pixels
    setColor(p, makeLighter(getColor(p)))
    #Lighten or darken each pixel based on luminance. Simulates under/overexposure.
    luminance = (getRed(p) * 0.299 + getGreen(p) * 0.587 + getBlue(p) * 0.114)
		
    # Darkens pixels with lighter luminance values and lightens pixels with darker luminance values
    if(luminance >= 163):
      setColor(p, makeDarker(getColor(p)))
    elif(luminance <= 93):
      setColor(p, makeLighter(getColor(p)))
  return pic
    
def setTimeAndDate(pic):

  #Set height and width of time stamp relative to height and width of source picture.
  height = getHeight(pic)
  width = getWidth(pic)
  #Time/date stamp height, width, font size 
  x_position = int (width / 100)
  y_position = height - (height / 9)
  fontsize = (height / 10)
		
  #Time stamp - relative to source picture
  time_stamp = datetime.datetime.now().strftime("%I:%M %p")
  #Date stamp - relative to time stamp position
  date_stamp = datetime.datetime.now().strftime("%b.%d,'%y")
  ds_position = int(y_position + fontsize)
		
  #Add time and date stamps
  addTextWithStyle(pic, x_position, y_position, time_stamp, makeStyle(mono,bold,fontsize),white)
  addTextWithStyle(pic, x_position, ds_position, date_stamp, makeStyle(mono,bold,fontsize),white)
  return pic   

  
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
      
      
  