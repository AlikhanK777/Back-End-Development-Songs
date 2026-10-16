# Back-End-Development-Songs

Flask + MongoDB microservice for managing songs.

## Endpoints
- GET /health
- GET /count
- GET /song
- GET /song/<id>
- POST /song
- PUT /song/<id>
- DELETE /song/<id>

## Run locally
pip install -r requirements.txt
set FLASK_APP=backend
python -m flask run -p 5000
