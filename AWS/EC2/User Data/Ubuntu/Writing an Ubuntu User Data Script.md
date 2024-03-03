# How to write an Ubuntu User Data Script
1. Include the shebang and directory where the bash file is. The shebang starts off with '#!' followed by the directory where the bash file is found. On most Linux systems, it is often found in the '/bin/bash' directory.

```
#!/bin/bash
```

2. Update and upgrade the system. Some download or package commands ask the user to say yes or no before installing them, writing "-y" means yes to automatically download or run some commands, such as "apt-get upgrade -y" in this case.

```
#!/bin/bash
apt-get update
apt-get upgrade -y
```

3. Install any other additional packages after including the shebang, update and upgrade:
```
apt-get install ... -y
```

Example Ubuntu User Data Script that installs pip for Python:
```
#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install python3-pip -y
```

Note: All aws instances user data scripts runs every command with admin or sudo privileges, so sudo is not needed in any of the commands. 
