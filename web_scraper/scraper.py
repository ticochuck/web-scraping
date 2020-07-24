import requests
from bs4 import BeautifulSoup

class wiki_page_parse():
    """
    Main class. Takes in a URL and parses information from the website. 
    """
    def __init__(self, URL):
        self.url = URL
        self.response = requests.get(URL)
        self.content = self.response.content
        self.soup = BeautifulSoup(self.content, 'html.parser')


    def get_citations_needed_count(self):
        """
        Takes in url of a wikipedia page
        Returns an interger of number of citations needed in the page
        """
        
        citations = self.soup.find_all('a', title = 'Wikipedia:Citation needed')
        total_citations = len(citations)
        print(total_citations, 'total citations')
        return total_citations


    def get_citations_needed_report(self):
        """
        Takes in url of a wikipedia page
        Returns a formatted string with each citation needed in separete lines, in the order found
        """
        
        citations = self.soup.find_all('p')
        paragraphs = ""
        for p in citations:
            if p.find('a', title = 'Wikipedia:Citation needed'): 
                paragraphs += str(p.text) + '\n'
        print(paragraphs)
        return paragraphs
    
washington= wiki_page_parse("https://en.wikipedia.org/wiki/United_States")
washington.get_citations_needed_count()
washington.get_citations_needed_report()
