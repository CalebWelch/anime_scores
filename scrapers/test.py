from bs4 import BeautifulSoup as bsoup
from collections import defaultdict
import requests as rq
import json
import re
import pandas as pd

def savetojson(data):
    with open('anime_ratings','w+') as fp:
	json.dump(data,fp)

def getLines(showCount=0):
    shows = defaultdict(list)
    showName = []
    href =[]
    loopCount = showCount/50
    for i in range(0,loopCount):
        flag = True
        while flag:
            print i,loopCount,showCount
            try:
                page= rq.get('http://myanimelist.net/topanime.php?limit='+str(50*i))
                flag = False
            except Exception:
                flag = True
                print 'retrying loop'
            soup = bsoup(page.content,'html.parser')
            table = soup.find_all('tr',class_="ranking-list")
            #shows = defaultdict(list)
            #showName = []
            for element in table:
                show = element.find('div',class_="di-ib clearfix")
                show.a['href']
                s = (show.a['href']).encode('utf-8').strip().split('/')[-1].replace('_',' ')
                href.append(show.a['href'])    
                showName.append(s)
		print s
            for index, name in enumerate((href)):
                index = index + i * 50
		genre = {"Genre":""}
		try:
		   print index, showName[index], len(href)
		   page = rq.get(href[index])
		except IndexError:
		   print 'index is out of bounds'
		   pass
                soup = bsoup(page.content,'html.parser')
                table = soup.find_all('div',class_='js-scrollfix-bottom')
                try:
                    genres =(table[0].find_all(text="Genres:")[0].parent.parent.find_all("a"))
                    score = soup.find_all('div',class_='fl-l score')[0].get_text(strip=True)
                except IndexError:
                    print "uh oh"
                    pass
		try:
                    shows[showName[index]] = [[x.get_text() for x in genres], score]
		except IndexError:
		    print 'index out of bounds :('
		    break
            if len(shows) == 0:
		print "get request messed up, restarting page"
                flag = True
	    print i, loopCount, showCount
            #with open('anime_ratings'+str(i)+'.json','w+') as fp:
                #json.dump(shows,fp)
    savetojson(shows)

def main():
    while True:
        numShows = input('Enter number of shoes as a multiple of 50 :: ')
        if numShows%50 is 0:
            break
        else:
            print "not a multiple of 50 :: "
            
    getLines(numShows)

if __name__ == "__main__":
    main()
