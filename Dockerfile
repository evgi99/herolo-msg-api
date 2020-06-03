FROM python:3

ADD . /

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD [ "python", "./manage.py" ,"runserver", "--host=0.0.0.0", "--port=8000"]