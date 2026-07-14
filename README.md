# 🔐 PixelCrypt - Image Encryption & Decryption Tool

PixelCrypt is a web application that encrypts and decrypts images using pixel manipulation with the XOR algorithm.

This project was developed as part of the **SkillCraft Technology Software Engineering Internship - Task 2**.

## Features

* Upload Images (PNG, JPG, JPEG)
* Encrypt Images
* Decrypt Images
* Secret Key Encryption
* Random Key Generator
* Image Preview
* Download Processed Image
* Input Validation
* Error Handling
* Responsive Design

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Libraries

* Pillow (PIL)
* Werkzeug

## Folder Structure

```text
PixelCrypt/
│── app.py
│── requirements.txt
│── README.md
│
├── templates/
│   │── index.html
│   │── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── uploads/
│   └── results/
│
└── utils/
    └── encryption.py
```

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the Flask application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Project Objective

To understand and implement image encryption and decryption using pixel manipulation techniques while gaining practical experience in image processing, Python Flask, and full-stack web development.

## Future Improvements

* Multiple Encryption Algorithms
* Password-Protected Encryption
* Drag-and-Drop Image Upload
* Batch Image Encryption
* Cloud Storage Integration
* User Authentication
* Encryption History
* Dark Mode
* Improved UI Animations

## Author

**Manikanth**
