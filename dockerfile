FROM ubuntu:jammy

RUN apt-get update && apt-get -y upgrade && apt-get install -y python3

COPY cards.py /code/
COPY player.py /code/
COPY game.py /code/
COPY playGame.py /code/

WORKDIR /code/

CMD ["python3", "playGame.py"]
