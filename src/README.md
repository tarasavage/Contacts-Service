# Contact Service

The Contact Service is a web application built using modern Python frameworks and patterns, designed to manage and interact with contact-related data. It utilizes the power of FastAPI, SQLAlchemy, Alembic, Pydantic, Redis, Celery, and `fastapi_users` for various aspects of the application.

## Features

- Unit of Work and Repository patterns for structured data access.
- API endpoints for managing contacts using FastAPI.
- Data persistence using SQLAlchemy ORM.
- Database migrations using Alembic.
- Data validation and serialization using Pydantic models.
- Background task scheduling with Celery.
- Caching support with Redis.
- User authentication and authorization using `fastapi_users` with cookies and JWT strategy.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python 3.7+.
- [SQLAlchemy](https://www.sqlalchemy.org/): A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- [Alembic](https://alembic.sqlalchemy.org/): A database migration tool for SQLAlchemy.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and settings management using Python type annotations.
- [Redis](https://redis.io/): An in-memory data structure store, used for caching.
- [Celery](http://www.celeryproject.org/): A distributed task queue system for background task processing.
- [FastAPI-users](https://frankie567.github.io/fastapi-users/): A high-level library for FastAPI to handle user authentication and authorization.

