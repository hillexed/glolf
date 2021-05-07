FROM alpine:3.12.1
WORKDIR /root/

RUN ["apk", "--update-cache", "add", "python3", "python3-dev", "py3-pip", "gfortran", "musl-dev", "linux-headers", "g++"]

COPY glolf/requirements.txt /root/requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY glolf/ /root/glolf/

WORKDIR /root/glolf

CMD env > .env && python3 bot.py
