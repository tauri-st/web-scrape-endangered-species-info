import requests
from bs4 import BeautifulSoup

#holds the variables to gather data
def get_soup(url):
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  soup = get_soup(url)
  data = {}
  #select and extract category animals
  categories = soup.find_all("dl")
  for category in categories:
    category_name = categories.find("dt").get_text()
    category_animals = category.find_all("a")
    #this key-value pair should match the dictionary value
    data[category_name] = category_animals

  # Return the data here
  return data

category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")