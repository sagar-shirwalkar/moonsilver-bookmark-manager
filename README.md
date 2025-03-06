# Moonsilver Bookmark Manager

Work in Progress. A modern and elegant bookmark manager that allows users to save, organize, and manage their bookmarks with ease. Built with FastAPI and MySQL.

## Features

- Clean and modern user interface
- User registration and authentication
- Create, read, and delete bookmarks
- Organize bookmarks into categories
- JWT-based authentication
- MySQL database with SQLAlchemy ORM
- Dockerized application with MySQL
- API versioning with /api/v1 prefix

## Running with Docker

The easiest way to run the application is using Docker Compose:

```bash
docker-compose up --build
```

This will:
1. Build the FastAPI application container
2. Pull and start the MySQL container
3. Set up the database and required volumes
4. Start the application on http://localhost:8000

The application will be available at:
- API Root: http://localhost:8000/
- API v1 Base URL: http://localhost:8000/api/v1
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc

## API Endpoints

All endpoints are prefixed with `/api/v1`

### Authentication
- `POST /api/v1/users` - Create a new user
- `POST /api/v1/token` - Login and get access token

### Categories
- `POST /api/v1/categories` - Create a new category
- `GET /api/v1/categories` - List all categories
- `GET /api/v1/categories/{category_id}` - Get a specific category with its bookmarks
- `PUT /api/v1/categories/{category_id}` - Update a category
- `DELETE /api/v1/categories/{category_id}` - Delete a category

### Bookmarks
- `POST /api/v1/bookmarks` - Create a new bookmark
- `GET /api/v1/bookmarks` - List all bookmarks
- `GET /api/v1/bookmarks/{bookmark_id}` - Get a specific bookmark
- `GET /api/v1/bookmarks/by-category/{category_id}` - List bookmarks in a category
- `DELETE /api/v1/bookmarks/{bookmark_id}` - Delete a bookmark

## Manual Setup (without Docker)

If you prefer to run without Docker:

1. Create a MySQL database named `bookmarks`

```sql
CREATE DATABASE bookmarks;
```

2. Create a `.env` file in the project root with the following variables:

```env
MYSQL_URL=mysql://root:root@localhost/bookmarks
SECRET_KEY=your-secret-key-here
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
uvicorn main:app --reload
