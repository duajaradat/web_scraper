import requests
from bs4 import BeautifulSoup
# link to get data from
url='https://en.wikipedia.org/wiki/History_of_Mexico' 

# send a request using requests tool 
response = requests.get(url)
# parse the html response 
soup = BeautifulSoup(response.content,'html.parser')

# print(response)
# print(soup)



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
