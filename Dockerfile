FROM lahirs2/vicious-machines:slim
MAINTAINER Siddhartha Lahiri "siddhartha.lahiri@gmail.com"
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
