import requests
import re
import math
import os
import time

URL_START='http://www.gumtree.com.au'
OFFER_CHOICE=['k0?ad=offering','k0?ad=wanted']
ARTIST_URL=re.sub("\s",+,artist)

pageURL='{0}/s-{1}+{2}/{3}'.format(URL_START,ARTIST_URL,city,OFFER_CHOICE)
results=requests.get(pageURL)
resultsfile.write(results.text)



#http://www.gumtree.com.au/s-arctic+monkeys+sydney/k0?ad=offering