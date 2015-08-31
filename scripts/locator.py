from lxml import html
import requests
import sys
import time

def printit(txt):
    print txt.strip()
    sys.stdout.flush()

def functionname( parameters ):
 #url = 'http://webcache.googleusercontent.com/search?q=cache:http://radio-locator.com/info/'+parameters+'-AM'
 url = 'http://radio-locator.com/cgi-bin/finder?sr=Y&s=C&call='+parameters
 printit(url)
 page = requests.get(url)
 tree = html.fromstring(page.text)
 texts = tree.xpath('///text()')
 for i in range(len(texts)):
     if texts[i].endswith('m3u') or texts[i].endswith('pls') or (texts[i].find('You have exceeded your allotted usage of Radio-Locator for the day') != -1) or (texts[i].find('inappropriate use') != -1):
         printit(texts[i])


with open(sys.argv[1]) as f:
 content = f.readlines()

for i in range(len(content)):
    line = content[i]
    if (line.startswith('http')):
        split = line.split()
        if (len(split) > 1):
            #print split[1]
            functionname(split[1])
            time.sleep(2)
    else: printit(line)

