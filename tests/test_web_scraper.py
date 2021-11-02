from web_scraper import __version__
import requests
from bs4 import BeautifulSoup
from web_scraper.scraper import get_citations_needed_count , get_citations_needed_report

def test_get_citations_needed_count():
    # Arrange
    url='https://en.wikipedia.org/wiki/History_of_Mexico' 
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    expected = 5

    # Act
    actual = get_citations_needed_count(soup)

    #Assert
    assert actual == expected




def test_version():
    assert __version__ == '0.1.0'
