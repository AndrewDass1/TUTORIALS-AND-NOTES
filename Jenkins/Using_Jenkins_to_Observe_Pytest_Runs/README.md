# USING_JENKINS_TO_OBSERVE_PYTEST_RUNS
This Repository contains a Python script which includes the module pytest. It is also connected to the CI/CD tool Jenkins and automated to run five times in the first minutes of every hour. 

## Materials Used
* Github - Source control
* Jenkins - CI/CD tool
  * In this demonstration, Docker was used to access Jenkins
  
## Procedure
1. Create a new Github repository. Write a Python script that includes pytest. Refer to the source code in this repository for an example. 
2. Run a Docker container that enables Jenkins. For further instructions to run a Jenkins Docker container, follow the specific guides on the official Jenkins website to run a Jenkins Docker container for either the macOS, Linux or Windows Operating Systems

Jenkins Docker Documentation: https://www.jenkins.io/doc/book/installing/docker/

To create a container, there are a few steps to follow, including to make a Dockerfile on Step 4 for any of the three operating systems. In this demonstration, two lines are added to the Dockerfile after the line of code "RUN apt-get update && apt-get install -y lsb-release":
```
RUN apt-get install python3-pip -y
RUN pip install -U pytest
```

When the Docker container is created, it downloads prerequisite software and runs commands to function properly. The two lines that are added above installs the package pip and pytest. Installing the pip command makes it easier to download other packages including pytest.  

3. After successfully making the Jenkins Docker Container, enter Jenkins through the internet browser by typing into the search bar:
```
localhost:8080
```
The Jenkins login setup page is shown below:
<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins5.png" width="600" />
     </h1>
</html>


The "Administrator Password" can be found in the "Logs" section in the Docker container

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins6.png" width="600" />
     </h1>
</html>

4. When customizing Jenkins, install plugins that are neccessary to run scripts. In this demonstration, "Install suggested plugins" was selected.

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins7.png" width="600" />
     </h1>
</html>

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins9.png" width="600" />
     </h1>
</html>

5. Create a Username, password and confirm an E-mal address or choose "Skip and continue as admin"
<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins9.png" width="600" />
     </h1>
</html>

6. When finishing setting up Jenkins, on the top right of the corner there is a shield icon. The shield icon provides many options and gives the option to update Jenkins by downloading software and any updating existing softwares to the latest versions. Click on "Manage Jenkins"

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins9-2.png" width="1000" />
     </h1>
</html>

Select "Manage Plugins"
<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins9-3.png" width="1000" />
     </h1>
</html>

Here, shows there can be updates and if there are any updates that need to be installed, carefully follow the directions. The left-bar menu gives the options to download or customize plugins or settings to run scripts.
<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins9-4.png" width="1000" />
     </h1>
</html>


7. After updating Jenkins, select "New Item" and choose "Pipeline" and connect this "Pipeline" job to read the files from the Github repository that contains the source code

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins10.png" width="1000" />
     </h1>
</html>

By providing the Github url, Jenkins now knows which Github repository is being referred to.
<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins11.png" width="1000" />
     </h1>
</html>

By enabling the option, "Build periodically" allows the script to run at a specified time. The code "0-5 0-23 * * *" means the script will run for the first minutes of every new hour.

Enabling the option, Github hook trigger will execute the Jenkins pipeline every time the source code was updated in the Github repository. 

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins11-2.png" width="1000" />
     </h1>
</html>


Below specifies what repository, which branch, how and where the files can be found in the Github repository to make sure Jenkins can find and execute the files that are given to it. Jenkins always executes a "Jenkinsfile" and in this repository, it is located in the path "/Jenkins/Jenkinsfile". The Jenkinsfile has commands or instructions to execute any other files in any of the repositories' directories if specified.
<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins12.png" width="1000" />
     </h1>
</html>

<html>
     <h1>
        <img style="float: center;" src="/Jenkins/Using_Jenkins_to_Observe_Pytest_Runs/pictures/jenkins13.png" width="1000" />
     </h1>
</html>
