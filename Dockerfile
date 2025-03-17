# Use an official Python image as base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose necessary ports (if required)
EXPOSE 5000 

# Run the game (update this based on how the game is launched)
CMD ["python", "main.py"]
