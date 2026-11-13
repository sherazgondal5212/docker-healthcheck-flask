# Docker Healthcheck Flask

Containerized Flask application with Docker HEALTHCHECK, Gunicorn and a non-root user. Tested in AWS CloudShell, including a failed-check test.

Part of the Gondal Digital Agency Cloud & DevOps portfolio.

## Projects

- **01-docker-flask:** Project 1.1, Dockerized Flask app
- **02-docker-healthcheck:** Project 1.2, Flask container with HEALTHCHECK

## What this demonstrates

- Dockerfile for a Flask app
- Gunicorn as the production server
- Non-root container user
- HEALTHCHECK with a failed-check test

## How to run

```bash
cd 02-docker-healthcheck
docker build -t flask-healthcheck .
docker run -d -p 5000:5000 --name flask-hc flask-healthcheck
docker ps
```

## Author

Muhammad Sheraz Gondal, Gondal Digital Agency
