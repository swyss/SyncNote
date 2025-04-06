# src/crud/password_crud.py

import json
import logging
from src.encryption.crypto import encrypt, decrypt

logger = logging.getLogger("SyncNote")

def add_password(redis_client, user, password):
    """Store an encrypted password."""
    try:
        encrypted_pw = encrypt(password)
        redis_client.hset("passwords", user, encrypted_pw)
        logger.info(f"Password for {user} stored successfully")
        return {"success": True, "message": "Password stored"}
    except Exception as e:
        logger.error(f"Failed to store password for {user}: {e}")
        return {"success": False, "message": str(e)}

def get_password(redis_client, user):
    """Retrieve and decrypt a password."""
    try:
        encrypted_pw = redis_client.hget("passwords", user)
        if encrypted_pw:
            decrypted_pw = decrypt(encrypted_pw)
            logger.info(f"Password for {user} retrieved successfully")
            return decrypted_pw
        return None
    except Exception as e:
        logger.error(f"Failed to retrieve password for {user}: {e}")
        return None
