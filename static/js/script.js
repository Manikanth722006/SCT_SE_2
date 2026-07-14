/**
 * CipherX - Image Encryption & Decryption
 * Client-side JavaScript functionality
 */

// ==================== DOM Elements ====================
const uploadArea = document.getElementById('uploadArea');
const imageInput = document.getElementById('imageInput');
const previewContainer = document.getElementById('previewContainer');
const imagePreview = document.getElementById('imagePreview');
const removeImageBtn = document.getElementById('removeImage');
const keyInput = document.getElementById('keyInput');
const generateKeyBtn = document.getElementById('generateKey');
const uploadForm = document.getElementById('uploadForm');
const loadingOverlay = document.getElementById('loadingOverlay');
const toastContainer = document.getElementById('toastContainer');
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const contactForm = document.getElementById('contactForm');

// ==================== Toast Notifications ====================
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    let icon = 'info-circle';
    if (type === 'success') icon = 'check-circle';
    if (type === 'error') icon = 'exclamation-circle';
    
    toast.innerHTML = `
        <i class="bi bi-${icon}"></i>
        <span>${message}</span>
    `;
    
    toastContainer.appendChild(toast);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        toast.style.animation = 'toastOut 0.3s ease forwards';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// ==================== Mobile Navigation ====================
if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// ==================== File Upload ====================
if (uploadArea && imageInput) {
    // Click to upload
    uploadArea.addEventListener('click', () => {
        imageInput.click();
    });

    // Drag and drop functionality
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    // File input change
    imageInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });
}

// ==================== Handle File ====================
function handleFile(file) {
    // Validate file type
    const validTypes = ['image/png', 'image/jpeg', 'image/jpg'];
    if (!validTypes.includes(file.type)) {
        showToast('Invalid file type. Please upload PNG, JPG, or JPEG.', 'error');
        return;
    }

    // Validate file size (10MB)
    const maxSize = 10 * 1024 * 1024;
    if (file.size > maxSize) {
        showToast('File size exceeds 10MB limit.', 'error');
        return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        uploadArea.style.display = 'none';
        previewContainer.style.display = 'block';
        showToast('Image uploaded successfully!', 'success');
    };
    reader.readAsDataURL(file);
}

// ==================== Remove Image ====================
if (removeImageBtn) {
    removeImageBtn.addEventListener('click', () => {
        imageInput.value = '';
        imagePreview.src = '';
        uploadArea.style.display = 'block';
        previewContainer.style.display = 'none';
        showToast('Image removed.', 'info');
    });
}

// ==================== Generate Random Key ====================
if (generateKeyBtn && keyInput) {
    generateKeyBtn.addEventListener('click', () => {
        const randomKey = Math.floor(Math.random() * 256);
        keyInput.value = randomKey;
        showToast(`Random key generated: ${randomKey}`, 'success');
    });
}

// ==================== Form Submission ====================
if (uploadForm) {
    uploadForm.addEventListener('submit', (e) => {
        // Validate file is selected
        if (!imageInput.files || imageInput.files.length === 0) {
            e.preventDefault();
            showToast('Please select an image to process.', 'error');
            return;
        }

        // Validate key
        const key = parseInt(keyInput.value);
        if (isNaN(key) || key < 0 || key > 255) {
            e.preventDefault();
            showToast('Key must be between 0 and 255.', 'error');
            return;
        }

        // Show loading overlay
        loadingOverlay.classList.add('active');
        
        // Disable buttons
        const buttons = uploadForm.querySelectorAll('button[type="submit"]');
        buttons.forEach(btn => btn.disabled = true);
    });
}

// ==================== Contact Form Validation ====================
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');
        
        let isValid = true;
        
        // Reset error messages
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
        
        // Validate name
        if (name.value.trim().length < 2) {
            document.getElementById('nameError').textContent = 'Name must be at least 2 characters.';
            isValid = false;
        }
        
        // Validate email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value.trim())) {
            document.getElementById('emailError').textContent = 'Please enter a valid email address.';
            isValid = false;
        }
        
        // Validate message
        if (message.value.trim().length < 10) {
            document.getElementById('messageError').textContent = 'Message must be at least 10 characters.';
            isValid = false;
        }
        
        if (isValid) {
            // Simulate form submission
            showToast('Message sent successfully! We will get back to you soon.', 'success');
            contactForm.reset();
        } else {
            showToast('Please fix the errors above.', 'error');
        }
    });
}

// ==================== Smooth Scroll ====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ==================== Initialize ====================
document.addEventListener('DOMContentLoaded', () => {
    // Auto-scroll to results if they exist
    const resultsSection = document.querySelector('.results-section');
    if (resultsSection) {
        setTimeout(() => {
            resultsSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }, 500);
    }
});
