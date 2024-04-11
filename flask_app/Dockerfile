FROM python:latest
RUN apt-get update
WORKDIR /flask_app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /flask_app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]