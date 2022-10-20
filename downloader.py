import urllib.request
import concurrent.futures
import sys

from file_parser import read_urls_from_file
from helpers import measure_time, hash_string
from validator import is_valid_url


IMAGE_STORAGE_FOLDER = "./images/"


def download_image(url: str, index: int) -> None:
    if is_valid_url(url=url):
        hashed_url = hash_string(string=url)
        file_name = f"./images/{hashed_url}_{index + 1}.jpeg"
        urllib.request.urlretrieve(url, file_name)


@measure_time
def download_images_from_file(urls: list) -> None:
    """
    Downloads images in multiple threads.
    ThreadPoolExecutor uses cpu_count + 4 for the number of max_workers
    # But it is limited to 32 to avoid consuming surprisingly large resource
    # on many core machine.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {
            executor.submit(download_image, url, index): url
            for index, url in enumerate(urls)
        }
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as exc:
                print(f"Error during multithreading for url: {url}. Error is: {exc}")


if __name__ == "__main__":
    image_file = sys.argv[1:][0]  # The file given by the user
    image_urls = read_urls_from_file(file=image_file)
    download_images_from_file(urls=image_urls)
