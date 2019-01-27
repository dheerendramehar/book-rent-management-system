FROM ubuntu

RUN apt-get update

RUN apt-get install python3-tk -y

COPY rent_calc.py /rent_calc.py

CMD ./rent_calc.py

