# This script was meant to facilitate easy log ingestion for SIEM vendors leveraging an opensource plugin 'Loggen. 

This is meant to be a quick and easy way to send data to your POV instances or demo environments. If you would like to contribute to the log sources, submit a pull request! The SE community will thank you :pray: 

| Log Source Folders | Version | 
| :-------------: |:-------------:|
| [Palo Alto](/loggen/log_source_config/palo)     | v10
| [Crowdstrike](/loggen/log_source_config/crowdstrike)     | centered     
| TBD |       


# How to use

We will be leveraging a wonderful module called [log-generator](https://pypi.org/project/log-generator/)! To use simply install via pip!

1. Install [pip](https://pip.pypa.io/en/stable/installation/)

2. Run the command below:

```
pip3 install log-generator
# most likely pip3 now adays right!
```
3. Clone this [repo](https://github.com/itsthepo/python.git)
```
git clone https://github.com/itsthepo/python.git
```
4. Change Directory to the log source config files
```
cd loggen/log_source_config
```
5. Customize the config to meet your needs (i.e., # of logs, output file location, etc. See here for more [details]((https://pypi.org/project/log-generator/)))
```
vi palo_traffic.yaml
```

6. Run log-generator on the source file
```
log-generator log_source_config/log_source_config/palo/palo_traffic.yaml
```

7. Getting the data into your SIEM - Coming soon on docs!