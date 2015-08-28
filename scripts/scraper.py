from lxml import html
import requests
import sys
page = requests.get(sys.argv[1])
tree = html.fromstring(page.text)
hrefs = tree.xpath('//a[@href]/attribute::href')
texts = tree.xpath('//a[@href]/text()')
for i in range(len(hrefs)):
 print hrefs[i], texts[i]
