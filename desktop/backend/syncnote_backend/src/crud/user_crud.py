# src/crud/user_crud.py

import json
import logging

logger = logging.getLogger("SyncNote")

def add_user(redis_client, user):
    """Add a new user."""
    try:
        redis_client.hset("users", user['username'], json.dumps(user))
        logger.info(f"User {user['username']} added successfully")
        return {"success": True, "message": "User added"}
    except Exception as e:
        logger.error(f"Failed to add user {user['username']}: {e}")
        return {"success": False, "message": str(e)}

def get_user(redis_client, username):
    """Retrieve user by username."""
    try:
        user_data = redis_client.hget("users", username)
        if user_data:
            logger.info(f"User {username} retrieved successfully")
            return json.loads(user_data)
        return None
    except Exception as e:
        logger.error(f"Failed to retrieve user {username}: {e}")
        return None

def delete_user(redis_client, username):
    """Delete a user."""
    try:
        redis_client.hdel("users", username)
        logger.info(f"User {username} deleted successfully")
        return {"success": True, "message": "User deleted"}
    except Exception as e:
        logger.error(f"Failed to delete user {username}: {e}")
        return {"success": False, "message": str(e)}
