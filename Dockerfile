# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set environment variables for Streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Expose port 8501 for Streamlit
EXPOSE 8080

# Set the working directory inside the container
WORKDIR /app

# Copy the Python requirements file into the container
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Run your Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
