
from lxml import etree

class MidiKaraokeVideo(object):
    def getKarList(self, connection):
        print('getKarList!!!')
        """
        page = connection.get('https://midi-karaoke-video.blogspot.it/2014/11/midi-karaoke-cantanti-italiani-ordine.html')
        tree = etree.HTML(page.content)

        links = tree.xpath('//*[@class="post-body entry-content"]/center/table/tr[1]/td[1]/center/font/a/@href')
        print(len(links))
        print(links[0])

        link = links[0]

        page = connection.get(link)
        tree = etree.HTML(page.content)

        altri_link = tree.xpath('//*[@class="post-body entry-content"]/center[2]/table[2]/tr[1]/td[1]/center/font/font/a/@href')

        print('link per A :', len(altri_link))

        for i in range(len(altri_link)):
            #print('primo link A :',altri_link.pop())
            continue

        link = altri_link[0]
        print('vado su ',link)
        page = connection.get(link)
        tree = etree.HTML(page.content)
        altri_link = tree.xpath('//*[@class="post-body entry-content"]/center[1]/table')

        print('per download :',len(altri_link))
        print('per download :',altri_link[0])
        print(etree.tostring(altri_link[1]))
        """