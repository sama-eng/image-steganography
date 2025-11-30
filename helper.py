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