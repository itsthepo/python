# This will step through an example of a configuration file for log-generator

1. Creating a data source is relatively simple!
    ``` 
    code loggen/data_sources/firewall/dns/dns.yaml
    ```
*Here is an example of a dns one I threw together*
![alt text](/loggen/screenshots/dns.png)


2. The configuration file is written in yaml but is very straight forward

```yaml
# Name of the logs being generated (for logging purposes only)
name: DNS

# The path to the file where to write the logs to
file: /Users/brborodach/projects/python/loggen/example_logs/dns/dns.txt

# The format of the log
format: "{date} ns1 named[{pid}]: client {ipaddress}#{port}: query: {query} IN {dns_type}"

# Time frame of how frequently to output logs
frequency:
  seconds: 5

# Time frame of the offset, from now, the timestamps should be - optional 
offset:
  seconds: 0

# Time frame of the jitter the timestamps should be. - optional
jitter:
  seconds: 2

# Number of logs to create per tick
amount: 50

# A dictionary of fields to be substituted into the log format - See format stanza.  

# Each property of fields should be one of the following types:

        #type: One of the following: enum, timestamp, integer, float, chance, ip

        #repeat: (optional) Number of times to repeat the current value before generating (default 1)
        
        #change: (optional) Float probability [0..1] that the current value will change (default 1)
        
        # value: (optional) The initial value for the field

fields:
  date:
  # Here there is a neat trick for timestamps 
    type: timestamp
    format: "%d/%b/%Y:%H:%M:%S"
  ipaddress:
    type: ip
  pid:
    type: integer
    min: 0 
    max: 100000
  port:
    type: integer 
    min: 0 
    max: 65535
  # this is the only "manual" data creation if you need random fields but pretty easy to google a list of random domains in a csv format.
  query:
    type: enum
    values: [www.cionfs.com ,www.forumpro.com ,www.sosorank.com ,www.teamtop.com ,www.redcoon.com ,www.alberta.com ,www.postupim.com ,www.evplayer.com ,www.cbsnews.com ,www.mihindia.com ,www.rotikaya.com ,www.grabcad.com ,www.memoclic.com ,www.rutube.com ,www.kulina.com ,www.icscards.com ,www.pandion.com ,www.ihuanju.com ,www.incont.com ,www.htpmedia.com ,www.devryu.com ,www.gigantti.com ,www.nehumath.com ,www.rhostbh.com ,www.artinfo.com ,www.survstat.com ,www.triberr.com ,www.soukai.com ,www.ankawa.com ,www.lifeweek.com ,www.imbolt.com ,www.tisiwi.com ,www.itmedia.com ,www.midomi.com ,www.cehome.com ,www.artinfo.com ,www.duoyoo.com ,www.ikoula.com ,www.ihuanju.com ,www.onofre.com ,www.gendai.com ,www.caltrain.com ,www.gosloto.com ,www.gamebean.com ,www.clinique.com ,www.hackbase.com ,www.midomi.com ,www.ongame.com ,www.suntimes.com ,www.klintsy.com ,www.lipsum.com ,www.tlavideo.com ,www.cuasar.com ,www.fsaten.com ,www.noticias.com ,www.mombaby.com ,www.chaoji.com ,www.abreeder.com ,www.incont.com ,www.ioncube.com ,www.gamevui.com ,www.milenio.com ,www.gynetube.com ,www.lansik.com ,www.kabbalah.com ,www.sunland.com ,www.kimsufi.com ,www.myhack.com ,www.garnek.com ,www.sosorank.com ,www.wetmummy.com ,www.kunyue.com ,www.camsympa.com ,www.asspoint.com ,www.sprint.com ,www.akinator.com ,www.prophpbb.com ,www.smatch.com ,www.survstat.com ,www.fmworld.com ,www.gamefly.com ,www.nowloss.com ,www.politika.com ,www.hillnews.com ,www.najmsat.com ,www.menlook.com ,www.arikair.com ,www.soukai.com ,www.ruclicks.com ,www.okcupid.com ,www.asspoint.com ,www.chaddo.com ,www.mactrast.com ,www.kirula.com ,www.lefora.com ,www.smarter.com ,www.melablog.com ,www.downbank.com ,www.drumtv.com ,www.distimo.com ,www.sonnik.com ,www.tolmol.com ,www.bonton.com ,www.tamilcnn.com ,www.esdlife.com ,www.erowid.com ,www.newone.com ,www.numbeo.com ,www.eurobank.com ,www.chmail.com ,www.snapsort.com ,www.newswire.com ,www.sosorank.com ,www.chintai.com ,www.sunland.com ,www.dnsstuff.com ,www.moshimo.com ,www.carbuyer.com ,www.cupidplc.com ,www.gongkong.com ,www.steelers.com ,www.megalife.com ,www.appone.com ,www.golfnow.com ,www.ljworld.com]
  dns_type:
    type: enum
    values: [A, NS, MD, MF, CNAME, SOA, MB, MG, MR, NULL, WKS, PTR, HINFO, MINFO, MX, TXT, AXFR, MAILB, MAILA, ANY]
```

3. Hit save and you can now use your new configuration file :). If this is a data source that I don't have or a new file format/update please submit a PR and I will update!

*Reminder if you need inspiraton you can leverage the [examples](/loggen/data_sources/) I have already created!*