import json

# Load the JSON file
with open('C:\\Users\\Wolfy\\projects\\python\\loggen\\data_sources\\email_gateway\\mimecast.json') as f:
    data = json.load(f)

# Replace the values in the nested dictionary
for key, value in data.items():
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                for k, v in item.items():
                    # Replace the value with a new value
                    print(k,v)

