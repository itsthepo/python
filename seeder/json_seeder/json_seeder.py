from randomize_json import randomize_json
from webhook import send_json_to_https_endpoint
from data_validate import data_validation 
from animation import loading_animation 
import time, sys

print("Please enter the number of logs you would like created")
num_times = int(input())
endpoint_url = input('Please enter a URL: ')
source_category=input('Please provide a sourceCategory (ex. dev/endpoint/cs): ')
filename = sys.argv[-1]
headers = {"X-Sumo-Category": source_category}


time.sleep(2)

def main(): 

  loading_animation()
  data_validation(filename)
  fake_logs = randomize_json(filename, num_times)
  send_json_to_https_endpoint(fake_logs,endpoint_url, num_times, headers)

  print("Complete")
  print('\n' + 'Thank you for using my seeder script! Any updates or features you would like to see added, please create a github issue!' + '\n' + '\n' + 'We processed ' + str(num_times) + ' logs this run.' +'\n' +'\n'  'Thank you! - Po')
  
if __name__ == "__main__":
  main()
  