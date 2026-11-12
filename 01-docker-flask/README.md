# Project 1.1: Containerized Flask App (Docker)

## Overview
A minimal Flask API containerized with Docker, served by Gunicorn and run as a non-root user.

## Tech Stack
Python 3.12, Flask 3.0.3, Gunicorn 22.0.0, Docker

## Endpoints
| Path | Response |
|---|---|
| `/` | JSON message and app version (from `APP_VERSION` env var) |
| `/health` | `{"status":"ok"}` (HTTP 200) |

## Build and Run
    docker build -t gda-flask:1.0 .
    docker run -d --name flask-test -p 5000:5000 -e APP_VERSION=1.0 gda-flask:1.0
    curl localhost:5000
    curl localhost:5000/health

## Security Practices
- Runs as non-root user (`appuser`, uid=1000), verified with `docker exec flask-test id`
- Production WSGI server (Gunicorn) instead of the Flask dev server
- Pinned dependency versions
- `.dockerignore` keeps unnecessary files out of the build context

## Test Results
- `/` returned the expected JSON; `/health` returned `{"status":"ok"}`
- Gunicorn started and booted a worker (verified in `docker logs`)
- Image size: 134MB (to be optimized in Project 1.3)

## Lessons Learned
The first `curl` right after `docker run` failed with "Connection reset by peer" because Gunicorn had not finished starting. Waiting a few seconds fixed it. This motivates adding a HEALTHCHECK.

## Cleanup
    docker rm -f flask-test
    docker rmi gda-flask:1.0
