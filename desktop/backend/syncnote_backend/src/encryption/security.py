# src/encryption/security.py

from cryptography.fernet import Fernet
import bcrypt
import logging

logger = logging.getLogger("SyncNote")

def generate_key():
    """Generate a secure encryption key."""
    try:
        key = Fernet.generate_key()
        logger.info("Encryption key generated successfully")
        return key
    except Exception as e:
        logger.error(f"Error generating encryption key: {e}")
        return None

def save_key_to_file(key, filename="encryption.key"):
    """Save the encryption key to a file."""
    try:
        with open(filename, "wb") as file:
            file.write(key)
        logger.info(f"Encryption key saved to {filename}")
        return True
    except Exception as e:
        logger.error(f"Error saving encryption key to file: {e}")
        return False

def load_key_from_file(filename="encryption.key"):
    """Load the encryption key from a file."""
    try:
        with open(filename, "rb") as file:
            key = file.read()
        logger.info(f"Encryption key loaded from {filename}")
        return key
    except Exception as e:
        logger.error(f"Error loading encryption key from file: {e}")
        return None

def hash_password(password):
    """Hash a password with bcrypt."""
    try:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        logger.info("Password hashed successfully")
        return hashed
    except Exception as e:
        logger.error(f"Error hashing password: {e}")
        return None

def verify_password(password, hashed):
    """Verify a password against the stored hash."""
    try:
        is_valid = bcrypt.checkpw(password.encode(), hashed)
        if is_valid:
            logger.info("Password verification successful")
        else:
            logger.warning("Password verification failed")
        return is_valid
    except Exception as e:
        logger.error(f"Error verifying password: {e}")
        return False
