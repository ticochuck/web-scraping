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

    
    def check_for_wiki_article(self):
        """
        Checks if wikipedia has an article with the input from the user.
        """
        no_article_found = 'Wikipedia does not have an article with this exact name.'
        
        if self.soup.find_all('table', id="noarticletext"):
            tables = self.soup.find_all('table', id="noarticletext")
            articles = tables[0].find_all('b')
            for b in articles:
                if b.text == no_article_found: 
                    print(no_article_found)
                    return False
        else: 
            return True


    def get_citations_needed_count(self):
        """
        Takes in url of a wikipedia page
        Returns an interger of number of citations needed in the page
        """
        citations = self.soup.find_all('a', title = 'Wikipedia:Citation needed')
        total_citations = len(citations)
        
        if total_citations == 0:
            return print("\nThis page does not need any citations\n")
        else:
            print(f'\nThis page needs a total of {total_citations} citations.\n')
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
    

def auto_search():
        search = input('What would you like to search for in Wikipedia? \n')
        x = search.split()
        formatted_search = ""

        for word in x:
            formatted_search +=  str(word) + "_"
        
        domain_url = 'https://en.wikipedia.org/wiki/'
        formatted_url = str(domain_url) + str(formatted_search[:-1])
        print(formatted_url)
        wiki_search = wiki_page_parse(formatted_url)
        
        if wiki_search.check_for_wiki_article():
            wiki_search.get_citations_needed_count()
            wiki_search.get_citations_needed_report()
        

if __name__ == "__main__":
    auto_search()
