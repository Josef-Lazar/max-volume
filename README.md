# max-volume
This program tries to find the dimensions of a box with the greates volume, whose surface area doesn't excede 1000 cm^2, and whose sides are all equal to an integer amount of cm


The program starts by setting the width and height of the box to 1 and setting the depth to the maximum amount possible that doesn't excede the surface area limitation. (1\*1\*249)

It then calculates the dimensions of a new box whose width is 2 and height is 1. The depth calculation remains the same. (1\*2\*166)

The program continues to make new boxes expanding the width, so long as its value does not exced that of the depth.

When it comes to this point, it increases the height by 1 and sets the value of width to the new height value. (21\*1\*21) -> (2\*2\*124)

When the width and depth match, it sets the width to the new icreased height instead of setting it to 1, so that it doesn't repeat previous dimensions in a rearanged order. (8\*5\*35) x (5\*8\*35)

Each time it makes a new box it checks to see if the volume is larger than in any previous generation, and if it is, it overwrites the previous max volume dimensions.

The depth is always the longest dimension (except when tied with width) and height is always the shortes dimension (also except when tied with width). (17\*6\*17) (7\*7\*32)

The height continue to grow, while the depth continues to contract until the two are equal. At this point every possible box shapes that uses all (or close to all) the surface area has been tested.

It then prints the dimensions of the box with the greates volume.


The program also includes a function called boxcalc(#, #, #) which takes in the dimensions of a six sided box and returns the surface and volume of that box.
