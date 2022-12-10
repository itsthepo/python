# Log Seeder

## This python script can take any json file as a template. The purpose of this project was to allow researchers, siem engineers, and others to generate random security logs based off their tool stack to help with testing and tuning of detections. This is meant to be used in a pinch and not suitable for a production environement. 

### How to use

1. Open your example log (in my case this was a crowdstrike log), and replace the 'string' values with a [supported string type](#supported-string-types). If there are any ints or booleans, the script will handle that for you. 
    - For example in the CS log, you can see there is a string for username. You will replace that string value with "user", because the script will read the "user" value and generate a random username from the choice list. You will need to do this for FileName, FilePaths, etc. This code can be edited and made to fit your needs! If you do not like the default templates then change them up!

2. After you have sanitzied the example file feed the file into our python script. **Please note, I am going to add accepting files via CLI args later**. It will ask you how many logs you would like to create (i.e., several 1000s and have a collector consume those?) and a URL to send that data via webhook. 


3. Check your webhook destination! 





## Supported String Types
| Strings | Example | 
| :-------------: |:-------------:|
ip | { json_key : "ip" }
int | { json_key : "int" }
user | { json_key : "user" }
mac | { json_key : "mac" }
file_name | { json_key : "file_name" }
file_path | { json_key : "file_path" }
command_line | { json_key : "command_line" }
sha_256 | { json_key : "sha_256" }
md5 | { json_key : "md5" }
computer_name | { json_key : "computer_name" }