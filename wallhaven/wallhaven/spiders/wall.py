import scrapy
from wallhaven.items import WallhavenItem


class WallSpider(scrapy.Spider):
    name = 'wall'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/toplist?page=1']

    def parse(self, response):
        # 获取进入第二个页面的链接
        hrefs = response.xpath("//a[@class='preview']/@href").extract()
        for url in hrefs:
            yield scrapy.Request(url=url, callback=self.parse_second)

    def parse_second(self, response):
        src_list = response.xpath("//img[@id='wallpaper']/@src").extract()
        for src in src_list:
            print(src)
            img_src = WallhavenItem(src=src)
            # 获取一个img_src就将book交给piplines
            yield img_src

    # 控制下载页数
    # def about_page:
    #     if self.page < 3:
    #         self.page = self.page + 1
    #         url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
    #         # 怎么去调用pass方法
    #         # scrapy.Request就是scrapy的get请求
    #         # url 是请求地址
    #         # callback就是你要执行的那个函数，注意不要加()
    #         yield scrapy.Request(url=url, callback=self.parse)
