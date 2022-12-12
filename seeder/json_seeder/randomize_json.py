from randomizer import randomize
import json
def randomize_json(filename, num_times):
      for i in range(num_times):
        # Load the JSON file
        with open(filename, "r") as f:
          data = json.load(f)
          randomize(data)
        return randomize(data)


        