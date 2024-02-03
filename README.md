# Dockerized Flask Image Processing App

This repository contains a simple Flask application that allows users to upload images, processes them, and generates thumbnails. The application is Dockerized and uses a tmpfs mount for temporary thumbnail storage.

## Prerequisites

- Docker installed on your machine.

## Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:mili-sucevic/hitc-tmpfs-mount-demo.git
   cd hitc-tmpfs-mount-demo

2. Build the Docker image:

    ```bash
    docker build -t image-processing-app .

3. Run the Docker container:

    ```bash
    docker run -d --name image-processing-container --tmpfs /tmp/cache:rw -p 8080:8080 image-processing-app

4. Access the web app at http://localhost:8080

5. Upload an image:
- Click on the "Upload Image" button.
- Choose an image file and click "Upload."

6. Check the logs - If there are any issues, you can check the container logs for debugging:

    ```bash 
    docker logs image-processing-container

7. Inspect tmpfs mount - You can also inspect the contents of the tmpfs mount:

    ```bash
    docker exec -it image-processing-container /bin/bash
    ls /tmp/cache

8. Also, check if the original image is saved in the /app/uploads directory:

    ```bash
    ls /app/uploads

9. While inside the container, check if there are any additional logs that might provide insights:

   ```bash
   cat /app/logs/*.log

## Notes
This application is for demonstration purposes and uses a tmpfs mount for temporary thumbnail storage.
