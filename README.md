# Image Downloader Script MVP

An MVP solution for image downloader script.
It expects a plain text file with a list of urls and downloads every valid image to the local hard drive.


## Getting Started

The necessary commands to run the script and to clean up commands are defined in the `Makefile`.


### Usage

Dockerized solution is recommended and offered to support portability. The script can also be directly executed without 
any problem in any machine where Python 3 is installed. 
The command below will trigger download of the images for a given file through a docker container.
```bash
make download-images file-name=<file_name>
```

an example command:

```bash
make download-images file-name=list_of_images.txt
```

to run it directly as a script:

```bash
python downloader.py list_of_images.txt
```


## Running the tests

To run all the test 

```bash
pip install -r requirement_dev.txt
pytest
```

There is also `file_generator.py` script which I used to generate a plain text file for mocking / testing purposes.
It uses https://placekitten.com/ and creates 20 urls by default.


### Architecture Flow

![image](https://user-images.githubusercontent.com/8826542/203024752-50f65635-c114-4d0c-bffd-1ff5ef332c07.png)

### Performance Benchmarking

CPU: 8

10 Images => 2.305503206 seconds

100 Images => 24.489661488 seconds

### Assumptions / Limitations

- It is assumed that all the files will be downloaded under the file called /images/ in the repository
- Numbers of workers for Multithreading cannot be arranged by the users. Script itself calculates 
  it via checking the number of CPUs in the running system.
- Images are stored as .jpeg files by default
- There is no storage limitation. There is only a timeout error.


### Possible Improvements after MVP

- Enable users to store images in any given folder path or even in cloud (S3 buckets, etc...)
- Improve the test coverage with more unit tests and even E2E via connecting to internet
- Create with-image-validation optional argument to validate if the given url is a downloadable image
- Show the current status via progress bar in the terminal (i.e: 3/81 images are downloaded)
- Implement a persistent cache. Already downloaded images should not be downloaded again
- Add options for the number of workers, max storage size, and timeout value
