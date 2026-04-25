FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

# Install Python + pip (already present but safe)
RUN apt-get update && apt-get install -y python3 python3-pip

# Install dependencies
RUN pip3 install flask selenium

CMD ["python3", "test.py"]