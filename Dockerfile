FROM python:3.11-slim
WORKDIR /app
COPY inventory_manager.py functions.py inventory.json .
CMD ["python", "inventory_manager.py"]