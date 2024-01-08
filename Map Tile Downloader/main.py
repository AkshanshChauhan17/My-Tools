from comps import get_tile
import sys

if len(sys.argv) < 5:
    print("Null")
else:
    x_inp = int(sys.argv[1])
    y_inp = int(sys.argv[2])
    z_inp = int(sys.argv[3])
    l_inp = int(sys.argv[4])
    for y in range(0, l_inp):
        for x in range(0, l_inp):
            file_name = f"{x_inp}.{y_inp}.{z_inp}.png"
            get_tile.display_image_from_url(f"https://mts1.google.com/vt/lyrs=m@186112443&hl=x-local&src=app&x={x_inp}&y={y_inp}&z={z_inp}", file_name)
            x_inp = x_inp + 1
        y_inp = y_inp + 1