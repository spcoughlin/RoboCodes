from string import whitespace
from PIL import Image, ImageDraw, ImageWin
import os
import shutil

members = 65
cat = Image.open("catresized.png")

for i in range(members):
    im = Image.new("RGB", (320, 128), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    im.paste(cat, (0, 0, 64, 64))
    im.paste(cat, (256, 64, 320, 128))

    binary = '{:08b}'.format(i)
    ix = 0
    for digit in binary:
        if int(digit) == 1:
            if ix == 0:
                draw.rectangle([64, 0, 128, 64], fill=(0, 0, 0, 255))
            elif ix == 1:
                draw.rectangle([128, 0, 192, 64], fill=(0, 0, 0, 255))
            elif ix == 2:
                draw.rectangle([192, 0, 256, 64], fill=(0, 0, 0, 255))
            elif ix == 3:
                draw.rectangle([256, 0, 320, 64], fill=(0, 0, 0, 255))
            elif ix == 4:
                draw.rectangle([0, 64, 64, 128], fill=(0, 0, 0, 255))
            elif ix == 5:
                draw.rectangle([64, 64, 128, 128], fill=(0, 0, 0, 255))
            elif ix == 6:
                draw.rectangle([128, 64, 192, 128], fill=(0, 0, 0, 255))
            elif ix == 7:
                draw.rectangle([192, 64, 256, 128], fill=(0, 0, 0, 255))
        
        ix += 1

    im.save(f"robocode{i}.png")
    shutil.move(f"robocode{i}.png", f"C:/RoboCodes/robocode{i}.png")
