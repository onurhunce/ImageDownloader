MINIMUM_IMAGE_SIZE = 720  # pixels
WEB_SITE_URL = "https://placekitten.com/"
NUMBER_OF_IMAGES = 10


def generate_file_with_image_urls(number_of_images: int) -> None:
    with open("list_of_images.txt", "w") as text_file:
        for i in range(number_of_images):
            text_file.write(f"{WEB_SITE_URL}{MINIMUM_IMAGE_SIZE + i} ")


if __name__ == "__main__":
    generate_file_with_image_urls(number_of_images=NUMBER_OF_IMAGES)
