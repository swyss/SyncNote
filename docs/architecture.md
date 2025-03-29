# SyncNote Architecture

## Overview
SyncNote is designed as a cross-platform task and password management application with synchronization capabilities between desktop (Electron) and mobile (Android) versions.

## Architecture Components:
- **Frontend (Desktop - Electron):**
  - User Interface for task management, calendar view, and password vault.
- **Backend (Python - Flask/FastAPI):**
  - API for task, reminder, and password management.
  - WebSocket support for real-time synchronization.
- **Mobile (Android - React Native):**
  - Sync client and offline task management.
- **Database (Redis):**
  - In-memory storage for fast data access.
  - Persistent JSON backups for data recovery.
- **Synchronization:**
  - WebSockets for real-time updates.
  - REST API for bulk data sync.

## Data Flow:
1. User adds/updates a task on desktop or mobile.
2. Data is stored in Redis and backed up as JSON.
3. Real-time sync to other devices through WebSocket.
4. On mobile, data is accessible offline and syncs when back online.
