
#py -m pip install pillow
#py script.py read kat.png

import os
import sys
from PIL import Image

def read_bit(img: Image.Image, offset: int) -> int:
    pixel = offset // 3
    bit = offset % 3
    x = pixel % img.width
    y = pixel // img.width
    return img.getpixel((x, y))[bit] & 1

def write_bit(img: Image.Image, offset: int, value: int) -> int:
    pixel = offset // 3
    bit = offset % 3
    x = pixel % img.width
    y = pixel // img.width
    rgb = list(img.getpixel((x, y)))
    rgb[bit] &= 0xfe
    rgb[bit] |= value & 1
    img.putpixel((x, y), tuple(rgb))

def read_bits(img: Image.Image, offset: int, bits: int) -> int:
    val = 0
    for i in range(bits):
        read_bit(img, offset + i)
        val |= (read_bit(img, offset + i) << (bits - i - 1))
    return val

def write_bits(img: Image.Image, offset: int, bits: int, value: int):
    for i in range(bits):
        write_bit(img, offset + i, (value >> (bits - i - 1)) & 1)


file = None
read = False
write = None

if len(sys.argv) < 3:
    raise Exception('Invalid arguments.')

mode = sys.argv[1].lower()
infile = sys.argv[2]

if mode != 'read' and mode != 'write':
    raise Exception('Invalid mode specified. Must be read/write.')

if not os.path.exists(infile):
    raise Exception('Input file does not exist.')

img = Image.open(infile)
rgb = img.convert('RGB')

if mode == 'read':
    size = read_bits(rgb, 0, 16)
    msg = ''
    for i in range(size):
        msg += chr(read_bits(rgb, 16 + i * 8, 8))
    print(msg)
elif mode == 'write':
    if len(sys.argv) < 5:
        raise Exception('Must specify an output file and message.')
    outfile = sys.argv[3]
    msg = sys.argv[4]
    write_bits(rgb, 0, 16, len(msg))
    for i in range(len(msg)):
        write_bits(rgb, 16 + 8 * i, 8, ord(msg[i]))
    rgb.save(outfile)