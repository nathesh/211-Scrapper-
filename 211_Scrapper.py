# Written for Python 3.4
 
from lxml import html
import requests
 
root_url = "https://www.211texas.org"
links = []
page_number = 1
 
while True:
        search_url = "https://www.211texas.org/zf/profile/search?page=" + str(page_number) + "&controller=profile&action=search&module=default&%2Fzf%2Findex_php=&%2Fzf%2Fprofile%2Fsearch=&keyword=&popular_searches=&agency_name=&distance_zip=&area_served=Austin&taxonomy_category=&taxonomy_name=&dosearch=1&Search=Search"
        page = requests.get(search_url)
        tree = html.fromstring(page.text)
 
        links.extend(tree.xpath('//p[@class="service"]//a/@href'))
       
        if "Next >" in tree.xpath('//*[@id="paginationControl"]/span/text()'):
                break
 
        page_number += 1
       
file = open("211_corpus.html", "w")
 
for link in links:
        url = root_url + link
        service = requests.get(url)
        service_tree = html.fromstring(service.text)
        name = service_tree.xpath('//*[@id="profile"]/tbody/tr[1]/td/table/tbody/tr/td[2]/h2/text()')[0]
        description = service_tree.xpath('//*[@id="profile_data"]/tbody/tr[5]/td[2]/text()')[0]
       
        summary = "<h1>" + name + "</h1><p>" + description + " - " + url + "</p>\n"
        file.write(summary)
       
print("Done!")