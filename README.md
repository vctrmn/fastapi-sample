# Sample Fast API

This is a basic FastAPI app that serves a single "Hello World" endpoint. It's intended to serve as a starting point for building a more complex FastAPI app.

## Getting started

### Develop locally
```
python3 -m venv venv
```

```
. venv/bin/activate
```

```
pip install -r requirements.txt
```

```
uvicorn app.main:app --reload
```

### Lint
```
pylint app
```

### Test
```
pytest
```

### Build Docker
```
docker build . -t demo-fastapi
```
```
docker run -d -p 5001:5000 --name demo-fastapi --rm demo-fastapi
```