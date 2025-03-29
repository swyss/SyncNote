# SyncNote: Task, Reminder, and Password Manager
SyncNote is a cross-platform application that allows users to manage tasks, reminders, and securely store passwords. It supports data synchronization between the desktop (Electron) and mobile (Android) applications.

## Key Features:
- Task management with categories and priorities.
- Reminders for tasks and recurring events.
- Calendar view for visualizing tasks and events.
- Encrypted password storage.
- Real-time synchronization between devices.

## Documentation:
The documentation is organized as follows:
- [Functional Requirements](./docs/requirements.md)
- [Architecture Overview](./docs/architecture.md)
- [Contribution Guidelines](./docs/contributing.md)
- [License Information](./docs/license.md)

## Tech Stack:
- Electron for the desktop frontend
- Python (Flask/FastAPI) for the backend
- Android (React Native) for mobile
- Redis for data storage with JSON backups
- AES-256 encryption for password security

## Getting Started:
1. Clone the repository:
```
git clone https://github.com/username/syncnote.git
```
2. Follow the instructions in the respective application folders (backend, frontend, mobile) to run the instances.

## License:
This project is licensed under the MIT License. See `LICENSE.md` for details.

## SyncNote Folder Structure

```
SyncNote/
├── desktop/                   # Desktop application components
│   ├── backend/               # Backend code (Python)
│   │   ├── src/               # Source code  
│   │   │   ├── config/        # Configuration management  
│   │   │   ├── database/      # Database initialization and handling  
│   │   │   ├── encryption/    # Password encryption and security functions  
│   │   │   ├── sync/          # Synchronization endpoints for mobile and desktop  
│   │   │   ├── utils/         # Utility functions (e.g., ASCII art for console)  
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


