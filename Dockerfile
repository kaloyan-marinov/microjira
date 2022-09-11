FROM python:3.8.3-alpine

# https://github.com/python-greenlet/greenlet/issues/232#issuecomment-910128433
# https://stackoverflow.com/questions/60595581/failed-to-install-gcc-on-python-3-7-alpine-docker-container#comment118193890_64352966
RUN apk add \
    build-base \
    libffi-dev

RUN adduser -D the-mighty-user

WORKDIR /home/the-mighty-user

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip \
 && venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY migrations migrations
COPY application.py ./

COPY boot.sh ./
RUN chmod a+x boot.sh

# declare build-time variables
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_REGION $AWS_REGION

ENV FLASK_APP application.py

RUN chown -R the-mighty-user:the-mighty-user ./
USER the-mighty-user

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
