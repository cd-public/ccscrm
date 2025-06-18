import numpy as np
from PIL import Image as im

# For your convenience - 700 worked well for me
IMAGE_SIZE = 700
MAX_BRIGHTNESS = 255
NUM_COLORS = 3

def get_colors(img_arr, region):
    return img_arr * MAX_BRIGHTNESS

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