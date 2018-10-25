FROM python:3.6.6-jessie

COPY requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip3 install -r requirements.txt
COPY . /src
ENTRYPOINT python3 /src/app.py
