This python [script](/jsonParser/json_parser.py) was created to load a json file and then remove certain dictionary's (JSON Objects) from the object and then re-write the original file. 


Ex. Use case

We were looking to ingest qualys inventory data and the json blob that came back on a particular asset was 355kb which for most SIEMs is bigger than they can handle for a single event (most are capped at like <64kb)