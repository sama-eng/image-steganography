# Encode.py
# Handles hiding a message inside a PPM image using LSB steganography

def encode_message(image_path):
    """
    Hide a message inside a PPM (P3) image.
    Supports dual input: typed or from text file.
    Automatically extends image if message is too long.
    """

    # --- Dual input: type message or provide text file ---
    while True:
        print("\nHow do you want to provide the message?")
        print("1. Type message manually")
        print("2. Provide a text file")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            message = input("Enter the message to hide: ")
            break
        elif choice == "2":
            file_path = input("Enter the path to the text file: ").strip()
            try:
                with open(file_path, 'r') as f:
                    message = f.read()
                break
            except FileNotFoundError:
                print("File not found. Try again.")
        else:
            print("Invalid choice. Enter 1 or 2.")

    if len(message) == 0:
        print("No message provided. Aborting.")
        return

    # --- Read PPM image ---
    with open(image_path, 'r') as f:
        lines = f.readlines()
    content = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

    if content[0] != 'P3':
        print("Unsupported PPM format. Only P3 supported.")
        return

    width, height = map(int, content[1].split())
    max_color = int(content[2])
    pixel_values = [int(x) for line in content[3:] for x in line.split()]

    # --- Convert message to binary and add null byte as delimiter ---
    binary_message = ''.join(format(ord(c), '08b') for c in message) + '00000000'

    # --- Check if image is big enough, extend if necessary ---
    required_bits = len(binary_message)
    available_bits = len(pixel_values)
    if required_bits > available_bits:
        extra_bits = required_bits - available_bits
        extra_pixels = (extra_bits + 2) // 3
        new_height = height + (extra_pixels // width) + 1
        added_pixels = (new_height * width) - (width * height)
        pixel_values.extend([0] * (added_pixels * 3))
        height = new_height
        print("Image extended to fit the message.")

    # --- Encode message in LSB of pixel values ---
    for i in range(len(binary_message)):
        pixel_values[i] = (pixel_values[i] & ~1) | int(binary_message[i])

    # --- Write encoded image to new file ---
    with open('encoded_image.ppm', 'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write(f'{max_color}\n')
        for i in range(0, len(pixel_values), 3):
            f.write(f'{pixel_values[i]} {pixel_values[i+1]} {pixel_values[i+2]}\n')

    print("Message hidden successfully!")
    print("Saved as 'encoded_image.ppm'")
