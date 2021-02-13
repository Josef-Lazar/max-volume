import math

width = 1
height = 1
depth = math.floor((500 - height * width) / (height + width))

volume = width * height * depth
surface = 2 * height * depth + 2 * height * width + 2 * depth * width
print(f'''We are told to make a box using 1000 cm^2 of material, such that it has the greatest possible volume.
What length should the sides be, assuming they must be integers?
Starting values:
width: {width}
height: {height}
depth: {depth}
surface: {surface}
volume: {volume}
''')

while height < depth:
    if width < depth and width + 1 != depth:
        width += 1
        depth = math.floor((500 - height * width) / (height + width))
        if volume < width * height * depth:
            print("w: " + str(width) + ", h: " + str(height) + ", d: " +
                  str(depth) + ", s: " +
                  str(2 * height * depth + 2 * height * width + 2 * depth * width)
                  + ", v: " + str(width * height * depth) + " - new max")
            max_width = width
            max_height = height
            max_depth = depth
            max_surface = surface
            volume = width * height * depth
        else:
            print("w: " + str(width) + ", h: " + str(height) + ", d: " +
                  str(depth) + ", s: " +
                  str(2 * height * depth + 2 * height * width + 2 * depth * width)
                  + ", v: " + str(width * height * depth))
    else:
        width = height
        height += 1
        depth = math.floor((500 - height * width) / (height + width))

print(f'''
width: {max_width}
height: {max_height}
depth: {max_depth}
surface: {max_surface}
volume: {volume}
The box with the greatest volume will have sides the are {max_width}, {max_height}, and {max_depth} cm long.
You can input 'boxcalc(#, #, #)' to see the surface and volume of any other box''')


def boxcalc(x, y, z):
    print("surface: " + str(2 * x * y + 2 * x * z + 2 * y * z))
    print("volume:  " + str(x * y * z))
