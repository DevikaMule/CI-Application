FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

# Install Python dependencies
RUN pip3 install flask selenium

CMD ["python3", "test.py"]