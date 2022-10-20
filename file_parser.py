CHUNK_SIZE = 100


def rows(f, chunk_size=CHUNK_SIZE, separator=" "):
    """
    Usage:
    with open('image_urls.txt') as f:
        for r in rows(f):
    """
    row = ""
    while (chunk := f.read(chunk_size)) != "":  # End of file
        while (i := chunk.find(separator)) != -1:  # No separator found
            yield row + chunk[:i]
            chunk = chunk[i + 1:]
            row = ""
        row += chunk
    yield row


def read_urls_from_file(file) -> list:
    with open(file) as f:
        return [row for row in rows(f)]
