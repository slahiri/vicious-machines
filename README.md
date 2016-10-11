# Python Scikit Application #

[![Build Status](https://travis-ci.org/slahiri/vicious-machines.svg?branch=master)](https://travis-ci.org/slahiri/vicious-machines) [![Code Climate](https://codeclimate.com/github/slahiri/vicious-machines/badges/gpa.svg)](https://codeclimate.com/github/slahiri/vicious-machines) [![Issue Count](https://codeclimate.com/github/slahiri/vicious-machines/badges/issue_count.svg)](https://codeclimate.com/github/slahiri/vicious-machines) [![Test Coverage](https://codeclimate.com/github/slahiri/vicious-machines/badges/coverage.svg)](https://codeclimate.com/github/slahiri/vicious-machines/coverage) [![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?maxAge=2592000)](https://gitter.im/sid-ai/vicious-machines?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

[![GitHub forks](https://img.shields.io/github/forks/slahiri/vicious-machines.svg?style=social&label=Fork)](https://github.com/slahiri/vicious-machines)
[![GitHub stars](https://img.shields.io/github/stars/slahiri/vicious-machines.svg?style=social&label=Star)](https://github.com/slahiri/vicious-machines)
[![GitHub watchers](https://img.shields.io/github/watchers/slahiri/vicious-machines.svg?style=social&label=Watch)](https://github.com/slahiri/vicious-machines)
[![GitHub followers](https://img.shields.io/github/followers/siddhartha-lahiri.svg?style=social&label=Follow)](https://github.com/slahiri/vicious-machines)
[![Twitter Follow](https://img.shields.io/twitter/follow/sid_2vicious.svg?style=social)](https://twitter.com/sid_2vicious)

[![nodesource/node](http://dockeri.co/image/lahirs2/vicious-machines)](https://registry.hub.docker.com/u/lahirs2/vicious-machines/)

## Implementation
Currently the code implements simple Classifier implementation to predict gender based on height, weight, show_size data.

Implemented models
- DecisionTreeClassifier
- KNeighborsClassifier
- LogisticRegression
- GaussianNB
- RandomForestClassifier

## Installation
Build the image using the following command

```bash
$ docker build -t lahirs2/vicious-machines:slim .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d --name vicious-app -p 5000:5000 lahirs2/vicious-machines:slim
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

## CURL Tests
```bash
$ curl -X GET http://127.0.0.1:5000/

$ curl -X GET http://127.0.0.1:5000/classify/

$ curl -X GET http://127.0.0.1:5000/classify/
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`

## References
- 
