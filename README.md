# Python Scikit Application #

[![Build Status](https://travis-ci.org/slahiri/vicious-machines.svg?branch=master)](https://travis-ci.org/slahiri/vicious-machines) [![Code Climate](https://codeclimate.com/github/slahiri/vicious-machines/badges/gpa.svg)](https://codeclimate.com/github/slahiri/vicious-machines) [![Issue Count](https://codeclimate.com/github/slahiri/vicious-machines/badges/issue_count.svg)](https://codeclimate.com/github/slahiri/vicious-machines) [![Test Coverage](https://codeclimate.com/github/slahiri/vicious-machines/badges/coverage.svg)](https://codeclimate.com/github/slahiri/vicious-machines/coverage) [![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?maxAge=2592000)](https://gitter.im/sid-ai/vicious-machines?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

[![nodesource/node](http://dockeri.co/image/lahirs2/vicious-machines)](https://registry.hub.docker.com/u/lahirs2/vicious-machines/)


## Models Implemented ##

- DecisionTreeClassifier
```python
# Classification Data
# [Height, Weight, Shoe_Size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
```

## Installation ##

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
$ sudo docker exec -i -t vicious-app /bin/bash
```

Kill Application Instance
```bash
$ docker rm -f vicious-app
```

## Simple CURL tests ##
```bash
$ curl -X GET http://127.0.0.1:5000/
[{"url": "/classify/", "model": "Classification"}]

$ curl -X GET http://127.0.0.1:5000/classify/
[{"sample": {"weight": 70, "height": 170, "key": 0, "shoe": 43}, "classifier_type": "DecisionTreeClassifier"}, {"sample": "{}", "classifier_type": "Classifier 1"}, {"sample": "{}", "classifier_type": "Classifier 2"}]

$ curl -H "Content-Type: application/json" -X POST -d '{"weight": 70, "height": 170, "key": 0, "shoe": 43}' http://127.0.0.1:5000/classify/
{"gender": "male"}
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`
