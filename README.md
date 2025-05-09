Theory
docker pull <image> — download an image.

docker images — view a list of downloaded images.

docker run <image> — run a container from an image.

docker ps — view running containers.

docker stop <container_id> — stop a container.

docker rm <container_id> — remove a container.

docker rmi <image> — remove an image.

Practice
1.Download image "hello-world", creat and run container with flag "-it" to see:
"Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/"
 2.Download image "python:3.9", creat and run container with flag "-it" and write some comands:
>>> 1+1
2
>>> 2+3
5
>>> print("hello")
hello