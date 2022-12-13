from faker import Faker
from datetime import datetime, timedelta
import json,random, hashlib, re, requests, time, sys, os, string, uuid

print("Please enter the number of logs you would like created")
num_times = int(input())
endpoint_url = input('Please enter a URL: ')
source_category=input('Please provide a sourceCategory (ex. dev/endpoint/cs): ')
print(f'You entered: {endpoint_url}')
filename = sys.argv[-1]
headers = {"X-Sumo-Category": source_category}

time.sleep(2)

def main(): 
  def data_validation(filename):
        ALLOWED_EXTENSIONS = {".json"}
        extension = None
        while extension not in ALLOWED_EXTENSIONS:
            if filename == sys.argv[0]:
                print("Please provide a valid json file with the script. Ex: 'python3 test.py data.json' ")
                return False
            elif filename == sys.argv[-1]:
                extension = os.path.splitext(filename)[1]
                print("We will process this " + filename + " file now")
                return filename
        return filename

  def randomize_json(filename, num_times):
      for i in range(num_times):
        # Load the JSON file
        with open(filename, "r") as f:
          data = json.load(f)

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
              linux_directories = ["/home/po", "/tmp", "/opt"]
              windows_directories = ["C:\Windows\System32", "C:\Windows", "C:\Program Files"]
              linux = random.choice(linux_directories) + "/" + random.choice(file_names)
              windows = random.choice(windows_directories) + "\\" + random.choice(file_names)
              obj[key] = random.choice([linux,windows])

          # Generate Command Line
            elif obj[key] == "command_line":
              ps_commands = ["powershell.exe Get-ChildItem", "powershell.exe Set-Location", "powershell.exe New-Item", "powershell.exe Remove-Item", "powershell.exe Get-Content"] 
              obj[key] = random.choice(ps_commands)
            
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
          
          # network direction
            elif obj[key] == "net_dir": 
                net_dir = ["Inbound", "Outbound", "in", "out"]
                obj[key] = random.choice(net_dir)
          
          # ciphers
            elif obj[key] == "cipher":
              cipher = ["TLS_RSA_WITH_AES_256_CBC_SHA","TLS_RSA_WITH_AES_128_CBC_SHA","TLS_RSA_WITH_3DES_EDE_CBC_SHA","TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA","TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA","TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA","TLS_ECDHE_ECDSA_WITH_RC4_128_SHA","TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA","TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA","TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA","TLS_ECDHE_RSA_WITH_RC4_128_SHA","TLS_RSA_WITH_AES_256_CBC_SHA","TLS_RSA_WITH_AES_128_CBC_SHA","TLS_RSA_WITH_3DES_EDE_CBC_SHA","TLS_RSA_WITH_3DES_EDE_CBC_MD5 ","TLS_RSA_WITH_RC4_128_SHA","TLS_RSA_WITH_RC4_128_MD5","TLS_RSA_EXPORT_WITH_DES40_CBC_SHA","TLS_RSA_EXPORT_WITH_RC4_40_MD5","TLS_RSA_WITH_DES_CBC_SHA","TLS_ECDHE_ECDSA_WITH_NULL_SHA","TLS_ECDHE_RSA_WITH_NULL_SHA","TLS_RSA_WITH_NULL_SHA","TLS_RSA_WITH_NULL_MD5"]
              obj[key] = random.choice(cipher)
          
          # emails
            elif obj[key] == "emails":
              domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]
              username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
              domain = random.choice(domains)
              obj[key] = f"{username}@{domain}"

          # tls
            elif obj[key] == "tls":
              tls = ["TLSv1.2", "TLSv1.3", "TLSv1.1", "SSLv1", "SSLv2", "SSLv3"]
              obj[key] = random.choice(tls)
              
          # Randomize the date
            elif obj[key] == "date":
              date = datetime.utcnow() - timedelta(seconds=random.randint(1, 10000))
              # Increment the date by a random number of seconds (between 5 and 10)
              date += timedelta(seconds=random.randint(5, 10))
              # Format the date as a string in the desired format
              obj[key] = date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

          # mitre_tactic
            elif obj[key] == "mitre_tactic": 
              mitre_tactic = ["Initial Access","Execution","Persistence","Privilege Escalation","Defense Evasion","Credential Access","Discovery","Lateral Movement","Collection","Exfiltration","Command and Control"]
              obj[key] = random.choice(mitre_tactic)
            
          #mitre_technique
            elif obj[key] == "mitre_technique": 
              mitre_technique = ["T1548","T1548.002","T1548.004","T1548.001","T1548.003","T1134","T1134.002","T1134.003","T1134.004","T1134.005","T1134.001","T1531","T1087","T1087.004","T1087.002","T1087.003","T1087.001","T1098","T1098.001","T1098.003","T1098.002","T1098.005","T1098.004","T1583","T1583.005","T1583.002","T1583.001","T1583.004","T1583.007","T1583.003","T1583.006","T1595","T1595.001","T1595.002","T1595.003","T1557","T1557.002","T1557.003","T1557.001","T1071","T1071.004","T1071.002","T1071.003","T1071.001","T1010","T1560","T1560.003","T1560.002","T1560.001","T1123","T1119","T1020","T1020.001","T1197","T1547","T1547.014","T1547.002","T1547.006","T1547.008","T1547.015","T1547.010","T1547.012","T1547.007","T1547.001","T1547.005","T1547.009","T1547.003","T1547.004","T1547.013","T1037","T1037.002","T1037.001","T1037.003","T1037.004","T1037.005","T1217","T1176","T1185","T1110","T1110.004","T1110.002","T1110.001","T1110.003","T1612","T1115","T1580","T1538","T1526","T1619","T1059","T1059.002","T1059.007","T1059.008","T1059.001","T1059.006","T1059.004","T1059.005","T1059.003","T1092","T1586","T1586.003","T1586.002","T1586.001","T1554","T1584","T1584.005","T1584.002","T1584.001","T1584.004","T1584.007","T1584.003","T1584.006","T1609","T1613","T1136","T1136.003","T1136.002","T1136.001","T1543","T1543.001","T1543.004","T1543.002","T1543.003","T1555","T1555.003","T1555.001","T1555.005","T1555.002","T1555.004","T1485","T1132","T1132.002","T1132.001","T1486","T1565","T1565.003","T1565.001","T1565.002","T1001","T1001.001","T1001.003","T1001.002","T1074","T1074.001","T1074.002","T1030","T1530","T1602","T1602.002","T1602.001","T1213","T1213.003","T1213.001","T1213.002","T1005","T1039","T1025","T1622","T1491","T1491.002","T1491.001","T1140","T1610","T1587","T1587.002","T1587.003","T1587.004","T1587.001","T1006","T1561","T1561.001","T1561.002","T1484","T1484.002","T1484.001","T1482","T1189","T1568","T1568.003","T1568.002","T1568.001","T1114","T1114.003","T1114.001","T1114.002","T1573","T1573.002","T1573.001","T1499","T1499.003","T1499.004","T1499.001","T1499.002","T1611","T1585","T1585.003","T1585.002","T1585.001","T1546","T1546.008","T1546.009","T1546.010","T1546.011","T1546.001","T1546.015","T1546.014","T1546.012","T1546.016","T1546.006","T1546.007","T1546.013","T1546.002","T1546.005","T1546.004","T1546.003","T1480","T1480.001","T1048","T1048.002","T1048.001","T1048.003","T1041","T1011","T1011.001","T1052","T1052.001","T1567","T1567.002","T1567.001","T1190","T1203","T1212","T1211","T1068","T1210","T1133","T1008","T1083","T1222","T1222.002","T1222.001","T1495","T1187","T1606","T1606.002","T1606.001","T1592","T1592.004","T1592.003","T1592.001","T1592.002","T1589","T1589.001","T1589.002","T1589.003","T1590","T1590.002","T1590.001","T1590.005","T1590.006","T1590.004","T1590.003","T1591","T1591.002","T1591.001","T1591.003","T1591.004","T1615","T1200","T1564","T1564.008","T1564.005","T1564.001","T1564.002","T1564.003","T1564.004","T1564.010","T1564.009","T1564.006","T1564.007","T1574","T1574.012","T1574.001","T1574.002","T1574.004","T1574.006","T1574.005","T1574.013","T1574.007","T1574.008","T1574.009","T1574.010","T1574.011","T1562","T1562.008","T1562.002","T1562.007","T1562.004","T1562.001","T1562.010","T1562.003","T1562.006","T1562.009","T1525","T1070","T1070.003","T1070.002","T1070.008","T1070.007","T1070.009","T1070.001","T1070.004","T1070.005","T1070.006","T1202","T1105","T1490","T1056","T1056.004","T1056.002","T1056.001","T1056.003","T1559","T1559.001","T1559.002","T1559.003","T1534","T1570","T1036","T1036.007","T1036.001","T1036.004","T1036.005","T1036.003","T1036.002","T1036.006","T1556","T1556.001","T1556.007","T1556.006","T1556.004","T1556.002","T1556.003","T1556.005","T1578","T1578.002","T1578.001","T1578.003","T1578.004","T1112","T1601","T1601.002","T1601.001","T1111","T1621","T1104","T1106","T1599","T1599.001","T1498","T1498.001","T1498.002","T1046","T1135","T1040","T1095","T1571","T1003","T1003.008","T1003.005","T1003.006","T1003.004","T1003.001","T1003.003","T1003.007","T1003.002","T1027","T1027.001","T1027.004","T1027.007","T1027.009","T1027.006","T1027.005","T1027.002","T1027.003","T1027.008","T1588","T1588.003","T1588.004","T1588.005","T1588.001","T1588.002","T1588.006","T1137","T1137.006","T1137.001","T1137.002","T1137.003","T1137.004","T1137.005","T1201","T1120","T1069","T1069.003","T1069.002","T1069.001","T1566","T1598","T1598.002","T1598.003","T1598.001","T1566.001","T1566.002","T1566.003","T1647","T1542","T1542.003","T1542.002","T1542.004","T1542.001","T1542.005","T1057","T1055","T1055.004","T1055.001","T1055.011","T1055.015","T1055.002","T1055.009","T1055.013","T1055.012","T1055.008","T1055.003","T1055.005","T1055.014","T1572","T1090","T1090.004","T1090.002","T1090.001","T1090.003","T1012","T1620","T1219","T1563","T1563.002","T1563.001","T1021","T1021.003","T1021.001","T1021.002","T1021.004","T1021.005","T1021.006","T1018","T1091","T1496","T1207","T1014","T1053","T1053.002","T1053.007","T1053.003","T1053.005","T1053.006","T1029","T1113","T1597","T1597.002","T1597.001","T1596","T1596.004","T1596.001","T1596.003","T1596.005","T1596.002","T1593","T1593.003","T1593.002","T1593.001","T1594","T1505","T1505.004","T1505.001","T1505.005","T1505.002","T1505.003","T1648","T1489","T1129","T1072","T1518","T1518.001","T1608","T1608.004","T1608.003","T1608.005","T1608.006","T1608.001","T1608.002","T1528","T1539","T1649","T1558","T1558.004","T1558.001","T1558.003","T1558.002","T1553","T1553.002","T1553.006","T1553.001","T1553.004","T1553.005","T1553.003","T1195","T1195.003","T1195.001","T1195.002","T1218","T1218.003","T1218.001","T1218.002","T1218.004","T1218.014","T1218.013","T1218.005","T1218.007","T1218.008","T1218.009","T1218.010","T1218.011","T1218.012","T1082","T1614","T1614.001","T1016","T1016.001","T1049","T1033","T1216","T1216.001","T1007","T1569","T1569.001","T1569.002","T1529","T1124","T1080","T1221","T1205","T1205.001","T1205.002","T1537","T1127","T1127.001","T1199","T1552","T1552.003","T1552.005","T1552.007","T1552.001","T1552.002","T1552.006","T1552.004","T1535","T1550","T1550.001","T1550.002","T1550.003","T1550.004","T1204","T1204.002","T1204.003","T1204.001","T1078","T1078.004","T1078.001","T1078.002","T1078.003","T1125","T1497","T1497.001","T1497.003","T1497.002","T1600","T1600.002","T1600.001","T1102","T1102.002","T1102.001","T1102.003","T1047","T1220"]
              obj[key] = random.choice(mitre_technique)

          # classifications
            elif obj[key] == "classifications": 
              classifications = ["Malware", "Phishing","Spam","PUA"]
              obj[key] = random.choice(classifications)
          
          # uuid
            elif obj[key] == "uuid": 
              obj[key] = str(uuid.uuid4())
          
          # url 
            elif obj[key] == "url": 
              length = 13
              random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
              # Return the random string as a URL by adding a prefix and suffix
              obj[key] = "https://www.{}.com".format(random_string)
          
          # user_agent
            elif obj[key] == "user_agent":
              user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36","Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"]
              obj[key] = random.choice(user_agents)
          # action 
            elif obj[key] == "action":
              actions = ["blocked","allow","alert"]
              obj[key] = random.choice(actions)

          # message type
            elif obj[key] == "message_type": 
              message_type = ["blocked_click", "allowed_click"]
              obj[key] = random.choice(message_type)

          # randomizing INTs
            elif isinstance(obj[key], int): 
              obj[key] = random.randint(0,10000000)
          
          # randomizing booleans
            elif isinstance(obj[key], bool): 
              obj[key] = random.choice(["True", "False"])

          # randomizing string values BUT checks to see if the user has deemed the field static by placing ' keep | ' in front of the value you they want to save.
            elif isinstance(obj[key], str):
              pattern = r"keep\|(.*?)$"
              match = re.search(pattern, obj[key])
              min_length = 4
              max_length = 25
              if match: 
                obj[key] = match.group(1)
              else:
                obj[key] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(min_length, max_length)))
        
            elif isinstance(obj[key], list):
              for item in obj[key]: 
                randomize(item)
                        
            elif isinstance(obj[key], dict):
            # If the key's value is a dictionary, recursively call the function
              randomize(obj[key])
          return(obj)
      # Call the randomize function to generate random values for the keys
        fake_logs = randomize(data)
    


        def send_json_to_https_endpoint(fake_logs, endpoint_url, headers):
          response = requests.post(endpoint_url, json=fake_logs, headers=headers)
          if response.status_code != 200:
            raise ValueError(f'Failed to send json to endpoint. Status code: {response.status_code}')
        send_json_to_https_endpoint(fake_logs, endpoint_url, headers)

  data_validation(filename)
  print('\n')
  randomize_json(filename, num_times)

  print('\n' + 'Thank you for using my seeder script! Any updates or features you would like to see added, please create a github issue!' + '\n' + '\n' + 'We processed ' + str(num_times) + ' logs this run.' +'\n' +'\n'  'Thank you! - Po')
  



if __name__ == "__main__":
  main()
  