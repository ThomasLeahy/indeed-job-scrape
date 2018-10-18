import requests
from bs4 import BeautifulSoup
import pprint


url_to_scrape = "https://www.indeed.co.uk/jobs?q=data+scientist&l=London"

page_response = requests.get(url_to_scrape, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

print(page_content.prettify())

jobPosts = []
for i in range(0, 20):
    anchors = page_content.find_all("a")[i].text
    jobPosts.append(anchors)

pprint.pprint(jobPosts)