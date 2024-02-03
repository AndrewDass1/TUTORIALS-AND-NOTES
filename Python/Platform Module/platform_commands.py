import platform

print(platform.platform())
# print(platform(1))
# print(platform(0,1))

print(platform.machine())

print("Processor:",platform.processor())

print("System:",platform.system())

print("Version:",platform.version()) #Check the about section to see if it is the same

print(platform.python_implementation())

print("Python Version:",platform.python_version_tuple())

print("Python Node:",platform.node())

print("Python Build",platform.python_build())

print("Python Compiler",platform.python_compiler())

print("Python Branch",platform.python_branch())

print("Python_revision",platform.python_revision())

print("Python Version",platform.python_version())

print("Python version tuple",platform.python_version_tuple())

print("Python Release",platform.release())
# Reads Operating System Version

print("Python Uname",platform.uname())
# Reads six attributes
