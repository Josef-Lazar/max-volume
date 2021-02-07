import math

width = 1
hight = 1
depth = math.floor((500 - hight * width) / (hight + width))

volume = width * hight * depth
surface = 2 * hight * depth + 2 * hight * width + 2 * depth * width
print(f'''We are told to make a box using 1000 cm^2 of material, such that it has the greatest possible volume.
What lenght should the sides be, assumming they must be integers?

Starting values:
width: {width}
hight: {hight}
depth: {depth}
surface: {surface}
volume: {volume}
''')

while hight < depth:
    if width < depth:
        width += 1
        depth = math.floor((500 - hight * width) / (hight + width))
        if volume < width * hight * depth:
            print("w: " + str(width) + ", h: " + str(hight) + ", d: " +
              str(depth) + ", s: " +
              str(2 * hight * depth + 2 * hight * width + 2 * depth * width)
              + ", v: " + str(width * hight * depth) + " - new high")
            max_width = width
            max_hight = hight
            max_depth = depth
            max_surface = surface
            volume = width * hight * depth
        else:
            print("w: " + str(width) + ", h: " + str(hight) + ", d: " +
              str(depth) + ", s: " +
              str(2 * hight * depth + 2 * hight * width + 2 * depth * width)
              + ", v: " + str(width * hight * depth))
    else:
        width = hight
        hight += 1
        depth = math.floor((500 - hight * width) / (hight + width))

print(f'''
width: {max_width}
hight: {max_hight}
depth: {max_depth}
surface: {max_surface}
volume: {volume}
The box with the greatest volume will have sides the are {max_width}, {max_hight}, and {max_depth} cm long.

You can imput 'boxcalc(#, #, #)' to see the surface and volume of any other box''')

def boxcalc(x, y, z):
    print("surface: " + str(2 * x * y + 2 * x * z + 2 * y * z))
    print("volume:  " + str(x * y * z))
