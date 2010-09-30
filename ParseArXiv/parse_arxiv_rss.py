#!/usr/bin/env python
import sys,re
from BeautifulSoup import *
from urllib import *
import datetime

class Sections(object):
    def __init__(self,section_names):
        self.section_names=section_names
        self.sections={}
    def add_section(self,arxiv):
        self.sections[arxiv.section]=arxiv

class Arxiv(object):
    def __init__(self,sect,date):
        self.section=sect
        self.from_date=date
        self.papers={}
        
    def add_paper(self,paper):
        paper_link_re=re.compile('(.*)/(.*)')
        paper_num=paper_link_re.match(paper.link).group(2)
        self.papers[paper_num]=paper

class Paper(object):
    def __init__(self,link,title,desc):
        self.link=link
        self.title=title
        self.description=desc

def main():
    BASE_URL='http://export.arxiv.org/rss/'
    if len(sys.argv) < 2:
        print """Usage: ./parse_arxiv_rss.py <section> <section> ...
        example: ./parse_arxiv_rss.py astro-ph gr-qc """
    sections=Sections(sys.argv[1:])
    for sect in sections.section_names:
        arxiv=Arxiv(sect,datetime.datetime.now())
        papers=BeautifulStoneSoup(urlopen(u'%s/%s' % (BASE_URL,sect)).read())
        for pap in papers.findAll(u'item'):
            pap=Paper(pap.link.contents[0],
                pap.title.contents[0],
                pap.description.contents[0])
            arxiv.add_paper(pap)
        sections.add_section(arxiv)
    for sect,arx in sections.sections.items():
        # do what you'd like here with the items we've obtained
        print sect,arx.papers.keys()

if __name__ == '__main__':
    main()
