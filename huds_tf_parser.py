import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}
PAGES_SWITCH_LINK = 'https://huds.tf/forum/forumdisplay.php?fid=27&page='


def get_page(url):
    req = requests.get(url, headers=HEADERS)

    if req.status_code != 200:
        print("Oops! Couldn't get web page's source code!")
        exit(-1)

    return req.text


def parse_sounds(page_number):
    url = PAGES_SWITCH_LINK + str(page_number)
    html = get_page(url)

    soup = BeautifulSoup(html, "html5lib")
    containers = soup.find_all('div', class_='card text-theme bg-theme mb-3')

    result = []

    for i in containers:
        author_line = i.find('a', href=True, title=True)
        if not author_line:
            continue
        title = author_line['title']
        author = i.find('a', href=True, title=False).get_text()
        file_name = i.find('audio')['src']
        link = 'https://huds.tf/forum/' + file_name

        res = {'title': title,
               'author': author,
               'link': link}
        result.append(res)

    return result
