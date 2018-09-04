# Use an official Python runtime as a parent image
FROM ubuntu:16.04

# Set the working directory to /app
WORKDIR /dag_app

# Copy the current directory contents into the container at /app
ADD . /dag_app


# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get upgrade -y && \
    apt-get install apt-utils -y && \
    apt-get install python3-pip -y && \
    apt-get install python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev -y && \
    pip3 install psycopg2 && \
    pip3 install cryptography && \
    pip3 install apache-airflow==1.9
    
# apt-get install redis-server -y
    
# redis-server

# RUN service postgresql start

ENV AIRFLOW_HOME=/dag_app/airflow
    
RUN airflow version

EXPOSE 8080
