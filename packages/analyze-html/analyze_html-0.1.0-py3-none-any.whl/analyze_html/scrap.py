import requests
from bs4 import BeautifulSoup

tag_to_find = ["div","a","li","p"]

def get_html(url):
    response = requests.get(url)
    print(response.status_code)
    html = response.text
    return html

def count_tag(tag,html):
    soup = BeautifulSoup(html,"html.parser")
    get_tag = soup.find_all(tag)
    count = len(get_tag)
    print(f"{count} of <{tag}> tag contained.")   
    return count 

if __name__=="__main__":
    url = "https://books.toscrape.com/"
    html = get_html(url)
    for tag in tag_to_find:
        count_tag(tag,html)