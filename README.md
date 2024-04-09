# Library Management System API

This project implements a RESTful API for a Library Management System using FastAPI with MongoDB Atlas as the database.

## API Endpoints

* [API REQUIREMENTS](https://app.swaggerhub.com/apis-docs/Cosmocloud/Backend-Intern-Hiring-Task/1.0.0)

- `POST /students`: Create a new student record.
- `GET /students`: Retrieve a list of students. Optional query parameters:
  - `country`: Filter students by country (string).
  - `age`: Filter students by age (integer).
- `GET /students/{id}`: Retrieve details of a specific student by ID.
- `PATCH /students/{id}`: Update details of a specific student by ID.
- `DELETE /students/{id}`: Delete a specific student by ID.


* **

## Folder Structure

```
.
|__config
|   |__config.py        # Configuration settings
|__models
|   |__students.py      # MongoDB models for students
|__routes
|   |__route.py         # FastAPI route definitions
|__schema
|   |__schemas.py       # Pydantic schemas for request/response data
|__.env                 # Environment variable configuration
|__.gitignore           # Gitignore file
|__docker-compose.yml   # Docker Compose configuration
|__Dockerfile           # Dockerfile for building the Docker image
|__main.py              # Main FastAPI application entry point
|__README.md            # Project README file
|__requirements.txt     # Python dependencies file
```

## Prerequisites

- Python 3.9 or higher
- Docker
- MongoDB Atlas account

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/library-management-api.git
   cd library-management-api
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the project root directory with the following content:
   ```plaintext
   MONGO_URI=mongodb+srv://yourusername:yourpassword@yourmongocluster.mongodb.net/yourdatabase?retryWrites=true&w=majority
   MONGO_DB_NAME=yourdatabase
   MONGO_COLLECTION_NAME=students
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Docker Deployment

To deploy the application using Docker, follow these steps:

1. **Build the Docker Image**:
   ```bash
   docker build -t library-management-api .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d --name library-api-container -p 8000:8000 library-management-api
   ```
