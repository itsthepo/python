from pprint import pprint
import sys, os, json, time

def main(): 
    
    filename = sys.argv[-1]


    def data_validation(filename):
        ALLOWED_EXTENSTIONS = {".json"}
        extension = None
        while extension not in ALLOWED_EXTENSTIONS:
            if filename == sys.argv[0]:
                print("Please provide a valid json file with the script. Ex: 'python3 test.py data.json' ")
                return False
            elif filename == sys.argv[-1]:
                extension = os.path.splitext(filename)[1]
                print("We will process this " + filename + " file now")
                return filename
        return filename
    print(filename)

    def delprint(text,delay_time):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(delay_time)

    def parser(filename):
            with open(sys.argv[1], 'r') as f:
                data = json.load(f)
            
            print('\n')
            
            for x in enumerate(data): 
                pprint(x)

            removed_data = int(input("Please select an index from the output below:  "))

            with open("newfile.json","w") as write_file:
                json.dump(data[removed_data], write_file)

            # new line to make it easier on the eyes
            print('\n')

            delprint("I will remove the object '" + str(removed_data) + "' from the list",.01)

            # new line to make it easier on the eyes

            print('\n')

            # sleep to give the user time to keyboard interrupt if they change their mind. 
            time.sleep(2)

            start_time = time.time()
            del data[removed_data]
            print("It took me %s seconds to delete that data. I am pretty cool" % (time.time() - start_time))

            # new line to make it easier on the eyes
            print('\n')

            delprint("I have removed '" + str(removed_data) + "' from the list", 0.01)

            with open(sys.argv[1],"w") as write_file2: 
                json.dump(data, write_file2)
            exit()

    data_validation(filename)

    parser(filename)


if __name__ == "__main__":
    main()