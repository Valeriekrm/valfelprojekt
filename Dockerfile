FROM python:3

ADD . /code

RUN apt-get update

RUN apt-get install -y python3 python-dev python-pip

RUN pip3 install -U nltk

RUN apt-get install -y python-scipy


RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet

WORKDIR /code

ENV DISPLAY :0

COPY . .

CMD [ "python3", "./FertigesProjektKrommMäder.py" ]