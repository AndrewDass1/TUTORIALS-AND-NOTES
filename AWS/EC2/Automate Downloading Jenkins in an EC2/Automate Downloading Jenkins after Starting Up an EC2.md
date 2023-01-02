# Automate Downloading Jenkins after Starting Up an EC2
There is an option for Amazon EC2 to automate downloading softwares from startup. There is an option in "Advanced Settings" called "User Data". Any commands that is listed in "User Data" will be run automatically and download programs if instructed to do so. The EC2 does take a few minutes to read and run every command that is provided. Using this option saves time from instead first creating an EC2 and then manually type in commands or code to download software. In this demonstration, an EC2 will be created to automatically download Jenkins which takes it about two minutes.

## Materials or Software Used
* AWS Account

## Procedure
1. Login and access AWS, and go to "EC2"
2. Select the "Instances" option, and then select the "Launch Instances" option
* A security group needs to be created to allow ports 22 and 8080. Port 22 is needed to ssh into the instance and port 8080 is used by default to access Jenkins and also used in this demonstration. 
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/1.png" width="200" />
     </h1>
</html> 


3. Click on the "Advanced Details" and more options should appear afterwards. Click it and scroll down
to "User Data"
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/2.png" width="400" />
     </h1>
</html>

<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/3.png" width="400" />
     </h1>
</html> 

4. In User Data, instructions can be pasted to download software. In this case, instructions from the
official Jenkins website will be pasted in "User Data" to download Jenkins. The script used in this 
demonstration is shown down below under "User Data Script"
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/3-2.png" width="400" />
     </h1>
</html> 

5. Log into the newly created Instance. As the instance is starting up, it also takes two to three minutes
to read and run the commands in the "User Data". After waiting for two to three minutes, type following the command in the ec2 terminal:
```
sudo systemctl status jenkins
```
After receiving a message similar shown below, Jenkins is downloaded though it shows it is not active:
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/4.png" width="1000" />
     </h1>
</html> 
This is because Jenkins is downloaded but it is not currently being used. A new message should appear when Jenkins is accessed or being used.

6. Access Jenkins through an internet browser by using: 
```
EC2IPv4address:8080
```
After accessing Jenkins, a page similar down below should appear
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/5.png" width="800" />
     </h1>
</html> 


After accessing Jenkins through the internet browser, use the same command in the terminal:
```
sudo systemctl status jenkins
```
Now Jenkins will show it is active since it is currently being accessed and used from the internet browser
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/6.png" width="1000" />
     </h1>
</html> 

7. Write the following command in the terminal:
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
This is the password that is required to enter into the Jenkins "Adminstrator Password" box. Afterwards, Jenkins can now be customized and then be used.

<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Automate Downloading Jenkins in an EC2/pictures/7.png" width="800" />
     </h1>
</html> 


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
