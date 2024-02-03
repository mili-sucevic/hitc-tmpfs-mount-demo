FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable to specify cache directory
ENV CACHE_DIR /tmp/cache

# Ensure the UPLOAD_FOLDER and THUMBNAIL_FOLDER exist
RUN mkdir -p /uploads /tmp/cache

EXPOSE 8080

CMD ["python", "app.py"]
