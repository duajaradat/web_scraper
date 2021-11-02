import requests
from bs4 import BeautifulSoup
# link to get data from
url='https://en.wikipedia.org/wiki/History_of_Mexico' 



# print(response)
# print(soup)



def get_citations_needed_count(url):
    """ 
    This function search for all the links have title (Wikipedia:Citation needed) to count them
    Arguments : url
    Returns : number of links have title name (Wikipedia:Citation needed)
    """

    # send a request using requests tool 
    response = requests.get(url)
    # parse the html response 
    soup = BeautifulSoup(response.content,'html.parser')
    citation_needed=soup.find_all('a', {'title': 'Wikipedia:Citation needed'})
    return len(citation_needed)


def get_citations_needed_report(url):
    """
    function finds the paragraph that contains citation needed 
    Arguments : url 
    Returns : list of strings of paragraphs

    """
    # send a request using requests tool 
    response = requests.get(url)
    # parse the html response 
    soup = BeautifulSoup(response.content,'html.parser')

    paragraphs=soup.find_all('p')

    all_paragraphs=[]
    for paragraph in paragraphs:
        paragraph_citation_needed = paragraph.find('a',{'title':'Wikipedia:Citation needed'})
        if paragraph_citation_needed :
            all_paragraphs.append(paragraph.text)
    return all_paragraphs

if __name__ == '__main__':

    # print(get_citations_needed_count(url))   
    print(get_citations_needed_report(url))
    pass