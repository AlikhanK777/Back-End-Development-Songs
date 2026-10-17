# Back-End-Development-Songs

Flask + MongoDB microservice for managing songs. Part of the Back-End Development Capstone Project.

## Endpoints

- `GET /health`
- `GET /count`
- `GET /song`
- `GET /song/{id}`
- `POST /song`
- `PUT /song/{id}`
- `DELETE /song/{id}`

## Run locally

    pip install -r requirements.txt
    set FLASK_APP=backend
    python -m flask run -p 5000

## Deploy on OpenShift

    oc new-app --name=songs python~https://github.com/AlikhanK777/Back-End-Development-Songs --env MONGODB_SERVICE=mongo
    oc expose service/songs
