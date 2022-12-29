# Running a Docker Container


In this guide, we will cover how to run a Docker container using the "docker run" command. This command allows you to run a new container from a given image, specify various options for how the container should be run, and specify the command that should be run inside the container.

## Prerequisites
---

Before you can run a Docker container, you must have the following prerequisites:

1.  Install Docker on your machine. You can find instructions for doing this on the [Docker website](https://docs.docker.com/get-docker/).

2.  Build a Docker image. You can do this using the `docker build` command, or you can pull an image from a Docker registry such as [Docker Hub](https://hub.docker.com/).

## Running a Container
---

To run a Docker container, you can use the `docker run` command followed by various options and the name of the image you want to run.

Here is an example command for running a container:

`docker run -d -p 5000:5000 --tag [TAG]`

This command does the following:

-   `-d`: Runs the container in detached mode, which means it runs in the background and leaves the command prompt available for you to use.

-   `-p 5000:5000`: Maps the host machine's port 5000 to the container's port 5000. This allows you to access the container's application on port 5000 of the host machine.

-   `--tag [TAG]`: Specifies the Docker tag of the image to use. This should be replaced with the tag provided by the end user when building the image.

