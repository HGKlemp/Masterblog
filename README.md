# Masterblog API

Masterblog is a simple RESTful blog API built with Flask.

The application provides CRUD functionality for blog posts and includes:

* GET all posts
* POST new posts
* PUT existing posts
* DELETE posts
* Search posts
* Sort posts
* CORS support
* Swagger UI for API testing

## Project Structure

```text
Masterblog/
│
├── backend/
│   └── backend_app.py
│
├── frontend/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/HGKlemp/Masterblog.git
```

Change into the project directory:

```bash
cd Masterblog
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Start the Application

Run:

```bash
python backend/backend_app.py
```

The API will be available at:

```text
http://localhost:5002
```

Swagger UI:

```text
http://localhost:5002/api/docs
```

## API Endpoints

### Get all posts

```text
GET /api/posts
```

Posts can optionally be sorted by `title` or `content`.

Example:

```text
GET /api/posts?sort=title&direction=asc
```

Supported directions:

```text
asc
desc
```

### Create a post

```text
POST /api/posts
```

Example request body:

```json
{
  "title": "My new post",
  "content": "This is my new blog post."
}
```

Both `title` and `content` are required.

### Search posts

```text
GET /api/posts/search
```

Examples:

```text
GET /api/posts/search?title=first
```

```text
GET /api/posts/search?content=blog
```

```text
GET /api/posts/search?title=first&content=post
```

### Update a post

```text
PUT /api/posts/<post_id>
```

Example:

```text
PUT /api/posts/1
```

Request body:

```json
{
  "title": "Updated title",
  "content": "Updated content"
}
```

### Delete a post

```text
DELETE /api/posts/<post_id>
```

Example:

```text
DELETE /api/posts/1
```

## Validation

The API validates incoming JSON data.

Invalid or missing values such as:

```json
{
  "title": null
}
```

return a `400 Bad Request` response instead of causing a server error.

## Technologies

* Python
* Flask
* Flask-CORS
* Flask-Swagger-UI
* REST API
* Swagger / OpenAPI

## Author

Hans-Günter Klemp
