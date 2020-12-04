FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev  

RUN apt install

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /TCHAI-Steven-TEL-Florian-SARI/requirements.txt

WORKDIR /TCHAI-Steven-TEL-Florian-SARI

RUN pip3 install -r requirements.txt

COPY . /TCHAI-Steven-TEL-Florian-SARI/

EXPOSE 5000


RUN python3 server.py
RUN sh test.sh

