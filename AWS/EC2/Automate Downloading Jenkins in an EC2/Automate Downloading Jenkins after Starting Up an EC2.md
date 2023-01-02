# Automate Downloading Jenkins after Starting Up an EC2
EC2 have the option to automate softwares from startup. What that means is, instead of first creating
an EC2 and then manually type in commands or code to download software, there is an option before creating
the EC2 in "Advanced Settings" called "User Data". Any commands that is listed in "User Data" will be run automatically
and download programs if instructed to do so. The EC2 does take a few minutes to read and run every command that is provided.
In this demonstration, an EC2 will be created to automatically download Jenkins which takes it about
two minutes.

## Materials or Software Used
* AWS Account

## Procedure
1. Login and access AWS, and go to "EC2"
2. Select the "Instances" option, and then select the "Launch an Instance" option
<html>
     <h1>
        <img style="float: center;" src="AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/1.png" width="1000" />
     </h1>
</html> 
* A security group needs to be created to allow ports 22 and 8080 
3. Click on the "Advanced Details" and more option should appear afterwards. Click it and scroll down
to "User Data"
4. In User Data, instructions can be pasted to download software. In this case, instructions from the
official Jenkins website will be pasted in "User Data" to download Jenkins. The script used in this 
demonstration is shown down below under "User Data Script"
5. Log into the newly created Instance. As the instance is starting up, it also takes two to three minutes
to read and run the commands in the "User Data". After waiting for two to three minutes, in the ec2 terminal,
write:
```
sudo systemctl status jenkins
```
After receiving a message similar shown below, Jenkins is downloaded.


6. Access Jenkins through an internet browser by using: 
```
EC2IPv4address:8080
```
After accessing Jenkins, a page similar down below should appear


After accessing Jenkins through the internet browser, using the same command in the terminal
```
sudo systemctl status jenkins
```
Will now show that Jenkins is active since it is currently being accessed and used from the internet
browser
7. Write the following command in the terminal:
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
This is the password that is required to enter into the Jenkins "Adminstrator Password" box. Afterwards,
Jenkins can now be customized and then be used.


## User Data Script
```
#!/bin/bash

sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

sudo yum upgrade -y

sudo amazon-linux-extras install -y java-openjdk11

sudo yum install -y jenkins

sudo systemctl daemon-reload

sudo systemctl enable jenkins

sudo systemctl start jenkins
```
