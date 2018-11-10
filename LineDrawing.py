# Run the main method
# change output directory to desired path on your machine

## Output directory
dir = ""

## main method
def main():
  writePict(lineDrawing(getPic()), "/output.jpg")

# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  
   
def lineDrawing(pic):
  DIFFERENCE = 10
  # Take a color picture and convert it to black and white
  betterBnW(pic) 
  # For each pixel in the picture, 
  # compare the luminance of that pixel to the luminance of the pixels to 
  # both the pixels below it and to the right.
  for x in range(0, getWidth(pic) - 1):
    for y in range(0, getHeight(pic) - 1):
      # If there is a large enough difference in the luminance between 
      # your pixel and BOTH the pixels to the right and below, 
      # then make your pixel black.  
      if( ( distance(getColor(getPixel(pic, x, y)), getColor(getPixel(pic, x + 1, y)) ) > DIFFERENCE ) and 
          ( distance(getColor(getPixel(pic, x, y)), getColor(getPixel(pic, x, y + 1) )) > DIFFERENCE ) ):
        setColor(getPixel(pic, x, y), black)
      #Otherwise, make your pixel white. 
      else:
        setColor(getPixel(pic, x, y), white)
  show(pic)      
  return pic

def lineDrawingLambda(pic, DIFFERENCE):

  # For each pixel in the picture, 
  # compare the luminance of that pixel to the luminance of the pixels to 
  # both the pixels below it and to the right.
  for x in range(0, getWidth(pic) - 1):
    for y in range(0, getHeight(pic) - 1):
       
      px = getPixel(pic, x, y) #pixel to change
      right = getPixel(pic, x+1, y) #pixel to right
      below = getPixel(pic, x, y+1) #pixel below
      
      #calculate the luminance of the three pixels
      luminance = lambda px: (getRed(px) * 0.299) + (getGreen(px) * 0.587) + (getBlue(px) * 0.114)
      
      lp = luminance(px)
      lr = luminance(right)
      lb = luminance(below)
      
      # If there is a large enough difference in the luminance between 
      # your pixel and BOTH the pixels to the right and below, 
      # then make your pixel black. 
      if( (abs(lp - lr ) > DIFFERENCE) and (abs(lp - lb ) > DIFFERENCE) ):
        setColor(px, black)
      #Otherwise, make your pixel white. 
      else:
        setColor(px, white)
  show(pic)      
  return pic
  
# improved grayscale function using weights  
def betterBnW(pic):
   pixels = getPixels(pic)
   for p in pixels:
      # Find opposite of color by subtracting from max and multiply by weight
      luminance =  ((getRed(p) * 0.299) + (getGreen(p) * 0.587) + (getBlue(p) * 0.114))
      setColor(p, makeColor(luminance, luminance, luminance))
  # show(pic)
   return pic
    
     

  
  