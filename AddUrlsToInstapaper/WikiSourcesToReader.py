#!/usr/bin/python
import sys,os,re
from BeautifulSoup import * 
from sets import Set
from urllib import *
#makes use of http://www.instapaper.com/api

INSTAPAPER_ADD='https://www.instapaper.com/api/add'
def valid_link(link):
	return ('http' in link) and not 'wikipedia.org' in link
	
if __name__ == '__main__':
	wikipedia_page=BeautifulSoup(open(sys.argv[1]).read())
	instapaper_params={}
	instapaper_params['username']=sys.argv[2]
	instapaper_params['password']=sys.argv[3]
	all_links=Set()
	for link in wikipedia_page.findAll('a'):
		try:
			link=link['href']
			if valid_link(link):
				all_links.add(link)
		except:
			continue
	#adding all these to instapaper
	for link in all_links:
		instapaper_params['url']=link
		api_params=urlencode(instapaper_params)
		res=urlopen(INSTAPAPER_ADD+'?%s' % api_params)
		if res.read()==201:
			print 'added ',link,' to instapaper'