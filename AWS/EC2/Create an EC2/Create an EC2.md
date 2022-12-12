# Create an EC2

This is a tutorial of how to make an EC2 on AWS and to connect to it by using SSH. The following is needed:
* Make an AWS account

## Procedure
1. Log in into AWS
2. Select EC2 to create one

<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/1.png" width="1000" />
     </h1>
</html> 

3. Select "Launch Instance"
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/2.png" width="1000" />
     </h1>
</html>

4. Give an EC2 a name, in this tutorial it will be named "test". Also, the option is given to select
what image the EC2 will be based off of. In this tutorial, the "Amazon Linux" image will be used.
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/3.png" width="1000" />
     </h1>
</html>

5. Choose the Architecture and instance type. 64-bit (x86) and t2.micro are used respectively. t2.micro is
a free-tier option. Afterwards, select "Create new key pair" to make a key pair login.  
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/4.png" width="1000" />
     </h1>
</html>

6. Give a name to the key pair. In this tutorial, the key pair will be named "test". Select "RSA" and .pem 
for "Key pair type" and "Private key file format" respectively. After creating it, the key pair file should be
downloaded onto the computer in the "Downloads" directory by default. To access the EC2, this key pair file
cannot be deleted!
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/5.png" width="1000" />
     </h1>
</html>

7. Choose "Create security group" if no security groups exist, otherwise choose "Select existing security group". Checkmark the box "Allow SSH traffic from", to enable the ssh feature to connect to the Amazon Linux 
image by using port 22. 
* Optional - Checkmarking the boxes "Allow HTTPS traffic from the internet" and "Allow HTTP traffic from the internet" allows to connect to the instance from ports 443 and 80. 

<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/6.png" width="1000" />
     </h1>
</html> 

After completing these steps, select the orange button "Launch instance" to make the EC2. There should be a confirmation after selecting "Launch instance" similar to the image shown below 
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/7.png" width="1000" />
     </h1>
</html> 

After a few minutes, the EC2 will run and show its status that its "running" under instance state
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/8.png" width="1000" />
     </h1>
</html> 

7. Under description, save the "IPv4 Public IP" address

8. Open a CLI tool, and log in into the EC2. The following format is used:
```
ssh -i "name_of_key_pair_file".pem "amazon_image"@"IPv4 Public IP"
```
* In this tutorial:
  * The name of the key pair file is "test.pem"
  * Since an Amazon Linux EC2 was created, in place of "amazon_image", write "ec2-user". This variable is case-sensitive as it depends what type of EC2 was created. 
  * For "IPv4 Public IP", insert the IPv4 Public IP address that was generated for the EC2
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/11.png" width="1000" />
     </h1>
</html> 

## Cleaning Up
9. To exit of the instance, write "exit" to logout from the EC2
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/12.png" width="1000" />
     </h1>
</html> 
10. To delete the instance forever, terminate it.
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/11.png" width="1000" />
     </h1>
</html> 
* The instance can remain while be ordered to stop running by selecting the "Stop" option to prevent billing charges. <br> 
<br>
11. Another warning page pops-up to confirm that this EC2 will be terminated and the consequences of doing so. Read the instructions and select "Yes, Terminate" when ready to delete the instance. 
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/14.png" width="1000" />
     </h1>
</html> 
12. After terminating, the status of the EC2 shows it is in progress of shutting down and finally terminates
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/15.png" width="1000" />
     </h1>
</html> 
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/16.png" width="1000" />
     </h1>
</html> 

13. Once an EC2 is deleted, the Key pair generated with the EC2 becomes useless since that specific Key pair can only be used to access the deleted EC2. To also delete the Key pair, select "Key pairs" on the EC2 Dashboard.

14. Select the Key pair that was associated with the deleted EC2. Then, select "Actions" and press "Delete"
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/18.png" width="1000" />
     </h1>
</html> 
A pop-up occurs to give a final warning whether to delete the Key pair. When ready, type "delete" in the box and select the orange button "Delete" to delete the Key pair.
<html>
     <h1>
        <img style="float: center;" src="/AWS/EC2/Create an EC2/images/19.png" width="1000" />
     </h1>
</html> 
