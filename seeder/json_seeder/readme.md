# JSON Log Seeder

## STOP!!! If you are looking to create fake log data for other log formats (CEF, SYSLOG, etc), please see this [section](/seeder/readme.md). This script is meant to handle only json file as a template.  
  
  
## Supported Log Sources (will continue to add)
| Log Source | Notes |
| :-------------: | :-------------: |
| [Crowdstrike](/seeder/json_seeder/data_sources/edr/crowdstrike/cs-example.json) | DetectionSummaryEvent
| [Mimecast](/seeder/json_seeder/data_sources/email_gateway/mimecast.json) | MTA 
| [ProofPoint](/seeder/json_seeder/data_sources/email_gateway/proofpoint.json) | Clicked Block Event

## How to use ##


## 1. Open your example log, and replace the 'string' values with a [supported string type](#supported-string-types). If there are any ints or booleans, the script will handle that for you.
-  A full list of examples can be seen [here](/seeder/json_seeder/data_sources/). I used [Crowdstrike](/seeder/json_seeder/data_sources/edr/crowdstrike/cs-example.json) and [Mimecast](/seeder/json_seeder/data_sources/email_gateway/mimecast.json) for my testing and have linked them directly for ease of use. 
- In the CS log, you can see there is a string for username. You will replace that string value with "user", because the script will read the "user" value and generate a random username. You will need to do this for all of the fields you want to randomize, again please check [supported string type](#supported-string-types). If you don't see one, please create a github issue and I will get to it when I can. 
- **Please note**, if you would like to KEEP the original value for a key, please just pre-append the value with ' ```keep |```. In the example CS log, ```keep|DetectionSummaryEvent```(also highlighted in the first screenshot below) will keep the origianl value of "DetectionSummaryEvent". If you want my script to replace that string then just leave it alone :). 

### Example CS Log:
![alt text](/seeder/json_seeder/screenshots/example-cs.png)

## 2. After you have updated the example file with your randomized fields, feed the file into the python script.

![alt text](/seeder/json_seeder/screenshots/cli.png)

## 3. After the script takes your updated json file it will prompt you for how many logs you would like to create, followed by a destination HTTPS Webhook and a source category. By default, this was made to support [Sumo Logic's HTTPS Endpoint](https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/logs-metrics/#configure-an-httplogs-and-metrics-source), which is why it forces a sourceCategory. If you are using this for another purpose, be sure to update the headers variable found in the main file [here](/seeder/json_seeder/json_seeder.py).

![alt text](/seeder/json_seeder/screenshots/full_cli.png)

*Please note that I have intentially covered the rest of the URL endpoint*. 


## 4. Check your webhook destination! In Sumo we can easily test this with our nice [live tail](https://help.sumologic.com/docs/search/live-tail/about-live-tail/) feature (basically a ```tail -f``` on a hosted collection endpoint)

![alt text](/seeder/json_seeder/screenshots/live_tail.png)


## Supported String Types
| Strings | Example | Notes |
| :-------------: | :-------------: | :-------------: |
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
net_dir | { json_key : "net_dir" }
cipher | { json_key : "cipher" }
emails | { json_key : "emails" }
tls | { json_key : "tls" }
date | { json_key : "date" } | Please note that you can specify a pattern if you like by leveraging [faker](https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html). To change the pattern, please go to line 117 in [v3.py](/loggen/v2/v3.py).  Ex. faker.date(pattern="%Y-%m-%d") <- This will generate a fake date in the format "YYYY-MM-DD". Please refer to their documentation if you need a specific format
mitre_tactic | { json_key : "mitre_tactic" } |
mitre_technique | { json_key : "mitre_technique" } | 
classifications | { json_key : "classifications" } | Malware, Phishing, Spam, PUA, ETC
uuid | { json_key : "uuid" } | This will generate something like '8c6cfedd-3050-4d65-8c09-c5f65c38da81'
url | { json_key : "url" } |
user_agent | { json_key : "user_agent" } | 
action |  { json_key : "action" } | allow, blocked, alert
message_type |  { json_key : "message_type" } | blocked_click, allowed_click