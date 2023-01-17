import cImage as image


# -------------------------------
# EXAMPLE PROGRAM #1: RED FILTER
# -------------------------------

# create image object and copy
img = image.Image('crayons.gif')
red_only_img = img.copy()

# get dimensions
w = img.getWidth()
h = img.getHeight()

# loop over every (x,y) pair
for x in range(w):
    for y in range(h):
        
        # filter out green and blue
        pixel = img.getPixel(x, y)
        red = pixel.getRed()
        redPixel = image.Pixel(red, 0, 0)
        red_only_img.setPixel(x, y, redPixel)

# save the new image and display both
red_only_img.save('red_crayons.gif')
win = image.ImageWin("Red Only", w, h*2)
img.draw(win)
red_only_img.setPosition(0, h)
red_only_img.draw(win)
win.exitonclick()


# -------------------------------
# EXAMPLE PROGRAM #2: COPY TOP
# -------------------------------

# create image object and copy
img = image.Image('crayons.gif')
img_top_copy = img.copy()

# get dimensions
w = img.getWidth()
h = img.getHeight()

# loop over every x value...
for x in range(w):
    # ... but only loop over y values in top half
    for y in range(int(h/2)):
        
        # replace pixel in the bottom half with the
        # corresponding one from the top half
        pixel = img.getPixel(x, y)
        img_top_copy.setPixel(x, y + int(h/2), pixel)


# save the new image and display both
img_top_copy.save('copy_top.gif')
win = image.ImageWin("Top Copied", w, h*2)
img.draw(win)
img_top_copy.setPosition(0, h)
img_top_copy.draw(win)
win.exitonclick()
