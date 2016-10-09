FROM lahirs2/vicious-machines:latest
MAINTAINER Siddhartha Lahiri "siddhartha.lahiri@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
