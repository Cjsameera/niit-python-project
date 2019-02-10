import requests
from bs4 import BeautifulSoup
word=input("enter:")

url = "http://www.read.gov/aesop/007.html"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("p")
print(links)
count=0
for i in links:
  if soup.findAll(text = word):
      count+=1
print(count)
