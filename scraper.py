import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://www.condointernet.net/our-buildings/').read()
soup = BeautifulSoup(page)
aas = soup.findAll("a", {"class": "bldg_title"})
print("Name\tAddress\tCity\tState\tZip")
for a in aas:
    name = a.string
    address = a.next_sibling.next_sibling.contents[0]
    street_address = address.split(",")[0]
    state = "WA"
    city = "Seattle"
    zip_code = address[-5:]
    print("{}\t{}\t{}\t{}\t{}".format(name, street_address, city, state, zip_code))

