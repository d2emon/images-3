import sys
import math
from PIL import Image, ImageOps
from numpy import asarray, mean, std


def main(input_file, output_file, mode):
    print("Loading image from {}...".format(input_file))
    image = Image.open(input_file)

    mode = int(mode)
    if mode == 0:
        pass
    elif mode == 1:
        image = image.convert('L')
    elif mode == 2:
        image = image.convert('1')
    elif mode == 3:
        image = ImageOps.invert(image)
    elif mode == 4:
        image = image.convert('L')
        data = image.getdata()
        new_data = [int(256 * math.log(1 + f / 256.0)) for f in data]
        image.putdata(new_data)
    elif mode == 5:
        image = image.convert('L')
        data = image.getdata()
        new_data = [int(256 * (f / 256.0) ** 0.5) for f in data]
        image.putdata(new_data)
    elif mode == 6:
        image = image.convert('L')
        data = image.getdata()
        new_data = [int(256 * (f / 256.0) ** 2) for f in data]
        image.putdata(new_data)
    image.show()
    image.save(output_file)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("images-3.py <inputfile> <outputfile> <mode>")
        sys.exit(0)

    main(*sys.argv[1:])
