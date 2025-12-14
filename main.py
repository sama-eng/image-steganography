from helper import (file_exists, get_file_extension, read_image_size, calc_max_steg_size)
from Encode import (encode_message)
from Decode import(decode_message)
def main():
    print("\n============================================")
    print("   Welcome to image steganography tool :) ")
    print("==============================================\n")

    print("Please provide the path to your image (PPM format ONLY (P3)).")
    print(" OR drag and drop the PPM file \n")

    while True: 
       image_path = input("Enter or drag the path to your PPM image: ").strip()
       
       if not file_exists(image_path):
           print("ERROR: File not found. Please try again. \n")
           continue
       
       extension = get_file_extension(image_path).lower()
       if extension != "ppm":
           print("ERROR: Unsupported format. Only PPM are allowed. \n")
           print("Please convert your image to PPM format and try again.")
           continue
       
       break

    width,height = read_image_size(image_path)
    max_chars = calc_max_steg_size(width, height)

    print("Image Loaded Successfully!")
    print("File:", image_path)
    print(f"Size: {width} x {height}")
    print(f"Max Steganography Size {max_chars}")

    while True:
        print("Choose an option:")
        print("1. Hide a message")
        print("2. Extract a message")
        print("3. Change image")
        print("4. Exit program")
        choice: str = input("Enter 1, 2, 3, or 4: ").strip()
    
        if choice == "1":
            encode_message(image_path)  
        elif choice == "2":
            decode_message(image_path)
        elif choice == "3":
            while True:
                image_path = input("Enter or drag the path to your new PPM image: ").strip()
                if not file_exists(image_path):
                    print("ERROR: File not found. Please try again.\n")
                    continue
                extension = get_file_extension(image_path).lower()
                if extension != "ppm":
                    print("ERROR: Only PPM images allowed. Convert and try again.\n")
                    continue
                width, height = read_image_size(image_path)
                max_chars = calc_max_steg_size(width, height)
                print("\nNew Image Loaded Successfully!")
                print("File:", image_path)
                print(f"Size: {width} x {height}")
                print(f"Max Steganography Size: {max_chars}\n")
                break
        elif choice == "4":
            print("\nProgram finished.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()