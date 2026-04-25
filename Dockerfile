FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

# Install Python dependencies
RUN pip3 install flask selenium

# Run Flask app first, then run test
CMD bash -c "python3 app.py & sleep 5 && python3 test.py"