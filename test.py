from bs4 import BeautifulSoup as bsoup
from collections import defaultdict
import requests as rq
import json
import re

page= rq.get('http://myanimelist.net/topanime.php?limit=0')
soup = bsoup(page.content,'html.parser')
table = soup.find_all('tr',class_="ranking-list")
shows = defaultdict(list)
showName = []
href = []
for element in table:
    show = element.find('div',class_="di-ib clearfix")
    show.a['href']
    s = (show.a['href']).encode('utf-8').strip().split('/')[-1].replace('_',' ')
    href.append(show.a['href'])    
    showName.append(s)
for index, name in enumerate(href):
    genre = {"Genre":""}
    print index, showName[index], len(href)
    page = rq.get(href[index])
    soup = bsoup(page.content,'html.parser')
    table = soup.find_all('div',class_='js-scrollfix-bottom')
    try:
        genres =(table[0].find_all(text="Genres:")[0].parent.parent.find_all("a"))
        score = soup.find_all('div',class_='fl-l score')[0].get_text(strip=True)
    except IndexError:
        print "uh oh"
        pass

    shows[showName[index]] = [[x.get_text() for x in genres], score]
print shows
print shows['Kimi no Na wa']
with open('anime_ratings.json','w') as fp:
    json.dump(shows,fp)
