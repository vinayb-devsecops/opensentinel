# OpenSentinel Architecture

NVD CVE Feed
      |
      v
Collector Engine
      |
      v
SQLite Database
      |
      +------------------+
      |                  |
      v                  v
REST API           Analytics Engine
      |                  |
      +--------+---------+
               |
               v
Flask Dashboard
               |
               v
Authentication Layer

Features:
- CVE Collection
- Risk Classification
- SQLite Persistence
- REST APIs
- CSV Export
- Trend Analytics
- Authentication
