from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
all_anchors = soup.find_all(name="a")
for tag in all_anchors:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")