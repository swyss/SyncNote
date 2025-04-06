# SyncNote: Task, Reminder, and Password Manager

SyncNote is a cross-platform application that allows users to manage tasks, reminders, and securely store passwords. It supports data synchronization between the desktop (Electron) and mobile (Android) applications. The application prioritizes data security, seamless synchronization, and efficient task management.

---

## **Key Features:**
- **Task Management:**
  - Create, update, delete, and list tasks.
  - Assign categories and priorities to tasks.
  - Set recurring tasks and reminders.
  - Calendar view for visualizing tasks and events.

- **Reminder System:**
  - Create reminders for tasks and recurring events.
  - Real-time notifications on due tasks.
  - Automated reminder management with priority handling.

- **Password Storage:**
  - Secure password storage with AES-256 encryption.
  - Auto-generation of secure passwords.
  - Encrypted local storage in Redis with JSON backup.

- **Data Synchronization:**
  - Real-time synchronization between desktop and mobile devices.
  - Conflict resolution mechanisms.
  - Bidirectional sync with error handling.

- **Security:**
  - Encrypted data storage using AES-256.
  - OAuth2 authentication and JWT tokens.
  - Role-based access control for enhanced security.
  - Two-factor authentication (2FA) for secure access.

- **Monitoring and Logging:**
  - Real-time status updates and logs.
  - Telemetry for API performance monitoring.
  - Log rotation and centralized logging.

---

## **Documentation:**
The documentation is organized as follows:
- [Functional Requirements](./docs/requirements.md)
- [Architecture Overview](./docs/architecture.md)
- [Contribution Guidelines](./docs/contributing.md)
- [License Information](./docs/license.md)

---

## **Tech Stack:**
- **Frontend (Desktop):** Electron with Vue 3
- **Backend:** Python (Flask/FastAPI), Redis
- **Mobile:** Android (React Native)
- **Data Storage:** Redis (persistent JSON backups)
- **Security:** AES-256 encryption for password management
- **Sync Protocol:** Real-time synchronization via WebSockets and REST APIs
- **Logging:** Enhanced structured logging with file rotation
- **Containerization:** Docker for the backend and database
- **Monitoring:** Integrated telemetry and logging

---

## **Getting Started:**
1. Clone the repository:
   ```bash
   git clone https://github.com/username/syncnote.git
   ```
2. Navigate to the project folder:
   ```bash
   cd syncnote
   ```
3. Set up the backend:
   ```bash
   cd desktop/backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   python src/main.py
   ```
4. Run the frontend:
   ```bash
   cd desktop/frontend
   npm install
   npm start
   ```
5. Start the mobile app:
   ```bash
   cd mobile
   npm install
   react-native run-android
   ```

---

## **SyncNote Folder Structure:**

```
SyncNote/
├── desktop/                   # Desktop application components
│   ├── backend/               # Backend code (Python)
│   │   ├── src/               # Source code  
│   │   │   ├── config/        # Configuration management  
│   │   │   ├── database/      # Database initialization and handling  
│   │   │   ├── encryption/    # Password encryption and security functions  
│   │   │   ├── sync/          # Synchronization endpoints for mobile and desktop  
│   │   │   ├── utils/         # Utility functions (e.g., ASCII art for console, logger)  
│   │   │   └── main.py        # Main entry point  
│   │   ├── tests/             # Unit and integration tests  
│   │   ├── requirements.txt   # Python dependencies  
│   └── config/                # Configuration files (e.g., Redis)  
│   
│   ├── frontend/              # Frontend code (Electron)  
│       ├── src/               # Source code for the Electron application  
│       ├── assets/            # Icons and static files  
│       ├── public/            # HTML and CSS files  
│       └── package.json       # Frontend dependencies  
├── mobile/                    # Android app code  
│   ├── src/                   # Mobile app source code  
│   └── assets/                # Mobile-specific resources  
├── docs/                      # Documentation files  
│   ├── requirements.md        # Functional and non-functional requirements  
│   ├── architecture.md        # Technical architecture and design  
│   ├── contributing.md        # Contribution guidelines  
│   └── license.md             # License information  
├── docker/                    # Docker configuration files  
│   ├── docker-compose.yml     # Docker setup for backend and Redis  
│   └── Dockerfile             # Backend container configuration  
├── README.md                  # Project overview  
```

---

## **Contributing:**
Contributions are welcome! Please check the [contribution guidelines](./docs/contributing.md) before submitting pull requests.

---

## **License:**
This project is licensed under the MIT License. See `LICENSE.md` for more details.
```
