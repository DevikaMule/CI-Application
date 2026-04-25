FROM python:3.10

WORKDIR /app
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y wget unzip chromium chromium-driver

RUN pip install flask selenium

# Set Chrome path
ENV PATH="/usr/lib/chromium/:$PATH"

CMD bash -c "python app.py & sleep 5 && python test.py && tail -f /dev/null"