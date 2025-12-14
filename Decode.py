# Decode.py
# Extracts hidden messages from a PPM image using LSB

def decode_message(image_path):
    """
    Extract a hidden message from a PPM (P3) image using LSB.
    """

    # --- Read PPM image ---
    with open(image_path, 'r') as f:
        lines = f.readlines()
    content = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

    if content[0] != 'P3':
        print("Unsupported PPM format. Only P3 supported.")
        return

    # --- Extract all pixel values ---
    pixel_values = [int(x) for line in content[3:] for x in line.split()]

    # --- Read LSBs to get bits of the message ---
    bits = [str(x & 1) for x in pixel_values]

    # --- Convert bits to characters until null byte ---
    message = ''
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(''.join(byte), 2))
        if char == '\x00':
            break
        message += char

    print("Hidden message extracted:")
    print(message)
    return message
