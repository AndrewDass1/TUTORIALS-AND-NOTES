# NOTE : Every line that starts with '#' is a comment to explain how a Dockerfile should be formatted to download packages to run a functionable Docker container that uses the Alpine operating system.

# First line: Run the official Alpine image or an image that uses the Alpine OS:
FROM image_name:version

# Next RUN apk update and upgrade to ensure the container can successfully install future packages

RUN apk update

RUN apk upgrade

# Next files or folders can either be copied from the local machine onto the container by using the 'COPY' or 'ADD' command respectively

COPY 

ADD

# Expose a port number to access the application, if the container is running an application

EXPOSE 80
