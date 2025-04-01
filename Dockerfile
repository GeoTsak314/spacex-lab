# Official Python image
FROM python:3.12-slim

# Working directory set
WORKDIR /app

# Files copying (duh!...)
COPY . .

# Dependencies installation
RUN pip install --no-cache-dir -r requirements.txt

# Flask port show / expose
EXPOSE 5000

# Run the damn app! 
CMD ["python", "run.py"]
