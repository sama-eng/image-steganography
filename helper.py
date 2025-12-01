
def file_exists(path):
    """Return True if the file exists, else False."""
    try:
        with open(path, 'rb'):
            return True
    except FileNotFoundError:
        return False


def get_file_extension(path):
    """Return the file extension of the given file path."""
    if '.' in path:
        return path.rsplit('.', 1)[-1]
    return ''

def read_image_size(path):
    """Reads width and height from a PPM (P3) image file.
    Returns (width, height)"""

    try:
        with open(path, 'r') as f:
            lines = f.readlines()

        content = [line.strip() for line in lines if line.strip() and not line.startswith('#')]

        if content[0] != 'P3':
            raise ValueError("Unsupported PPM format. Only P3 supported.")

        dimensions = content[1].split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        return width, height

    except Exception as e:
        print("Error reading image size:", e)
        return 0, 0
    
def calc_max_steg_size(width, height):
    """
    Calculates maximum number of characters that can be hidden in the image
    using LSB logic (1 character = 8 bits, 3 channels RGB per pixel).
    """
    if width == 0 or height == 0:
        return 0
    return (width * height * 3) // 8