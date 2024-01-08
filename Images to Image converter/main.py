from PIL import Image
import sys
import glob
import os

if len(sys.argv) < 4:
    print("Null")
else:
    dims = sys.argv[1]
    path = sys.argv[2]
    fote = sys.argv[3]

    images = glob.glob(f"*.{fote}")

    os.chdir(fote)

    imgList = []
    i = 0
    per = 100

    for image in images:
        img = Image.open(image)
        imgList.insert(i, img)
        print((i/len(images))*100, "%")
        i = i + 1

    width, height = image1.size

    merged_image = Image.new("RGB", (width * 2, height))
    merged_image.paste(image1, (0, 0))
    merged_image.paste(image2, (width, 0))
    merged_image.save("merged_image.jpg")