FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY app.py .
COPY products.json .

# Install dependencies
RUN pip install flask psycopg2-binary

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

