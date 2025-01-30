
# Book Reservation FastAPI

This is a Test projct that use

[FastAPI](https://fastapi.tiangolo.com/),
[SQLAlchemy](https://www.sqlalchemy.org/),
[Alembic](https://alembic.sqlalchemy.org/en/latest/),
[PostgreSQL](https://www.postgresql.org/)
for a book reservation service

## Installation

In this project i use [uv](https://docs.astral.sh/uv/) as a package manager.

for installing the requirements you can use this command
```bash
  uv sync
```
or you could use pip for installing requirements from 

```bash
  requirements.txt
```

To run this project you must first create a postgres database

and put the connction info in the 

```bash
  .env
```
there is a .env.example that you can use

after that you must go to the database directory and use alemib to initialize your database
you can use this command

```bash
  cd database
  uv run alembic upgrade head
```

after this you could simply go to the root of the project and start the fast api server

```bash
  cd ..
  uv run fastapi dev main.py 
```

## What work and What doesn't

the only thing that work in this project is creating a user :(


## ToDo
- [ ]  complete the project
- [ ]  dockerize the projct


Create a make file for this thing

- [ ]  creating admin
- [ ]  build and run the docker
- [ ]  populating the database with mock data
