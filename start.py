from utils import ModuleLoader, Connection
import os, requests

DOWNLOAD_FOLDER = "d:\\salvo\\kar\\"

print('*** START ***')

main_folder = '/home/salvo/kar/'

def download_file(folder, url):
    folder = os.path.join(main_folder, folder)
    local_filename = os.path.join(folder, url.split('/')[-1])
    if not os.path.exists(folder):
        os.makedirs(folder)
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

modules = ModuleLoader().load('modules')

for clazz in modules:
    m = clazz()
    lst = m.getKarList(Connection())
    n = 1
    m = len(lst)
    for singer,url in lst.iteritems():
        print(n,'/',m)
        n += 1
        download_file(singer,url)

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
