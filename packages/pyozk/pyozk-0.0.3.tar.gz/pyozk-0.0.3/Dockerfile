FROM python:3.10.11

LABEL MAINTAINER="Chinh Nguyen <chinhnc2@gmail.com>"

# ENV GROUP_ID=1000 \
#     USER_ID=1000

WORKDIR /home/app

COPY . /home/app
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y netcat
RUN apt-get update && apt-get install -y iputils-ping

# RUN groupadd -g $GROUP_ID www
# RUN useradd -u $USER_ID -g www www -s /bin/sh

# USER www

# EXPOSE 5000

# CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]
CMD ["python3", "app.py"]