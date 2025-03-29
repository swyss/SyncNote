# SyncNote Backend

## Overview
The backend of SyncNote is built using Python (Flask/FastAPI) and serves as the core service for task management, password encryption, and synchronization between desktop and mobile applications.

## Folder Structure
```
backend/  
├── src/                    # Source code  
├── config/                 # Configuration management  
├── database/               # Database initialization and handling  
├── encryption/             # Password encryption and security functions  
├── sync/                   # Synchronization endpoints for mobile and desktop  
├── utils/                  # Utility functions (e.g., ASCII art for console)  
└── main.py                 # Main entry point  
├── config/                 # Configuration files (e.g., Redis)  
├── tests/                  # Unit and integration tests  
└── requirements.txt        # Python dependencies
```

## Functional Requirements
- **Database Initialization:**
  - Establish connection to Redis.
  - Prepare data structures (Tasks, Reminders, Passwords).
  - Periodic JSON file backups.

- **Console Status Output:**
  - ASCII art at startup.
  - Service status display (Running, Stopped).
  - Management functions (Start, Stop, Restart).

- **Configuration Management:**
  - Load and save configuration files.
  - Environment variable handling.

- **Password Handling:**
  - AES-256 encryption for passwords.
  - bcrypt hashing for master password.
  - Password validation and error handling.

- **Synchronization Endpoints:**
  - **/sync/tasks**: Sync tasks between devices.
  - **/sync/reminders**: Sync reminders.
  - **/sync/passwords**: Sync password data.
  - **/status**: Display server status.

## Getting Started
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run the backend server:
```
python src/main.py
```

## Running Tests
To execute unit and integration tests:
```
pytest tests/
```

## Troubleshooting
- If the server does not start, check the Redis connection and ensure that configuration files are correctly loaded.
- Check the logs for detailed error messages.


