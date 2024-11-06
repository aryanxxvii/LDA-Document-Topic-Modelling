# Use a Python 3.9 slim image for the backend
FROM python:3.9-slim AS backend

# Set working directory for the backend
WORKDIR /app/backend

# Copy the backend requirements file
COPY backend/requirements.txt ./

# # Install the Cython package
# RUN pip install --no-cache-dir cython
# RUN pip install --no-cache-dir numpy==2.0.0

# # Install the Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY backend/ ./

# Download the spaCy model
# RUN python -m spacy download en_core_web_md

# Expose the port for Flask (5000)
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Start the Flask app
CMD ["python", "app.py"]
