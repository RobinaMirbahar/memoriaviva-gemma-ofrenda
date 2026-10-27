FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY memoriaviva/ ./memoriaviva/
COPY scripts/ ./scripts/

EXPOSE 8080
CMD ["uvicorn", "memoriaviva.dashboard:app", "--host", "0.0.0.0", "--port", "8080"]
