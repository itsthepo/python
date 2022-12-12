import sys, os
def data_validation(filename):
        ALLOWED_EXTENSTIONS = {".json"}
        extension = None
        while extension not in ALLOWED_EXTENSTIONS:
            if filename == sys.argv[0]:
                print("Please provide a valid json file with the script. Ex: 'python3 test.py data.json' ")
                return False
            elif filename == sys.argv[-1]:
                extension = os.path.splitext(filename)[1]
                return filename
        return filename