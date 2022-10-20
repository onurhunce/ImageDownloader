FROM python:3.9-slim-bullseye

WORKDIR /ImageDownloader

COPY . .

ENTRYPOINT ["python","downloader.py"]
