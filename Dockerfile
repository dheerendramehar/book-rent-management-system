FROM ubuntu

RUN apt-get update

RUN apt-get install python3-tk -y

COPY calc.py /calc.py

CMD ./calc.py
