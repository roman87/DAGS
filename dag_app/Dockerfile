# Use an official Python runtime as a parent image
FROM ubuntu:16.04

# Set the working directory to /app
WORKDIR /dag_app

# Copy the current directory contents into the container at /app
ADD . /dag_app


# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get upgrade -y && \
    apt-get install apt-utils -y && \
    apt-get install postgresql-9.5 postgresql-contrib-9.5 postgresql-client-9.5 -y && \
    apt-get install python3-pip -y && \
    pip3 install psycopg2 && \
#    export AIRFLOW_GPL_UNIDECODE=yes && \
    pip3 install apache-airflow==1.9
    
# apt-get install redis-server -y
    
# redis-server

# RUN service postgresql start



USER postgres

RUN    /etc/init.d/postgresql start &&\
    psql --command "ALTER USER postgres WITH PASSWORD 'postgres';" &&\
    createdb -O postgres romantest && \
    createdb -O postgres currency && \
    python3 create.py && \
    airflow version

EXPOSE 5432
