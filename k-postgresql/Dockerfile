# set base image (host OS)
FROM python:3.8

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY src/ .

CMD tail -f /dev/null