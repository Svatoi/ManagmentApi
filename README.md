# Management API

A program for automating inventory and order management in a warehouse, including access control (role model: Administrators / Users), secure password hashing, and authentication using JWT tokens.

## Tech Stack

* **Programming Language:** Python 3.11
* **Framework:** FastAPI (REST API)
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (v2.0)
* **Database Migration:** Alembic
* **Containerization:** Docker and Docker Compose
* **Testing:** Pytest (unit tests)
* **Security:** JWT tokens (PyJWT) + password hashing (Bcrypt)

---

## Running in Docker

For a successful project launch You need to install and run Docker Desktop.

### Step 1. Clone the repository

git clone https://github.com/your_login/managment_api.git
cd management_api

### Step 2. Set up environment variables

Create a .env file in the project's root directory and copy the structure from the .env.example file into it. Make sure you fill in the secret keys and database connection parameters in the created .env file.

cp.env.example.env

### Step 3. Building and Running Containers

Make sure Docker Desktop is running, then run the command in the console (the --build flag is required to build the latest Python image):

docker compose up --build

Docker will automatically download the PostgreSQL image, build the container with FastAPI, and run them in the same virtual network.

### Step 4. Applying Database Migrations

To automatically create all the necessary tables in a clean database, run the migration command inside the running container:

docker compose exec web alembic upgrade head

---

## API Documentation

After a successful launch, interactive documentation will be available at the following addresses:
* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

### Main endpoint groups:
1. /auth - User registration and authorization, password hashing using bcrypt
2. /items - Product catalog management (browsing, searching, filtering)
3. /orders - User order creation with automatic total cost calculation (server-side)

---

## Testing

The project is covered by automated tests. The configuration is in the pytest.ini file. To run the tests, run the command:

pytest