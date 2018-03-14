
from lxml import etree
import re

class MidiKaraokeVideo(object):
    all_links = []
    all_midi = []
    midi_by_singer = {}

    def getKarList(self, connection):
        
        page = connection.get('https://midi-karaoke-video.blogspot.it/2014/11/midi-karaoke-cantanti-italiani-ordine.html')
        tree = etree.HTML(page.content)

        links = tree.xpath('//*[@class="post-body entry-content"]//font/a/@href')
        self.addAll(links, None)

        n = 1
        for link in self.all_links:
            print(n,'/',len(self.all_links))
            n += 1
            page = connection.get(link)
            tree = etree.HTML(page.content)

            singer = tree.xpath('//*h3[@class="post-title entry-title"]/text()')
            if singer:
                singer = singer.split('-')[1]
                singer = re.sub('(^\s+)|(\s+$)','',singer)

            altri_link = tree.xpath('//*[@class="post-body entry-content"]//font/a/@href')
            self.addAll(altri_link, singer)

            altri_link = tree.xpath('//*[@class="post-body entry-content"]//font/li/a/@href')
            self.addAll(altri_link, singer)
            
        print('found ',len(self.all_midi,' midi'))
        
    def addAll(self, arr, singer):
        link_added = False
        midi_added = False
        for ele in arr:
            if ele.endswith('.mid'):
                if self.all_midi.count(ele) == 0:
                    self.all_midi.append(ele)
                    midi_added = True
                    if singer:
                        self.add(singer, ele)
            else:
                if self.all_links.count(ele) == 0:
                    self.all_links.append(ele)
                    link_added = True
        return link_added, midi_added

    def add(self, singer, url):
        if not self.midi_by_singer.has_key(singer):
            self.midi_by_singer[singer] = []
        self.midi_by_singer[singer].append(url)