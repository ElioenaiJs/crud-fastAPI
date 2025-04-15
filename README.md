# TaskBack - Backend API (Python + MySQL Docker)

## 🚀 Guía Rápida de Uso

```bash

# 1. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\activate  # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar MySQL con Docker
docker-compose up -d

# 4. Ejecutar la API
source venv/bin/activate  
uvicorn app.main:app --reload

# 5. Acceder a:
# Docs: http://localhost:8000/docs
