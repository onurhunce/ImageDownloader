from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """
    A method to check if given string is constructed as a valid url.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])

    except ValueError:
        print(f"Given string: {url} is not a valid  url.")
        return False
