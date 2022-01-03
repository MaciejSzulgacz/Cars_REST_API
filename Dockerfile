FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /car_service
WORKDIR /car_service
ADD . /car_service/
RUN pip install -r requirements.txt