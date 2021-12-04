# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request


class WallhavenPipeline:
    def scrapy_open(self, spider):
        pass

    def process_item(self, item, spider):
        return item

    def scrapy_close(self, spider):
        pass


class WallhavenDownLoadPipeline:
    def process_item(self, item, spider):
        url = item.get('src')
        name = item.get('src').split('/')[-1]
        filename = './Wallhaven/' + name
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/95.0.4638.69 ')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url=url, filename=filename)
        return item












