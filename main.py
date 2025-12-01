from helper import (file_exists, get_file_extension, read_image_size, calc_max_steg_size)


def main():
    print("\n==================================")
    print("   Welcome to image steganography tool :) ")
    print("==================================\n")

    print("Please provide the path to your image (PPM format ONLY).")

    while True: 
       image_path = input("Enter or drag the path to your PPM image: ").strip()
       
       if not file_exists(image_path):
           print("ERROR: File not found. Please try again. \n")
           continue
       
       extension = get_file_extension(image_path).lower()
       if extension != "ppm":
           print("ERROR: Unsupported format. Only PPM are allowed. \n")
           continue
       
       break

    width,height = read_image_size(image_path)
    max_chars = calc_max_steg_size(width, height)

    print("\n-------------------------------")
    print("Image Loaded Successfully!")
    print("File:", image_path)
    print(f"Size: {width} x {height}")
    print(f"Max Steganography Size {max_chars}")
    print("-------------------------------\n")