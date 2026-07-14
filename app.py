"""
Image Encryption & Decryption Web Application
Flask backend for processing image encryption/decryption operations.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import os
import uuid

from utils.encryption import encrypt_image, decrypt_image, validate_key, validate_image_format

app = Flask(__name__)
app.secret_key = "image-encryption-secret-key-2024"

# Configuration
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    """
    Home page route.
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    About page route.
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    Contact page route.
    """
    return render_template("contact.html")


@app.route("/process", methods=["POST"])
def process():
    """
    Process image encryption or decryption.
    """
    # Check if file is present
    if "image" not in request.files:
        flash("No file selected. Please upload an image.", "error")
        return redirect(url_for("home"))
    
    file = request.files["image"]
    
    # Check if filename is empty
    if file.filename == "":
        flash("No file selected. Please choose an image.", "error")
        return redirect(url_for("home"))
    
    # Validate file extension
    if not allowed_file(file.filename):
        flash("Invalid file type. Only PNG, JPG, and JPEG files are allowed.", "error")
        return redirect(url_for("home"))
    
    # Validate key
    try:
        key = int(request.form.get("key", 0))
    except (ValueError, TypeError):
        flash("Invalid key. Key must be an integer between 0 and 255.", "error")
        return redirect(url_for("home"))
    
    if not validate_key(key):
        flash("Key must be between 0 and 255.", "error")
        return redirect(url_for("home"))
    
    # Get operation type
    operation = request.form.get("operation", "encrypt")
    
    # Generate unique filename
    original_filename = secure_filename(file.filename)
    unique_filename = str(uuid.uuid4()) + "_" + original_filename
    upload_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
    
    # Save uploaded file
    file.save(upload_path)
    
    # Generate result filename
    result_filename = "processed_" + unique_filename
    result_path = os.path.join(app.config["RESULT_FOLDER"], result_filename)
    
    # Process image based on operation
    if operation == "encrypt":
        success = encrypt_image(upload_path, result_path, key)
        operation_name = "Encrypted"
    else:
        success = decrypt_image(upload_path, result_path, key)
        operation_name = "Decrypted"
    
    if not success:
        flash("Error processing image. Please try again.", "error")
        return redirect(url_for("home"))
    
    # Render result page
    return render_template(
        "index.html",
        original="/" + upload_path.replace("\\", "/"),
        result="/" + result_path.replace("\\", "/"),
        download=result_path.replace("\\", "/"),
        operation=operation_name,
        key=key
    )


@app.route("/download")
def download():
    """
    Download processed image.
    """
    file_path = request.args.get("file")
    
    if not file_path:
        flash("No file specified for download.", "error")
        return redirect(url_for("home"))
    
    # Ensure the file is within the results folder
    if not file_path.startswith("static/results/"):
        flash("Invalid file path.", "error")
        return redirect(url_for("home"))
    
    full_path = os.path.join(os.getcwd(), file_path.replace("/", os.sep))
    
    if not os.path.exists(full_path):
        flash("File not found.", "error")
        return redirect(url_for("home"))
    
    return send_file(full_path, as_attachment=True)


@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle file too large error.
    """
    flash("File is too large. Maximum size is 10 MB.", "error")
    return redirect(url_for("home"))


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle internal server error.
    """
    flash("An internal server error occurred. Please try again.", "error")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
   