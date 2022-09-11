FROM python:buster

LABEL org.opencontainers.image.authors="I2etr0"

# create work direcory for app
RUN mkdir /app
WORKDIR /app

# copy files from pc to container
COPY bot.py /app
COPY parser.py /app
COPY docker-entrypoint.sh /app

# install library for python
RUN apt update \
    && pip install telebot requests beautifulsoup4 pyTelegramBotApi

# set entrypoint as file
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
CMD [ "python3" ]
