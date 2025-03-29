# SyncNote Requirements

## Functional Requirements
- **Task Management:**
  - CRUD operations (Create, Read, Update, Delete) for tasks.
  - Task categories and priorities.
  - Task status (open, in progress, completed).
- **Reminders:**
  - Notifications for due tasks.
  - Recurring reminders.
- **Calendar Integration:**
  - Display tasks and reminders within a calendar.
  - Integration with external calendars (Google Calendar).
- **Password Management:**
  - Create, read, update, and delete passwords.
  - AES-256 encryption for data security.
- **Synchronization:**
  - Data sync between desktop and mobile.
  - Configurable sync options.

## Non-functional Requirements
- **Security:**
  - Data encryption at rest and in transit.
  - Master password with hashing (bcrypt).
- **Performance:**
  - Low-latency synchronization.
- **Platform Compatibility:**
  - Windows for desktop, Android for mobile.
- **Usability:**
  - Intuitive UI, accessible both on desktop and mobile.

