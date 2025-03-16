import requests
from bs4 import BeautifulSoup
import pandas as pd

def targetListings(url):
    response = requests.get(url)

    searchResults = []
    
    if(response.status_code == 200):
        htmlContent = response.text

        soup = BeautifulSoup(htmlContent, "html.parser")

        products = soup.select()
    else:
        print(f"Error: {response.statuse_code}") 

def main():
    url = "https://www.target.com/s?searchTerm=pokemon&tref=typeahead%7Cterm%7Cpokemon%7C%7C%7Chistory&ignoreBrandExactness=true&facetedValue=tkle6&Nao=0&moveTo=product-list-grid"

    results = targetListings(url)

if __name__== "__main__":
    main()

# data = []

# proceed = True

# while(proceed):
#     url = "https://www.target.com/s?searchTerm=pokemon&tref=typeahead%7Cterm%7Cpokemon%7C%7C%7Chistory&ignoreBrandExactness=true&facetedValue=tkle6&Nao=0&moveTo=product-list-grid"

#     page = requests.get(url)

#     soup = BeautifulSoup(page.text, "html.parser")