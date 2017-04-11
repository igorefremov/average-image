from PIL import Image

import sys
import os


def average_pixels(image_data, width, height, x, y, radius):
    startx = x - radius
    endx = x + radius + 1
    starty = y - radius
    endy = y + radius + 1

    averages = [0, 0, 0]
    avg_r = 0
    avg_g = 0
    avg_b = 0
    pixels_read = 0

    for i in range(max(0, startx), min(width - 1, endx)):
        for j in range(max(0, starty), min(height - 1, endy)):
            pixels_read += 1
            pixel_data = image_data[j][i]

            avg_r += pixel_data[0]
            avg_g += pixel_data[1]
            avg_b += pixel_data[2]
    
    d = float(pixels_read)
    a = (float(avg_r) / d, float(avg_g) / d, float(avg_b) / d)
    return (int(a[0]), int(a[1]), int(a[2]))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print "Usage: %s <input> <output> <radius> <iterations>" % sys.argv[0]
        sys.exit(1)


    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    radius = int(sys.argv[3])
    iterations = int(sys.argv[4])

    if not os.path.exists(input_image_path):
        print "Error: image \"%s\" does not exist" % input_image_path
        sys.exit(2)

    if radius < 1:
        print "Error: invalid radius"
        sys.exit(3)

    if iterations < 1:
        print "Error: invalid iterations"
        sys.exit(4)
    

    input_image = Image.open(input_image_path).convert("RGB")   
    width = input_image.size[0]
    height = input_image.size[1]
    print "Opened image of size %d x %d pixels" % (width, height) 


    print "Converting data"
    input_image_data = input_image.getdata()
    image_data = []
    count = 0
    row = []
    for b in input_image_data:
        row.append(b)
        count += 1
        if count == width:
            image_data.append(row)
            row = []
            count = 0
            
            print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b%.02f%% complete" % (float(len(image_data) * 100) / float(height)),
            sys.stdout.flush()
    print ""
    sys.stdout.flush()
    input_image_data = image_data


    print "Applying transformation"
    for i in range(0, iterations):
        output_image_data = []
        for y in range(0, height):
            row = []
            for x in range(0, width):
                row.append(average_pixels(input_image_data, width, height, x, y, radius))
                
            output_image_data.append(row)
            print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\bIteration %d - %.02f%% complete" % (i + 1, (float(y * 100) / float(height))),
            sys.stdout.flush()

        input_image_data = output_image_data
    print ""
    
    
    print "Writing new image to \"%s\"" % output_image_path
    sys.stdout.flush()

    output_image = Image.new("RGB", (width, height))
    for x in range(0, width):
        for y in range(0, height):
            output_image.putpixel((x, y), input_image_data[y][x])

    output_image.save(output_image_path)
    print "Done!"