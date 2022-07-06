FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y unixodbc-dev unixodbc libaio1 python3-dev gcc libpq-dev git
RUN apt-get install -y libpq-dev postgresql mdbtools

ARG user=swadm
ENV HOME /home/$user
RUN adduser $user

COPY . Friday
WORKDIR /Friday

RUN pip install pipenv
RUN pipenv install --skip-lock --sequential

RUN chown -R $user:$user /Friday
USER $user