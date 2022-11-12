# This python [script](/jsonParser/slicer.py) 'Slicer' :knife: was created to load a json file and then remove certain dictionary's (JSON Objects) from the object and then re-write the original file. 

## Ex. Use case

### We were looking to ingest qualys inventory data and the json blob that came back on a particular asset was 355kb which for most SIEMs is bigger than they can handle for a single event (most are capped at like <64kb). This JSON parser, strips out whatever object you want/need to trim the file and then writes it to another for safe keeping or reconstruction later. 

*I have left my [old version](/jsonParser/v1/json_slicer.py) of the parser to see how much I have grown :grin:*