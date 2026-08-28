# Masterblog

Masterblog is a small Flask-based blog application consisting of a separate frontend and backend.

The backend provides a REST API for managing blog posts, while the frontend provides the web interface.

## Features

- Display blog posts
- Create new posts
- Update existing posts
- Delete posts
- Search posts by title and content
- Sort posts by title or content
- REST API built with Flask
- CORS support
- Swagger API documentation

## Project Structure

```text
Masterblog/
│
├── backend/
│   └── backend_app.py
│
├── frontend/
│   ├── frontend_app.py
│   ├── static/
│   └── templates/
│
├── main.py
├── requirements.txt
└── README.md