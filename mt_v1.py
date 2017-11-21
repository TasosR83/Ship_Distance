# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib
import urllib2
import re
from geopy.distance import vincenty #pip install geopy


def get_Marine_traffic_coords(page):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib2.Request(page, headers=hdr)
    aResp = urllib2.urlopen(req);
    web_pg = aResp.read();
    # print web_pg
    pattern = 'class="details_data_link">*&deg; / *&deg;</a></strong></span>'
    pattern = 'class="details_data_link">(.*)&deg; / (.*)&deg;</a></strong></span>'
    m = re.search(pattern, web_pg)
    '''print m.group(0)
    if m:
      print "LOC0:", m.group(0)
      print "LOC1:", m.group(1)
      print "LOC2:", m.group(2)
    '''
    lat = m.group(1)
    lon  = m.group(2)
    return (float(lat),float(lon))

# DEFINE THE SHIP I NEED + MY LOCATION !!!
page="http://www.marinetraffic.com/en/ais/details/ships/shipid:214349/mmsi:241053000/vessel:PELAGITIS";
coords1 = get_Marine_traffic_coords(page);

print coords1

coords2 = (39.106,26.558); # DESTINATION
print(vincenty(coords1, coords2).kilometers)