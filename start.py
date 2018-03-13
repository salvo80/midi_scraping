from utils import ModuleLoader, Connection

DOWNLOAD_FOLDER = "d:\\salvo\\kar\\"

print('*** START ***')

def download(karModel):
    return

modules = ModuleLoader().load('modules')

for module_name, class_name in modules:
    print('module: ',module_name,' class: ', class_name)
    module = __import__(module_name)
    class_ = getattr(module, class_name)
    m = class_()
    lst = m.getKarList(Connection())
    for l in lst:
        print('{',l.singer)
        print(l.title)
        print(l.url)
        print(l.isKar,'}')
        download(l)

print('*** END ***')

"""
page = requests.get('https://midi-karaoke-video.blogspot.it/2014/11/midi-karaoke-cantanti-italiani-ordine.html',headers={},proxies=proxyDict)
tree = etree.HTML(page.content)

links = tree.xpath('//*[@class="post-body entry-content"]/center/table/tr[1]/td[1]/center/font/a/@href')
print(len(links))
print(links[0])

link = links[0]

page = requests.get(link,headers={},proxies=proxyDict)
tree = etree.HTML(page.content)

altri_link = tree.xpath('//*[@class="post-body entry-content"]/center[2]/table[2]/tr[1]/td[1]/center/font/font/a/@href')

print('link per A :', len(altri_link))

for i in range(len(altri_link)):
    #print('primo link A :',altri_link.pop())
    continue

link = altri_link[0]
print('vado su ',link)
page = requests.get(link,headers={},proxies=proxyDict)
tree = etree.HTML(page.content)
altri_link = tree.xpath('//*[@class="post-body entry-content"]/center[1]/table')

print('per download :',len(altri_link))
print('per download :',altri_link[0])
print(etree.tostring(altri_link[1]))

"""
