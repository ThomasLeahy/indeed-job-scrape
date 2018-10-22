import requests
from bs4 import BeautifulSoup
import pprint


url_to_scrape = "https://www.indeed.co.uk/jobs?q=data+scientist&l=London&start={}"
jobPosts = []

page_limits = range(0,110,10)

for lim in page_limits:
    page_response = requests.get(url_to_scrape.format(lim), timeout=5)

    page_content = BeautifulSoup(page_response.content, "html.parser")

    #print(page_content.prettify())

    anchors = page_content.find_all("a", attrs={"data-tn-element":"jobTitle"} )
    for anchor in anchors:
        jobPosts.append("{}&vjk={}".format(url_to_scrape.format(lim), anchor.find_parent('div')['data-jk']))
    pprint.pprint(jobPosts)
