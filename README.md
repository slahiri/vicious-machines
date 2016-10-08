# Python Scikit Application #

[![Build Status](https://travis-ci.org/slahiri/vicious-machines.svg?branch=master)](https://travis-ci.org/slahiri/vicious-machines) [![Code Climate](https://codeclimate.com/github/slahiri/vicious-machines/badges/gpa.svg)](https://codeclimate.com/github/slahiri/vicious-machines)

[![nodesource/node](http://dockeri.co/image/lahirs2/vicious-machines)](https://registry.hub.docker.com/u/lahirs2/vicious-machines/)

Build the image using the following command

```bash
$ docker build -t lahirs2/vicious-machines:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d --name vicious-app -p 5000:5000 lahirs2/vicious-machines:latest
```

```bash
$ docker exec vicious-app python -m unittest discover
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`
