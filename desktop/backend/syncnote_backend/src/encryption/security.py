# src/encryption/security.py
from cryptography.fernet import Fernet
import bcrypt

def generate_key():
    key = Fernet.generate_key()
    print(f"[INFO] Generated Encryption Key: {key.decode()}")
    return key

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
