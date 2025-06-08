FROM python:3.9-slim
WORKDIR /app
COPY app.py products.json ./
RUN pip install flask
CMD ["python", "app.py"]
