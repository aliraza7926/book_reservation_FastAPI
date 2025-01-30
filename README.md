
# Book Reservation FastAPI

This is a Test project that use

[FastAPI](https://fastapi.tiangolo.com/),
[SQLAlchemy](https://www.sqlalchemy.org/),
[Alembic](https://alembic.sqlalchemy.org/en/latest/),
[PostgreSQL](https://www.postgresql.org/)
for a book reservation service

## Installation

In this project, I use [uv](https://docs.astral.sh/uv/) as a package manager.

To install the requirements you can use this command
```bash
  uv sync
```
or you could use pip for installing requirements from 

```bash
  requirements.txt
```

To run this project you must first create a Postgres database

and put the connection info in the 

```bash
  .env
```
there is a .env.example that you can use

after that, you must go to the database directory and use alembic to initialize your database
you can use this command

```bash
  cd database
  uv run alembic upgrade head
```

after this, you could simply go to the root of the project and start the FastAPI server

```bash
  cd ..
  uv run fastapi dev main.py 
```

## What works and What doesn't

the only thing that works in this project is creating a customer :(


## ToDo
- [ ]  complete the project
- [ ]  dockerize the project


Create a make file for this thing

- [ ]  creating admin
- [ ]  build and run the docker
- [ ]  populating the database with mock data
