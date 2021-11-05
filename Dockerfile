# taken from - https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ 

# pull the official base image

FROM python:3.9.7-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY ./ows/* /usr/src/app/
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt
EXPOSE 8000


RUN flake8 --ignore=E501,F401 .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt



# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/app && addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web/
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

COPY ./ows $APP_HOME
COPY ./build /build

RUN apk update && apk add libpq; pip install --no-cache /wheels/*; chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/build/entrypoint.dev.sh"]