import os
import subprocess

def detect_os():
# detect the operating system
    if os.name == "nt":
        print("hi, its windows")
        # Windows
        # instructions for installing software on Windows goes here
    elif os.name == "posix" and os.uname().sysname == "Linux":
        command = ""
        print("hi its linux")
    # Unix-like (Linux)
    elif os.name =="posix" and os.uname().sysname == "Darwin":
    # install Sumo Logic 
        print("hi its marky mark the mac")
    else:
    # Unknown OS
        print("Sorry, I don't know how to install software on this operating system.")

detect_os()