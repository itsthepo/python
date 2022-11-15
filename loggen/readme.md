# This script was meant to facilitate easy log ingestion for SIEM vendors leveraging an opensource python module '[log-generator](https://pypi.org/project/log-generator/)'. *At this time, it does NOT support json formatted logs. I am working on a few workarounds!* 

This is meant to be a quick and easy way to send data to your POV instances or demo environments. If you would like to contribute to the log sources, submit a pull request! The SE community will thank you :pray: 

| Log Source Function | Vendors | 
| :-------------: |:-------------:|
| [Firewalls](/loggen/data_sources/firewall/)     | [Palo](/loggen/data_sources/firewall/palo/palo_traffic.yaml), [FortiNet - WIP](/loggen/data_sources/firewall/fortinet/fortinet.yaml)
| [EDR](/loggen/data_sources/edr/)     | [Crowdstrike](/loggen/data_sources/edr/crowdstrike/cs.yaml), [Sentinel One - WIP](/loggen/data_sources/edr/sentinelone/sentinelone.yaml)
| [DNS](/loggen/data_sources/dns/) | [Bind DNS](/loggen/data_sources/dns/dns.yaml)
| [Web](/loggen/data_sources/web/) | [Apache](/loggen/data_sources/web/apache/apache2_4.yaml), [Nginx - WIP](/loggen/data_sources/web/nginx/nginx.yaml)        


# How to use

We will be leveraging a wonderful module called [log-generator](https://pypi.org/project/log-generator/)! To use simply install via pip!

1. Install [pip](https://pip.pypa.io/en/stable/installation/)

2. Run the command below:

```
pip3 install log-generator
# most likely pip3 now a days right!
```
3. Clone this [repo](https://github.com/itsthepo/python.git)
```
git clone https://github.com/itsthepo/python.git
```
4. Change Directory to the log source function folders
```
cd loggen/data_sources
```
5. See what data sources are available
``` 
ls 
```
6. Select a log function/data source. In this example, I chose Palo Alto TRAFFIC logs.
``` 
cd firewall/palo
```

7. Customize the config to meet your needs (i.e., # of logs, output file location, etc. See here for more from the [creater for log-generator](https://pypi.org/project/log-generator/) or please see the [readme](/loggen/data_sources/readme.md) from data_sources folder
```
vi palo_traffic.yaml
```

6. Run log-generator on the source file

*Example below is from Palo but can customized by putting in a different *
```
log-generator palo_traffic.yaml
```

7. Getting the data into your SIEM - Coming soon on docs!