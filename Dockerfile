FROM python:3.11-slim
WORKDIR /app
COPY persistent_auditor.py functions.py inventory.json .
CMD ["python", "persistent_auditor.py"]