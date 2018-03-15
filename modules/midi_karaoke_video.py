
from lxml import etree
import re

class MidiKaraokeVideo(object):
    all_links = []
    all_midi = []
    midi_by_singer = {}

    def getKarList(self, connection):
        
        page = connection.get('https://midi-karaoke-video.blogspot.it/2014/11/midi-karaoke-cantanti-italiani-ordine.html')
        tree = etree.HTML(page.content)

        links = tree.xpath('//div[contains(@class,"entry-content")]//font/a/@href')
        self.addAll(links, None)

        n = 1
        for link in self.all_links:
            print(n,'/',len(self.all_links),' and ',len(self.all_midi),' midi')
            n += 1
            page = connection.get(link)
            if not page:
                continue
            tree = etree.HTML(page.content)

            singer = self.getSinger(tree)
            print('singer: ', singer)

            altri_link = tree.xpath('//div[contains(@class,"entry-content")]//a/@href')
            self.addAll(altri_link, singer)

            #if len(self.midi_by_singer.items())>0:
            #    break
            
        print('found ',len(self.all_midi),' midi')
        return self.midi_by_singer
    
    def getSinger(self, tree):
        singer = tree.xpath('//div[contains(@class,"entry-content")]/center/center/font/text()')
        if len(singer)==0:
            singer = tree.xpath('//h3[contains(@class,"entry-title")]/text()')
        if len(singer)>0:
            singer = singer[0]
            if singer.count('-')>0:
                singer = singer.split('-')
                if singer[0].lower().count('midi')>0:
                    singer = singer[-1]
                else:
                    singer = singer[0]
            singer = re.sub('(^\s+)|(\s+$)','',singer)
        return singer

    def addAll(self, arr, singer):
        link_added = False
        midi_added = False
        for ele in arr:
            if ele.lower().endswith('.mid'):
                if self.all_midi.count(ele) == 0:
                    self.all_midi.append(ele)
                    midi_added = True
                    if singer:
                        self.add(singer, ele)
            elif ele.lower().endswith('.html'):
                if self.all_links.count(ele) == 0:
                    self.all_links.append(ele)
                    link_added = True
        return link_added, midi_added

    def add(self, singer, url):
        if not self.midi_by_singer.has_key(singer):
            self.midi_by_singer[singer] = []
        self.midi_by_singer[singer].append(url)