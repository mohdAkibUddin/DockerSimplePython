FROM python:latest

RUN mkdir -p /home/user/test/

ADD src/main.py /home/user/test/

ADD rng.py /home/user/test/

WORKDIR /home/user/test/

CMD [ "python", "main.py" ]