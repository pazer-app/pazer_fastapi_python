# Pazer FastAPI - Python

### Module
```bash
pip install python-dotenv
pip install uvicorn
pip install fastapi
pip install pazer_core_python
```

### command
#### Dev
```bash
uvicorn Core:core.app --reload --env-file Env/.env.development --port 8000 --host 0.0.0.0
```

#### Prod
```bash
uvicorn Core:core.app --reload --env-file Env/.env.production --port 8001 --host 0.0.0.0
```
