# This script was meant to facilitate easy log ingestion for SIEM vendors leveraging an opensource python module '[log-generator](https://pypi.org/project/log-generator/)'. If you have JSON logs that you would like to randomize, please see the [json_seeder](/seeder/json_seeder/)

This is meant to be a quick and easy way to send data to your POV instances or demo environments. If you would like to contribute to the log sources, submit a pull request! The SE community will thank you :pray: 

| Log Source Function | Vendors | 
| :-------------: |:-------------:|
| [Firewalls](/seeder/data_sources/firewall/)     | [Palo](/seeder/data_sources/firewall/palo/palo_traffic.yaml), [FortiNet - WIP](/seeder/data_sources/firewall/fortinet/fortinet.yaml)
| [EDR](/seeder/data_sources/edr/)     | [Crowdstrike - WIP](/seeder/data_sources/edr/crowdstrike/cs.yaml), [Sentinel One - WIP](/seeder/data_sources/edr/sentinelone/sentinelone.yaml)
| [DNS](/seeder/data_sources/dns/) | [Bind DNS](/seeder/data_sources/dns/bind/dns.yaml), [Umbrella](/seeder/data_sources/dns/umbrella/)
| [Web Server](/seeder/data_sources/web_server/) | [Apache](/seeder/data_sources/web_server/apache/apache2_4.yaml), [Nginx - WIP](/seeder/data_sources/web_server/nginx/nginx.yaml)
| [Proxies](/seeder/data_sources/proxy/)         | [Umbrella](/seeder/data_sources/proxy/umbrella/umbrella-proxy.yaml)


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
cd seeder/data_sources
```
5. See what data sources are available
``` 
ls 
```
6. Select a log function/data source. In this example, I chose Palo Alto TRAFFIC logs.
``` 
cd firewall/palo
```

7. Customize the config to meet your needs (i.e., # of logs, output file location, etc. See here for more from the [creater for log-generator](https://pypi.org/project/log-generator/) or please see the [readme](/seeder/data_sources/readme.md) from data_sources folder
```
vi palo_traffic.yaml
```

6. Run log-generator on the source file

*Example below is from Palo but can customized by putting in a different *
```
log-generator palo_traffic.yaml
```

7. Getting the data into your SIEM - Coming soon on docs!