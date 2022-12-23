# How to Setup a MFA

## Materials Needed for this Guide
* An AWS account
* A Virtual MFA App on a Device (Ex: An Authenticator App on a smartphone. Using a smartphone is recommended.)

## What is MFA
MFA stands for Multifactor Authentication. Some websites gives the option to enable MFA when logging into an account on their website. After putting in the information and 
password to log in into an account, the device MFA is set up on generates a passcode that also needs to be entered to sign in into that account. This is useful since
MFA provides another password or layer of security to prevent hackers from entering other people's accounts.

## Procedure
1. Select "IAM"
<html>
     <h1>
        <img style="float: center;" src="/AWS/IAM/Create an MFA/images/1.png" width="750" />
     </h1>
</html> 

2. In the left side of the screen, under "Access Management", select "Users"
<html>
     <h1>
        <img style="float: center;" src="/AWS/IAM/Create an MFA/images/2.png" />
     </h1>
</html> 

3. Click on "Security Credentials tab" and then an option "Assign MFA device" should appear, select it
<html>
     <h1>
        <img style="float: center;" src="/AWS/IAM/Create an MFA/images/3.png" width="1000" />
     </h1>
</html> 

4. Give a name and choose "Virtual MFA device"
<html>
     <h1>
        <img style="float: center;" src="/AWS/IAM/Create an MFA/images/4.png" width="500"/>
     </h1>
</html> 

5. A page now appears with a QR code. Before scanning, have an Authenticator app downloaded prior to scanning. If not, first download an Authenticator app. 
After scanning the QR code, the name that was assigned in Step 4 now appears in the Authenticator app and every few seconds, there is a new number passcode that is generated. <br>  
To complete the setup on AWS, enter the last two MFA codes that was generated. If the MFA is successful, now your password and the MFA passcode is now required to sign-in.
