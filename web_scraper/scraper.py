import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(soup):
    citation_needed=soup.find_all('a', {'title': 'Wikipedia:Citation needed'})
    return len(citation_needed)


def get_citations_needed_report(soup):
    paragraphs=soup.find_all('p')

    all_paragraphs=[]
    for paragraph in paragraphs:
        paragraph_citation_needed = paragraph.find('a',{'title':'Wikipedia:Citation needed'})
        if paragraph_citation_needed :
            all_paragraphs.append(paragraph.text)
    return all_paragraphs
