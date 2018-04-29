FROM python:3

WORKDIR /Users/valerie/Desktop/WichtigesProjekt/FertigesProjekt/FertigesProjektKrommMäder.py

COPY . .

CMD [ "python3", "./FertigesProjektKrommMäder.py" ]