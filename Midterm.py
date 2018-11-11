# Run the main method
# change output directory to desired path on your machine

## Output directory
dir = ""

## main method
def main():
  writePict(removeRedEye(getPic(), 322, 995, 385, 465), dir + "/noredeye.jpg")
  writePict(sepia(getPic()), dir + "/sepia.jpg")
  writePict(artify(getPic()), dir + "/artify2.jpg")
  writePict(chromaKey(getPic(), getPic()), dir + "/greenscreen2.png")


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
  #create canvas using the height and width dimensions
  target = makeEmptyPicture(w, h)
  for x in range(w):
    for y in range(h):
      px = getPixel(target, x, y)
      pic_px = getPixel(pic, x, y)
      grad_px = getPixel(gradient, x, y)
      
      pic_r, pic_g, pic_b = getRed(pic_px), getGreen(pic_px), getBlue(pic_px)
      grad_r, grad_g, grad_b =getRed(grad_px), getGreen(grad_px), getBlue(grad_px)
      r = (pic_r + grad_r) / 2
      g = (pic_g + grad_g) / 2
      b = (pic_b + grad_b) / 2
      setColor(px, makeColor(r,g,b))  
  drawOtter(target)      
  
  
  show(target)
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
  
  