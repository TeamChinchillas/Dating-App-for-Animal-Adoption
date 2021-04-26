FROM python:3.9.4
RUN mkdir -p /var/www/animal_adoption
WORKDIR /var/www/animal_adoption
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD flask run
