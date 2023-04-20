# Name: Sawao Kato - Anna Hauer, Brooke Pohlman, Riley Clayton, and Sabrina Harrington
# email: hauerac@mail.uc.edu, pohlmabe@mail.uc.edu, claytorm@mail.uc.edu, & harrinsr@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Our team collaborated to develop an Eclipse application and went on a scavenger hunt.
# Citations:
# Anything else that's relevant: Group Assignment

# main.py
from PIL import Image
import json
from functionsPackage.functions import *

secretAnswer = encrypted_txt(decrypt_file())
print(secretAnswer)

im = Image.open("../photo1.jpg")
print(im.width, im.height, im.mode, im.format)  # Display some info about the image

my_image = load_image("../photo1.jpg")
try:
    print(type(my_image))
    my_image.show(my_image)
except Exception as e:
    # Print the message in the exception raised by load_image
    print(e)
