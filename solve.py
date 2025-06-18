import numpy as np
from PIL import Image as im

# For your convenience - 700 worked well for me
IMAGE_SIZE = 700
MAX_BRIGHTNESS = 255
NUM_COLORS = 3

def square(img_arr):
    offset = (img_arr.shape[1] - img_arr.shape[0])//2
    return img_arr[:, offset:-offset, :]

def resize(img_arr):
    scale = img_arr.shape[0] / IMAGE_SIZE
    new_arr = np.ones([IMAGE_SIZE,IMAGE_SIZE,NUM_COLORS]).astype(np.uint8)
    for i in range(IMAGE_SIZE):
        for j in range(IMAGE_SIZE):
            new_arr[i][j] = img_arr[int(i*scale)][int(j*scale)]
    return new_arr

def read_rgbs():
    colors, rgbs = [], []
    for line in open("rgbs.csv"):
        colors.append(line.split()[0])
        rgbs.append(line.split()[1:])
    return colors, np.array(rgbs).astype(np.uint8)

def img_file(color, rgb):
    img_arr = np.array(im.open("imgs/" + color + ".png"))
    img_arr = resize(square((img_arr)))
    img_arr = colorscale(img_arr, rgb)
    return img_arr

def luminence(color):
    r, g, b = color//8
    return (4*g + 3*r+b)

def colorscale(img_arr, rgb):
    for i in range(IMAGE_SIZE):
        for j in range(IMAGE_SIZE):
            lum = luminence(img_arr[i][j])
            for k in range(NUM_COLORS):
                img_arr[i][j][k] = int(lum/255 * rgb[k])
    return img_arr

def get_colors(img_arr, region):
    offset = {"Qullasuyu": 3, "Antisuyu": 4, "Kuntisuyu": 2, "Chinchaysuyu": 0}[region]
    colors, rgbs = read_rgbs()
    pixels = [img_file(colors[i], rgbs[i]) for i in range(len(rgbs))]
    for i in range(IMAGE_SIZE):
        for j in range(IMAGE_SIZE):
            img_arr[i][j] = pixels[(i//100 - j//100 + offset) % len(rgbs)][i][j]
    return img_arr

# Main Function
def flag(region):
    # Create an image array array IMAGE_SIZE pixels by IMAGE_SIZE pixels by NUM_COLORS colors
    img_arr = np.ones([IMAGE_SIZE,IMAGE_SIZE,NUM_COLORS]).astype(np.uint8)
    # Set all colors in the image array
    img_arr = get_colors(img_arr, region)
    # Convert the array to an image
    img = im.fromarray(img_arr)
    # Save the image as "flag.png"
    img.save("flag.png")

flag('Qullasuyu')