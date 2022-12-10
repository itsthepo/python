import json
from faker import Faker
import random
import hashlib
import re

print("Please enter the number of logs you would like created")
num_times = int(input())
for i in range(num_times):
  def randomize_json(json_file, num_times):
  # Load the JSON file
   with open(json_file, "r") as f:
    data = json.load(f)

  # Recursively loop through the keys in the JSON file and
  # assign a random value to each key
    def randomize(obj):
      faker = Faker()
      for key in obj:
      
        # Generate random IP address if user has flagged the key as an IP. 
        if obj[key] == "ip":
          obj[key] = faker.ipv4()
        
        # Generate if the value is a string data type but a series of numbers
        elif obj[key] == "int":
          obj[key] = random.randint(0,10000000)
        
        # Generate random user if field was flagged as user
        elif obj[key] == "user": 
          # List of possible first names
          first_names = ["John", "Jane", "Tom", "Sally", "Bob"]

          # List of possible last names
          last_names = ["Smith", "Doe", "Johnson", "Williams", "Brown"]

          # Generate a random username by concatenating
          # a random first name and last name
          obj[key] = random.choice(first_names) + random.choice(last_names)
        
        # Generate Mac Address 
        elif obj[key] == "mac": 
          obj[key] = "02:%02x:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))  
        
        # Generate File Names
        elif obj[key] == "file_name":
          file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
          obj[key] = random.choice(file_names)

        # Generate File Paths
        elif obj[key] == "file_path": 
          file_names = ["file1.txt", "file2.exe", "file3.js", "file4.pdf", "file5.docx", "file.elf"]
          directories = ["C:\\Windows\\System32\\", "C:\\Windows\\", "/home/po", "/tmp", "/opt"]
          obj[key] = random.choice(directories) + "/" + random.choice(file_names)

        # Generate Command Line
        elif obj[key] == "command_line":
          ps_commands = ["Get-ChildItem", "Set-Location", "New-Item", "Remove-Item", "Get-Content"] 
          ps_commandline = "Powershell.exe" + "/" + random.choice(ps_commands)
          obj[key] = random.choice(ps_commandline)
          
        
        # Generate SHA 256 Hash 
        elif obj[key] == "sha_256":
          obj[key] = hashlib.sha256(str(random.random()).encode("utf-8")).hexdigest()

        # Generate MD5 String
        elif obj[key] == "md5":
          obj[key] = hashlib.md5(str(random.random()).encode("utf-8")).hexdigest()


        # Computer names
        elif obj[key] == "computer_name": 
          computer_names = ["computer1", "computer2", "computer3", "computer4", "computer5"]
          obj[key] = random.choice(computer_names)

        elif isinstance(obj[key], int): 
          obj[key] = random.randint(0,10000000)
        
        elif isinstance(obj[key], bool): 
          obj[key] = random.choice(["True", "False"])

        elif isinstance(obj[key], str):
          pattern = r"keep\|(.*?)$"
          match = re.search(pattern, obj[key])
          if match: 
            obj[key] = match.group(1)
          else:
            obj[key] = random.choice(["helloworld", "worldtest", "foodwadadad", "baawdadawdadadr"])
        
        elif isinstance(obj[key], list):
        # If the key's value is a list, assign a random list
          obj[key] = [random.randint(1, 100), random.choice(["hello", "world", "foo", "bar"])]
        
        elif isinstance(obj[key], dict):
        # If the key's value is a dictionary, recursively call the function
          randomize(obj[key])

  # Call the randomize function to generate random values for the keys
    randomize(data)

  # Write the randomized data to a new JSON file
    with open("randomized_" + str(i) + json_file, "w") as f:
      json.dump(data, f)

#### Code here that will be repeated with the for loop above , that does a HTTPS webhook push to a url the user will input.

  if __name__ == "__main__":
  # Provide the name of the JSON file you want to randomize
    randomize_json("example.json", num_times)