import requests 
def send_json_to_https_endpoint(fake_logs, endpoint_url, num_times):
    for i in range(num_times):
          response = requests.post(endpoint_url, json=fake_logs)
          if response.status_code != 200:
            raise ValueError(f'Failed to send json to endpoint. Status code: {response.status_code}')

      