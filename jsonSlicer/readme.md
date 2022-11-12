# Welcome to one of my first [scripts](/jsonParser/slicer.py), 'Slicer' :knife: ! 

Slicer was created to load a large json file and then remove (slice) certain JSON Objects from the file for further investgiation or to slice the file into smaller chunks for consumption. Please see an example use case below:

## Ex. Use case

### We were looking to ingest [qualys inventory data](https://www.qualys.com/docs/qualys-asset-management-tagging-api-v2-user-guide.pdf) and the json blob that came back on a particular asset was 355kb which for most SIEMs is bigger than they can handle for a single log event (most are capped at like <64kb). This JSON parser, slices out whatever object you want/need to trim the file and then writes it to another for safe keeping or reconstruction later.  




#  **I will be making updates to this in the future**

*I have left my [old version](/jsonParser/v1/json_slicer.py) of the parser to see how much I have grown :grin:*
