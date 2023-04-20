# functions.py
from PIL import Image
import json
def decrypt_file():
    # read the encrypted JSON file
    with open('../EncryptedGroupHints Spring 2023 Section 001.json') as f:
        encrypted_data = json.load(f)
        encrypted_data = encrypted_data['Sawao Kato']
        return encrypted_data
def encrypted_txt(encrypted_data):
    with open('../English.txt') as f:
        english_txt = [num for num in f.read().split()]
        decrypted_str = ''
    for num in encrypted_data:
        decrypted_str += english_txt[int(num)-1].strip() + " "  # subtract 1 since indices are 1-based in encrypted data

    return decrypted_str

def load_image( filename ) :
    # Error handling
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        # It's not good to print here. The UI might be messed up
        # print("Unable to open", filename)
        # "Raise an exception" instead
        raise Exception("Unable")
        return None     # Not much else to do
    return myimage
