# Library Management System API

- The APIs are implemented using FastAPI.
- Database: MongoDB Atlas

- `POST /students`: Create student
- `GET /stdudents`: List of students. Filter by country(str) or age(int) from query parameter
- `GET /students/{id}`: Fetch student info
- `PATCH /students/{id}`: Update Student
- `DELETE /students/{id}`: Delete student

* **

Folder Structure

```
.
|__config
    |__config.py
|__models
    |__students.py
|__routes
    |__route.py
|__schema
    |__schemas.py
|__main.py
|__requirements.txt
```