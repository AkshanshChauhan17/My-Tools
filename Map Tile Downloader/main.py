from comps import get_tile
import sys

if len(sys.argv) < 4:
    print("Null")
else:
    x_inp = int(sys.argv[1])
    y_inp = int(sys.argv[2])
    z_inp = int(sys.argv[3])
    index = 0
    for x in range(2):
        for y in range(2):
            index = index + 1
            x = x + x_inp
            y = y + y_inp
            get_tile.display_image_from_url(f"https://mts1.google.com/vt/lyrs=m@186112443&hl=x-local&src=app&x={x}&y={y}&z={z_inp}", index)