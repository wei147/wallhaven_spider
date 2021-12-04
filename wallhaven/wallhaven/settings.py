# Scrapy settings for wallhaven project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wallhaven'

SPIDER_MODULES = ['wallhaven.spiders']
NEWSPIDER_MODULE = 'wallhaven.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'wallhaven (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 '
                  'Safari/537.36 ',
    'cookie': '_pk_id.1.01b8=48aa1f55146effe7.1616311124.; _pk_ses.1.01b8=1; '
              'XSRF-TOKEN'
              '=eyJpdiI6IkJmMmNJZjV5Vks4OUNtbzJUeHJjZVE9PSIsInZhbHVlIjoiajdYajJMcnhLbHNoOVFKMm5pczdYc245NjNKVmYydTBLd0pcLzFrelZRQXRVZ3Z1allpXC9ET3p3NWE1ekE2elN3IiwibWFjIjoiYmZkMGNkNDc2YWU0NjI2MWYwYTJmOTI4Y2FkMTg2YzE5MDNhMzM0YjRiOWI2ZDJlN2Q1ZjIyZWQzNTQ1NGVjNCJ9; wallhaven_session=eyJpdiI6InM5dklvdW8xNjE5QTVFNHBubHlqc0E9PSIsInZhbHVlIjoiMW9kK3RScnpVVWlzMGRRYmFIdElwSXZlNWhmMExLRkE3bDN3VXhKUndheUxlN0Z1dmRlY29LSWMzdU1ESUN4bCIsIm1hYyI6IjczZDc0YzI0YzU0MzM2N2I2ZDdjYWUxMWM2YmQwMjNjNTFiNzFkYTM3MDdjODk5YTYzMmZkZjZjYWU2MjZmNmIifQ%3D%3D '
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'wallhaven.middlewares.WallhavenSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'wallhaven.middlewares.WallhavenDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'wallhaven.pipelines.WallhavenPipeline': 300,
    'wallhaven.pipelines.WallhavenDownLoadPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
