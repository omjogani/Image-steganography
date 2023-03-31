import numpy as np
from PIL import Image


class Decoding:
    def decode(src):
        img = Image.open(src, 'r')
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
            total_pixels = array.size // n
        elif img.mode == 'RGBA':
            n = 4
            total_pixels = array.size // n

        hidden_bits = ""
        for p in range(total_pixels):
            for q in range(0, 3):
                hidden_bits += (bin(array[p][q])[2:][-1])

        hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

        message = ""
        for i in range(len(hidden_bits)):
            if message[-5:] == "$t3g0":
                break
            else:
                message += chr(int(hidden_bits[i], 2))
        if "$t3g0" in message:
            print("Hidden Message:", message[:-5])
        else:
            print("No Hidden Message Found")


