from helper import (file_exists, get_file_extention)


def main():
    print("\n==================================")
    print("   Welcome to image steganography tool :) ")
    print("==================================\n")

    print("Please provide  the path to your image (PPM format ONLY).")

    while True: 
       image_path = input("Enter or drag the path to your PPM image: ").strip()
       
       if not file_exists(image_path):
           print("ERROR: File not found. Please try again. \n")
           continue
       
       extension = get_file_extention(image_path).lower()
       if extension != "ppm":
           print("ERROR: Unsupported format. Only PPM are allowed. \n")
           continue
       
       break