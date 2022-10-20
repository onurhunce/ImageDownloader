download-images:
	@docker build -t image-downloader .
	@docker run --name image-downloader-container -v $(shell pwd)/images:/ImageDownloader/images image-downloader $(file-name)

docker-clean-up: ## Remove the Docker container and the image
	@docker rm image-downloader-container
	@docker rmi image-downloader
