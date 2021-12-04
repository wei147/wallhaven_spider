import urllib.request

url = 'https://w.wallhaven.cc/full/pk/wallhaven-pkgkkp.png'
filename = url.split('/')[-1]
# print(start)
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/95.0.4638.69 ')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url=url, filename=filename)
