# SyncNote Backend

The SyncNote backend is responsible for managing tasks, reminders, password storage, synchronization, and real-time notifications. It is built using Python with Flask and SocketIO and leverages Redis for data storage. The backend is designed to be modular, scalable, and secure.

---

## **Core Features**

- **Task and Reminder Management:**
  - Create, update, delete, and list tasks and reminders.
  - Set priorities and categories for tasks.
  - Manage recurring tasks and timed reminders.

- **Secure Password Storage:**
  - Store passwords with AES-256 encryption.
  - Auto-generate secure passwords.
  - Encrypted local storage in Redis with JSON backup.

- **Synchronization:**
  - Real-time sync between desktop and mobile apps.
  - Conflict resolution and sync protocol.
  - Asynchronous processing for improved performance.

- **Monitoring and Logging:**
  - Real-time status updates and logs.
  - Telemetry for API performance monitoring.
  - Log rotation and centralized logging.

- **Security:**
  - OAuth2 authentication and JWT tokens.
  - Role-based access control.
  - Two-factor authentication (2FA) support.

---

## **Technologies Used**

- **Python:** Flask, SocketIO
- **Data Storage:** Redis with persistent JSON backup
- **Encryption:** AES-256 for secure password management
- **Logging:** Custom logger with color-coded console output
- **Containerization:** Docker for backend and Redis

---

## **Backend Folder Structure**

```
desktop/backend/
├── src/                      # Source code
│   ├── models/               # Data models (Task, Reminder)
│   │    ├── __init__.py
│   │    ├── task.py
│   │    └── reminder.py
│   ├── crud/                 # CRUD operations for tasks and reminders
│   │    ├── __init__.py
│   │    ├── task_crud.py
│   │    └── reminder_crud.py
│   ├── sync/                 # Sync endpoints and conflict resolution
│   ├── utils/                # Utility functions (logger, redis client, console)
│   ├── config/               # Configuration files (e.g., Redis)
│   ├── database/             # Database initialization and management
│   ├── encryption/           # Password encryption and security functions
│   ├── message/              # Notification and message handling
│   └── main.py               # Main entry point
├── tests/                    # Unit and integration tests
├── logs/                     # Log files
├── requirements.txt          # Python dependencies
└── README.md                 # Backend overview
```

---

## **Setup Instructions**

### **1. Environment Setup:**
1. Clone the repository:
   ```bash
   git clone https://github.com/username/syncnote.git
   ```
2. Navigate to the backend folder:
   ```bash
   cd syncnote/desktop/backend
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **2. Start Redis:**
- Start Redis using Docker:
   ```bash
   docker run -d -p 6379:6379 --name redis-server redis
   ```
- Check the Redis connection:
   ```bash
   redis-cli ping
   ```
   Expected output:
   ```
   PONG
   ```

### **3. Start the Backend Server:**
```bash
python src/main.py
```
- The backend server will start on **http://0.0.0.0:5000**.

---

## **API Endpoints**

### **Task Management**
- **Create Task:**
  - `POST /tasks`
- **List Tasks:**
  - `GET /tasks`
- **Update Task:**
  - `PUT /tasks/{index}`
- **Delete Task:**
  - `DELETE /tasks/{index}`

### **Reminder Management**
- **Create Reminder:**
  - `POST /reminders`
- **List Reminders:**
  - `GET /reminders`
- **Delete Reminder:**
  - `DELETE /reminders/{index}`

### **System Status**
- **Health Check:**
  - `GET /status`

---

## **Running Tests**

Run the unit and integration tests:
```bash
pytest tests/
```

---

## **Configuration**

- Configuration files are located in the `config/` folder.
- Example configuration (`config/config.json`):
  ```json
  {
    "PORT": 5000,
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "SECRET_KEY": "your_secret_key"
  }
  ```
- Modify environment variables as needed.

---

## **Logging**

- Logs are stored in the `logs/` folder.
- The logging format includes timestamps, log levels, and messages.
- The logging configuration supports color-coded console output:
  - **INFO (Green)**
  - **WARNING (Yellow)**
  - **ERROR (Red)**
  - **DEBUG (White)**

---

## **Troubleshooting**

- **Redis Connection Failed:**
  - Make sure Redis is running locally or via Docker.
  - Check the configuration file for correct Redis host and port.

- **Application Not Starting:**
  - Check if the port is already in use.
  - Make sure the required Python packages are installed.

- **Permission Issues:**
  - Run the commands as an administrator if needed.

---

## **Contribution**

Feel free to open issues or submit pull requests. Follow the [contributing guidelines](../../docs/contributing.md) for more details.

---

## **License**

This project is licensed under the MIT License. See `LICENSE.md` for more information.
