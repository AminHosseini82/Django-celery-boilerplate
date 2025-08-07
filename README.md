# Django & Celery Starter Project

This is a starter project demonstrating how to integrate **Celery** with **Django**. The main goal of this repository is to provide a simple and ready-to-use template for running background tasks in Django projects, using **Redis** as the message broker. The entire project is containerized using **Docker** and **Docker Compose** for easy development and deployment across different environments.

## ✨ Features

* **Django Project**: A standard Django project structure.
* **Celery Integration**: Fully configured to connect Django with Celery for asynchronous task processing.
* **Redis Broker**: Uses Redis as both the message broker and the result backend.
* **Dockerized Environment**: All services (Django, Celery, and Redis) run in Docker containers.
* **Easy Setup**: Get the entire project running with a single `docker-compose` command.
* **Example Tasks**: Includes sample tasks to test the Celery setup.

## 🛠️ Tech Stack

* **Backend**: Django
* **Task Queue**: Celery
* **Message Broker**: Redis
* **Containerization**: Docker, Docker Compose
* **Language**: Python 3.11

## 🚀 Getting Started

To run this project, you only need Docker and Docker Compose installed on your system. Then, follow the steps below.

1.  First, clone the repository:
    ```bash
    git clone https://github.com/AminHosseini82/my_celery_test.git
    cd my_celery_test
    ```

2.  Build and run the project using Docker Compose. This command will build the images and start the containers.
    ```bash
    docker-compose up --build
    ```
    After running the command, the following services will be available:
    * **Django service**: Running on port `8000` (`http://localhost:8000`).
    * **Celery service**: Fetches and executes tasks from the Redis queue.
    * **Redis service**: Acts as the broker on port `6379`.

## 📝 Usage

### Defining New Tasks
You can define your new tasks in the `tasks.py` file of any Django app. In this project, for example, sample tasks are located in `Project/notifications/tasks.py`.

A sample task is defined as follows:
```python
from celery import shared_task
import time

@shared_task
def my_new_task(arg1, arg2):
    # Code you want to run in the background
    print(f"Executing task with args: {arg1}, {arg2}")
    time.sleep(10)  # Simulate a long-running operation
    return "Task Completed!"