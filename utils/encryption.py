"""
Image Encryption Module
Implements XOR-based pixel manipulation for image encryption and decryption.
"""

from PIL import Image
import os


def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image using XOR operation on each pixel.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the encrypted image
        key (int): Encryption key (0-255)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Get pixel data
        pixels = img.load()
        width, height = img.size
        
        # Apply XOR operation to each pixel
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                
                # XOR each color channel with the key
                new_r = r ^ key
                new_g = g ^ key
                new_b = b ^ key
                
                pixels[x, y] = (new_r, new_g, new_b)
        
        # Save the encrypted image
        img.save(output_path)
        return True
    
    except Exception as e:
        print(f"Error encrypting image: {e}")
        return False


def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image using XOR operation on each pixel.
    Since XOR is reversible, this is the same as encryption.
    
    Args:
        input_path (str): Path to the encrypted image
        output_path (str): Path to save the decrypted image
        key (int): Decryption key (0-255)
    
    Returns:
        bool: True if successful, False otherwise
    """
    # XOR is reversible, so decryption is the same as encryption
    return encrypt_image(input_path, output_path, key)


def validate_key(key):
    """
    Validate that the key is within the valid range (0-255).
    
    Args:
        key (int): The key to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        key_int = int(key)
        return 0 <= key_int <= 255
    except (ValueError, TypeError):
        return False


def validate_image_format(filename):
    """
    Validate that the file has an allowed image format.
    
    Args:
        filename (str): The filename to validate
    
    Returns:
        bool: True if valid format, False otherwise
    """
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    return ext in allowed_extensions
