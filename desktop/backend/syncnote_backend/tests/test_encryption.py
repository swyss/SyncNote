# tests/test_encryption.py
from src.encryption.security import hash_password, verify_password

def test_password_hashing():
    password = "SecurePassword123"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("WrongPassword", hashed) is False
