FROM python:2.7
MAINTAINER Eduardo Klosowski <eduardo_klosowski@yahoo.com>
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "wsgi:application"]
