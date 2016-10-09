# Python Scikit Application #

[![Build Status](https://travis-ci.org/slahiri/vicious-machines.svg?branch=master)](https://travis-ci.org/slahiri/vicious-machines) [![Code Climate](https://codeclimate.com/github/slahiri/vicious-machines/badges/gpa.svg)](https://codeclimate.com/github/slahiri/vicious-machines) [![Issue Count](https://codeclimate.com/github/slahiri/vicious-machines/badges/issue_count.svg)](https://codeclimate.com/github/slahiri/vicious-machines) [![Test Coverage](https://codeclimate.com/github/slahiri/vicious-machines/badges/coverage.svg)](https://codeclimate.com/github/slahiri/vicious-machines/coverage)

[![nodesource/node](http://dockeri.co/image/lahirs2/vicious-machines)](https://registry.hub.docker.com/u/lahirs2/vicious-machines/)

Build the image using the following command

```bash
$ docker build -t lahirs2/vicious-machines:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d --name vicious-app -p 5000:5000 lahirs2/vicious-machines:latest
```

Execute unit test case

```bash
$ docker exec vicious-app python -m unittest discover
```

Login to bash
```bash
$ sudo docker exec -i -t <CONTAINER ID> /bin/bash
```

Kill Application Instance
```bash
$ docker rm -f vicious-app
```

Simple CURL tests
```bash
$ curl -X GET http://127.0.0.1:5000/
[{"url": "http://127.0.0.1:5000/0/", "text": "do the shopping"}, {"url": "http://127.0.0.1:5000/1/", "text": "build the codez"}, {"url": "http://127.0.0.1:5000/2/", "text": "paint the door"}]
$ curl -X GET http://127.0.0.1:5000/1/
{"url": "http://127.0.0.1:5000/1/", "text": "build the codez"}
$ curl -X PUT http://127.0.0.1:5000/1/ -d text="flask api is teh awesomez"
{"url": "http://127.0.0.1:5000/1/", "text": "flask api is teh awesomez"}
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`
