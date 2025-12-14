def encode_message(image_path):
    """
    Hide a message inside a PPM (P3) image.
    Modifies the original image to embed the message.
    """
    with open(image_path, 'r') as f:
        lines = f.readlines()

    content = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

    if content[0] != 'P3':
        print("Unsupported PPM format. Only P3 supported.")
        return

    width, height = map(int, content[1].split())
    max_color = int(content[2])
    pixel_values = []
    for line in content[3:]:
        pixel_values.extend(line.split())
    pixel_values = [int(x) for x in pixel_values]

    message = input("Enter the message to hide: ")
    if len(message) == 0:
        print("No message entered. Aborting.")
        return
    
    binary_message = ''.join([format(ord(c), '08b') for c in message])
    binary_message += '00000000' 

    required_bits = len(binary_message)
    available_bits = len(pixel_values)


    if required_bits > available_bits:
        extra_bits = required_bits - available_bits
        extra_pixels = (extra_bits + 2) // 3
        new_height = height + (extra_pixels // width) + 1
        added_pixels = (new_height * width) - (width * height)
        for _ in range(added_pixels * 3):
            pixel_values.append(0)

        height = new_height

        print("Image extended to fit the message.")

        
    for i in range(len(binary_message)):
        pixel_values[i] = (pixel_values[i] & ~1) | int(binary_message[i])

    with open('encoded_image.ppm', 'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write(f'{max_color}\n')
        for i in range(0, len(pixel_values), 3):
            f.write(f'{pixel_values[i]} {pixel_values[i+1]} {pixel_values[i+2]}\n')
    print("Message hidden successfully!")
    print("Saved as 'encoded_image.ppm'")
    