from PIL import Image, ImageDraw, ImageWin, ImageOps
import os
import shutil

members = 65
tick = 0
bigarr = []
smallarr = []
for i in range(members):
    smallarr.append(f"RoboCodes/robocode{i}.png")
    if len(smallarr) == 8:
        bigarr.append(smallarr)
        smallarr = []

coords = [0, 250, 500, 750]
border = (5, 5, 5, 5)
x = 0
for i in bigarr:
    canvas = Image.new("RGB", (816, 1054), (255, 255, 255))
    count = 0
    for j, coord in zip(i, coords):
        code = Image.open(j)
        code = ImageOps.expand(code, border=border, fill=(0, 0, 0, 255))
        canvas.paste(code, (0, coord))
        count += 1
        if count == 4:
            break
    for j, coord in zip(i[4:], coords):
        code = Image.open(j)
        code = ImageOps.expand(code, border=border, fill=(0, 0, 0, 255))
        canvas.paste(code, (400, coord))

    canvas.save(f"robocodesheet{x}.png")
    shutil.move(f"robocodesheet{x}.png", f"RoboCodeSheets/robocodesheet{x}.png")
    x += 1