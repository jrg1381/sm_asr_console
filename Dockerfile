FROM python:3.6.6-jessie

COPY . /src
WORKDIR /src
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 /src/app.py
