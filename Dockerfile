FROM python:2.7
MAINTAINER Siddhartha Lahiri "siddhartha.lahiri@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
