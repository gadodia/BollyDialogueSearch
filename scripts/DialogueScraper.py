'''
Created on Sep 17, 2016

@author: vineetgadodia
'''
from lxml import html
import requests
import csv
COUNT = 0
def fetch_data(url, writer):
    global COUNT
    dialogues = requests.get(url)
    dia_tree = html.fromstring(dialogues.text)
    for node in dia_tree.xpath('//*[@id="dialogueBoxes"]/div'):
        try:
            hindi_dia = node.xpath('./div[2]/div[2]/text()')[0]
            english_dia = node.xpath('./div[3]/div[2]/text()')[0]
            attr_list = node.xpath('./div[4]/text()')
            movie_name = attr_list[0]
            actor_name = attr_list[2]
            cat = attr_list[4:]
            cat = ','.join(v.replace('|','').strip() for v in cat)
        except:
            print "Failed to process"
            continue
        COUNT += 1
        writer.writerow([url, movie_name, actor_name, hindi_dia, english_dia, cat])

def scrape():
    global COUNT
    filename = open("output.csv", "w")
    writer = csv.writer(filename)
    movies = requests.get('http://www.filmyquotes.com/movies/')
    movies_tree = html.fromstring(movies.text)
    for node1 in movies_tree.xpath('//*[@id="moviesListTabContent"]/ul'):
        for node2 in node1.xpath('./li'):
            link = node2.xpath('./a')[0].attrib['href']
            if 'list' not in link:
                url = 'http://www.filmyquotes.com{0}'.format(link)
                fetch_data(url, writer)
    print COUNT

if __name__ == '__main__':
    scrape()