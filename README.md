# Store API

## Description

The main goal of this project is to create an API to make CRUD operations on a store and its items.

## Tools Used

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask Smorest](https://flask-smorest.readthedocs.io/en/latest/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- [Docker](https://docs.docker.com/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)

## How To Run it

First create a virtual environment:

```shell
python -m venv .venv
```

After creating it you'll need to activate it

For windows:

```shell
.venv\Scripts\activate.bat
```

For linux:

```shell
source .venv/bin/activate
```

After that, install the required packages:

```shell
pip install -r requirements.txt
```

Then run the server:


```shell
make run
```

In the browser type:

```shell
http://127.0.0.1:5000/swagger-ui
```
After this process, the requests can be made in the swagger interface.

## What I've Learned

For this project i had to learn even more about flask by using flask smorest to create a REST API, validations with marshmellows, swagger ui and docker cli, i have also learned to create a makefile to run commands easier.

- More about REST APIs
- How to use flask smorest to create REST APIs
- How to make validations using the marshmallow lib
- How to use swagger ui
- How to create a make file
- More about docker (docker cli)