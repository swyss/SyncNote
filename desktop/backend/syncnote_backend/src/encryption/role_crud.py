# src/crud/role_crud.py

import json
import logging

logger = logging.getLogger("SyncNote")

def add_role(redis_client, role_name, permissions):
    """Add a new role with specific permissions."""
    try:
        role_data = {"name": role_name, "permissions": permissions}
        redis_client.hset("roles", role_name, json.dumps(role_data))
        logger.info(f"Role {role_name} added successfully")
        return {"success": True, "message": "Role added"}
    except Exception as e:
        logger.error(f"Failed to add role {role_name}: {e}")
        return {"success": False, "message": str(e)}

def get_role(redis_client, role_name):
    """Retrieve a role by name."""
    try:
        role_data = redis_client.hget("roles", role_name)
        if role_data:
            logger.info(f"Role {role_name} retrieved successfully")
            return json.loads(role_data)
        return None
    except Exception as e:
        logger.error(f"Failed to retrieve role {role_name}: {e}")
        return None

def delete_role(redis_client, role_name):
    """Delete a role."""
    try:
        redis_client.hdel("roles", role_name)
        logger.info(f"Role {role_name} deleted successfully")
        return {"success": True, "message": "Role deleted"}
    except Exception as e:
        logger.error(f"Failed to delete role {role_name}: {e}")
        return {"success": False, "message": str(e)}
