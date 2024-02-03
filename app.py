from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/app/uploads'
app.config['THUMBNAIL_FOLDER'] = '/tmp/cache'  # Using tmpfs for temporary storage

# Ensure the UPLOAD_FOLDER and THUMBNAIL_FOLDER exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['THUMBNAIL_FOLDER'], exist_ok=True)

def generate_thumbnail(original_path, thumbnail_path):
    # Load the original image
    original_image = Image.open(original_path)
    
    # Create and save a thumbnail
    thumbnail_image = original_image.copy()
    thumbnail_image.thumbnail((100, 100))
    thumbnail_image.save(thumbnail_path)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the original image
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(original_path)

        # Generate a unique name for the thumbnail
        thumbnail_filename = f"thumbnail_{file.filename}"
        thumbnail_path = os.path.join(app.config['THUMBNAIL_FOLDER'], thumbnail_filename)

        # Generate and save the thumbnail
        generate_thumbnail(original_path, thumbnail_path)

        return f'Success! Original image saved at: {original_path}, Thumbnail saved at: {thumbnail_path}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
