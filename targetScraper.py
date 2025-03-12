import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.target.com/s?searchTerm=pokemon&tref=typeahead%7Cterm%7Cpokemon%7C%7C%7Chistory&ignoreBrandExactness=true&facetedValue=tkle6&Nao=0&moveTo=product-list-grid"
response = requests.get(url)

if(response.status_code == 200):
    htmlContent = response.text
    print(htmlContent)
else:
    print(f"Error: {repsonse.statuse_code}")

# data = []

# proceed = True

# while(proceed):
#     url = "https://www.target.com/s?searchTerm=pokemon&tref=typeahead%7Cterm%7Cpokemon%7C%7C%7Chistory&ignoreBrandExactness=true&facetedValue=tkle6&Nao=0&moveTo=product-list-grid"

#     page = requests.get(url)

#     soup = BeautifulSoup(page.text, "html.parser")