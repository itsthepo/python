import json

with open('qualys_asset.json', 'r') as f:
  data = json.load(f)

with open("openPortListData.json","w") as write_file: 
    json.dump(data["openPortListData"], write_file)

for s in data.copy():
	remove_key = data.pop("openPortListData", None)

with open("qualys_asset.json","w") as write_file2: 
    json.dump(data, write_file2)


