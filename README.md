# Library Management API

## Description

The Library Management API is a Django-based application designed to manage a collection of books within a library. It
provides a comprehensive set of CRUD operations, allowing users to add, edit, delete, and view books. The API also
includes filtering and pagination features to help users efficiently manage and explore the library's inventory.

## Key Features

- **Book Management**: Enables users to perform CRUD operations on books, including adding, updating, deleting, and
  retrieving books.
- **Filtering and Pagination**: Allows users to filter books by author, published date, and language, with built-in
  pagination for efficient data handling.
- **Swagger Integration**: Provides an interactive API documentation through Swagger UI for easy exploration and testing
  of endpoints.

## Technology Stack

- **Django & Django REST Framework**: For building a secure and scalable backend.
- **PostgreSQL**: As the primary database solution for storing book records.
- **Docker & Docker Compose**: For containerization and streamlined deployment.
- **pytest**: For automated testing with coverage reporting.

## Installation Guide

### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine. You can download them from:

- Docker: [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/)

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hahan18/library_project.git  
   cd library_project
   ```

2. **Start the application using Docker Compose:**
    ```bash
    docker compose up --build
    ```
   The application with Swagger UI will be accessible at `http://localhost:8000/swagger/`.

### API Endpoints

**Book Management**

- `GET /api/books/`: Retrieve all books with optional filtering by author, published date, and language.
- `POST /api/books/`: Create a new book entry.
- `GET /api/books/{id}/`: Retrieve detailed information about a specific book by its ID.
- `PUT /api/books/{id}/`: Update information about a specific book by its ID.
- `PATCH /api/books/{id}/`: Patch information about a specific book by its ID.
- `DELETE /api/books/{id}/`: Delete a specific book by its ID.

## Running Tests

Execute automated tests with coverage by running:

```bash
docker compose run --rm test
```

Coverage reports will be generated and can be reviewed to ensure full test coverage.

## Authors

- **Oleksandr Khakhanovskyi** - "Library Management API"

