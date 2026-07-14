# CipherX - Image Encryption & Decryption Website

A complete, production-quality web application for encrypting and decrypting images using pixel manipulation with the XOR encryption algorithm. Built with Flask, this project was developed as part of the SkillCraft Technology Internship.

## Features

- **Image Encryption**: Encrypt images using XOR-based pixel manipulation
- **Image Decryption**: Decrypt encrypted images using the same XOR algorithm
- **Secure Key System**: Use secret keys (0-255) for encryption/decryption
- **Random Key Generation**: Generate random encryption keys with one click
- **Drag & Drop Upload**: Modern drag-and-drop interface for image uploads
- **Image Preview**: Preview images before processing
- **Multiple Format Support**: Supports PNG, JPG, and JPEG formats
- **Download Processed Images**: Download encrypted/decrypted images
- **Modern UI**: Glassmorphism design with smooth animations
- **Responsive Design**: Fully responsive for all devices
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **File Size Limit**: 10MB maximum file size for uploads

## Tech Stack

### Frontend
- HTML5
- CSS3 (Glassmorphism Design)
- Vanilla JavaScript

### Backend
- Python Flask
- Pillow (PIL) for image processing
- Werkzeug for secure file handling

### External Libraries
- Bootstrap Icons (CDN)
- Google Fonts (Poppins)

## Project Structure

```
Image-Encryption-Website/
│
├── app.py                      # Flask application with all routes
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
│
├── utils/
│   └── encryption.py           # Encryption/decryption algorithms
│
├── templates/
│   ├── index.html              # Home page with upload form
│   ├── about.html              # About page with explanations
│   └── contact.html            # Contact page with form
│
├── static/
│   ├── css/
│   │   └── style.css           # Complete stylesheet with glassmorphism
│   │
│   ├── js/
│   │   └── script.js           # Client-side JavaScript functionality
│   │
│   ├── uploads/                # Uploaded images storage
│   └── results/                # Processed images storage
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project**

2. **Navigate to the project directory**
   ```bash
   cd cipherx2
   ```

3. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

5. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

### Encrypting an Image

1. **Upload an Image**
   - Click "Browse Files" or drag & drop an image
   - Supported formats: PNG, JPG, JPEG
   - Maximum file size: 10MB

2. **Enter Secret Key**
   - Enter an integer key between 0 and 255
   - Or click "Generate" for a random key

3. **Click Encrypt**
   - The image will be encrypted using XOR algorithm
   - View the original and encrypted images side by side

4. **Download**
   - Click "Download Encrypted Image" to save the result

### Decrypting an Image

1. **Upload the Encrypted Image**
   - Use the same process as encryption

2. **Enter the Same Key**
   - Use the exact key that was used for encryption
   - Without the correct key, the image cannot be properly decrypted

3. **Click Decrypt**
   - The image will be decrypted using the XOR algorithm
   - View the original and decrypted images side by side

4. **Download**
   - Click "Download Decrypted Image" to save the result

## How It Works

### XOR Encryption Algorithm

The application uses XOR (Exclusive OR) encryption, which is a simple yet effective encryption method. Here's how it works:

1. **Pixel Access**: Each pixel in the image has three color channels: Red (R), Green (G), and Blue (B), each with values 0-255.

2. **XOR Operation**: For each pixel, we apply the XOR operation with the secret key:
   ```
   New_R = R XOR key
   New_G = G XOR key
   New_B = B XOR key
   ```

3. **Reversibility**: XOR is reversible - applying XOR twice with the same key returns the original value:
   ```
   (R XOR key) XOR key = R
   ```

This property makes XOR encryption perfect for image encryption because the same operation works for both encryption and decryption.

### Security Features

- **Secure Filenames**: Uses UUID to generate unique filenames
- **File Validation**: Validates file types and sizes before processing
- **Key Validation**: Ensures keys are within valid range (0-255)
- **Path Security**: Prevents directory traversal attacks
- **Size Limit**: Restricts uploads to 10MB to prevent server overload

## Screenshots

### Home Page
- Beautiful landing page with hero section
- Upload card with drag-and-drop functionality
- Key input with random generation
- Encrypt/Decrypt buttons

### Results Page
- Side-by-side comparison of original and processed images
- Download button for processed image
- Operation confirmation with key used

### About Page
- Explanation of image encryption
- XOR encryption algorithm details
- Pixel manipulation diagrams
- Key features overview

### Contact Page
- Professional contact form
- Contact information
- Form validation

## API Endpoints

### Routes

- `GET /` - Home page
- `GET /about` - About page
- `GET /contact` - Contact page
- `POST /process` - Process image encryption/decryption
- `GET /download` - Download processed image

### Error Handling

- **413 Error**: File too large (>10MB)
- **500 Error**: Internal server error
- **Flash Messages**: User-friendly error messages

## Dependencies

```
Flask==3.0.0
Pillow==10.1.0
Werkzeug==3.0.1
```

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Future Improvements

- [ ] Add AES encryption option for stronger security
- [ ] Support for additional image formats (BMP, GIF, WebP)
- [ ] Batch processing for multiple images
- [ ] User authentication and saved encryption history
- [ ] Real-time preview during encryption
- [ ] Mobile app version
- [ ] Cloud storage integration
- [ ] Advanced encryption algorithms (RSA, AES)
- [ ] Image compression before encryption
- [ ] Watermarking feature

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is developed as part of the SkillCraft Technology Internship. All rights reserved.

## Contact

For questions or feedback, please use the contact form on the website or email support@cipherx.com.

## Acknowledgments

- SkillCraft Technology for the internship opportunity
- Flask community for excellent documentation
- Bootstrap Icons for the icon set
- Google Fonts for the Poppins font

---

**Note**: This is a demonstration project for educational purposes. For production use, consider implementing additional security measures such as HTTPS, user authentication, and more robust encryption algorithms.
