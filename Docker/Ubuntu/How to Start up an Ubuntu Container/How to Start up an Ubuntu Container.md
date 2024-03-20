# How to Start up an Ubuntu Container
This tutorial is a guide how to startup a Docker Container that runs Ubuntu. The following is needed to be installed on a computer for this tutorial:
* Docker or Docker Desktop
* Dockerhub (Optional)
To visit Docker and to download the software, there are instructions on the official Docker website for all operating systems: https://www.docker.com/

## What is Docker?
Docker is a software that creates containers. Containers are built to run fully developed applications which could be shared and run on other computers.
For example, if one computer contains the source code for a Word Generator application, it could be distributed through other computers by first converting the source
code into an image and run it to make a container to access the application. It is optional the image can be published to Dockerhub, where other computers 
can download the image and run it. Dockerhub is a place where pre-existing Docker images exist, and this tutorial will demonstrate how to download the official 
Ubuntu image and run it. To visit Dockerhub and see many pre-existing images, please visit the official website: https://hub.docker.com/
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/DockerHomepage.png" width="1000" />
     </h1>
</html>
<br>

On the top-left of the screen, an image can be searched by using the search bar <br>

<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/DockerhubHomepage.png" width="1000" />
     </h1>
</html> 

To navigate the entire image list, scroll down and click on "See all Docker Official Images"

<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/DockerhubHomepage2.png" width="1000" />
     </h1>
</html> 

The image list:
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/Dockerhub3.png" width="1000" />
     </h1>
</html>

## Downloading an Ubuntu Container
* Docker or Docker Desktop must be installed onto the computer for the following steps to work. Docker and Docker Desktop must be currently running while running
the following steps. 

1. Open a CLI tool
2. Type "docker" to see if it is installed on the machine
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI1.png" width="1000" />
     </h1>
</html>
If Docker is installed, an output should be outputted to how to use many commands should be received
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI2.png" width="1000" />
     </h1>
</html>

3. Any existing docker image can be pulled by using the
```
docker pull name:tag
```
By specifying the name of the image, that image will be pulled and the tag is the version of that particular image. If the tag is not specified, the latest version of that image will always be pulled. To pull the Ubuntu image the following command is:
```
docker pull ubuntu:latest
```
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI4.png" width="1000" />
     </h1>
</html>
4. To see if the image is on the computer, input the following command:
```
docker images
```
"docker images" shows the current existing images that were downloaded or built onto the computer. If the Ubuntu image was downloaded, it should be specified that it is there
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI5.png" width="1000" />
     </h1>
</html>
5. By having the Ubuntu image, it is possible to run the image and make a container from it, which gives access to the Ubuntu operating system. Running the image is done by:
```
docker run -i -name=running_an_ubuntu_container -t ubuntu /bin/bash
```
If successful, all commands will be within the container root space
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI7.png" width="1000" />
     </h1>
</html>
6. When creating a new container from any operating system, a good precaution is to always update and upgrade it
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI8.png" width="1000" />
     </h1>
</html>

## Cleaning Up
7. To leave the container, type:
```
exit
```
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI9.png" width="1000" />
     </h1>
</html>

8. To delete the container, go to Dockerhub and press the trash bin icon
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI10.png" width="1000" />
     </h1>
</html>
9. To delete the image
```
docker rmi -f ubuntu
```
* ubuntu is the name of the image. Can specify the image_ID instead to delete it the image
<html>
     <h1>
        <img style="float: center;" src="/Docker/Ubuntu/How to Start up an Ubuntu Container/images/CLI11.png" width="1000" />
     </h1>
</html>
