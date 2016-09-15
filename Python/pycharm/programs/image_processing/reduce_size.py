import Image
import glob

path = glob.glob("*.jpg")   # read all the .JPG file

for i in range(len(path)):
    im = Image.open(path[i])    # open image using PIL library
    print path[i]
    print im.format, im.size, im.mode

    new_size = tuple([int(x*0.5) for x in im.size])  # scale down size by 0.5 from original size
    im_new_size = im.resize(new_size)     # create image using new file size
    im_new_size.save(path[i])

