# Running a Docker Container


In this guide, we will cover how to run a Docker container using the `docker run` command. This command allows you to run a new container from a given image, specify various options for how the container should be run, and specify the command that should be run inside the container.

## Prerequisites
---

Before you can run a Docker container, you must have the following prerequisites:

1.  Install Docker on your machine. You can find instructions for doing this on the [Docker website](https://docs.docker.com/get-docker/).

## Build the Image
---

To build the image, use the following command:
`docker build -t python-docker .`

## Running the Container
---

To run a Docker container, use the following command:

`docker run -d -p 5000:5000 python-docker`

