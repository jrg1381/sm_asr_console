FROM python:3.6.6-jessie as base

ARG DEFAULT_LICENSE_CODE
ARG DEFAULT_USERNAME
ARG DEFAULT_COMPANY
ARG DEFAULT_EMAIL

ENV DEFAULT_LICENSE_CODE=${DEFAULT_LICENSE_CODE} \
    DEFAULT_USERNAME=${DEFAULT_USERNAME} \
    DEFAULT_COMPANY=${DEFAULT_COMPANY} \
    DEFAULT_EMAIL=${DEFAULT_EMAIL}
COPY requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip3 install -r requirements.txt
COPY . /src
ENTRYPOINT python3 /src/app.py

FROM python:3.6.6-jessie as sm_asr_console_builder
RUN apt-get update && apt-get install -y make
COPY --from=base /src /src
COPY requirements-dev.txt /src/requirements-dev.txt
WORKDIR /src
RUN pip3 install -r requirements.txt -r requirements-dev.txt
