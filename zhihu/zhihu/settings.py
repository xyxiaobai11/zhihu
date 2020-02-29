# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 将其设置为False 默认头信息设置的cookie才能生效
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'cookie': '_zap=988a8e7a-d830-44b9-a329-44319dfa4ef6; d_c0="APDldsdrCg6PTh4uarz-OwltD0w_RLWZyGc=|1533997510"; _xsrf=HsdozDWCP9Do8ETHQEkPlcfpXTOxFXe3; __utma=155987696.376379388.1534422589.1534424814.1534428023.3; __gads=ID=f2754ad56f95a4ff:T=1544015706:S=ALNI_MZKIhaC9zZOfZkCvWO65bT7o-rwsw; tst=r; q_c1=6154cd2fd4bb4a72af44ef6681abdfe1|1579330162000|1533997510000; cap_id="ZTYzZGRkZDM1NWI5NDQ4ZDliYjViZDcwZGU5ZGNkOTA=|1579419466|6fa1afb5aa76c02ad6a08411f4b4aa3ce9d80ee3"; r_cap_id="OTI4ZDkwODBiZTIwNDcwZWFhY2RjOWVmMzA0ZDViNDk=|1579419466|7630991857e6b38f25872f0fdb03894b82cdcd3b"; l_cap_id="NzcyNGM0OTQ2NzUxNDViMjgwZmIxODU1M2NhZTRlODU=|1579419466|6bbfaa776ca35f434455d21722b6765d76fad2e5"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1579416892,1579417656,1579419481,1579420178; capsion_ticket="2|1:0|10:1579430510|14:capsion_ticket|44:Y2Q1NjRmMDhlOTQ5NDQ0YWJmMGMyMTJlMWUwNTNhYzI=|b9d79d8e6787b243ad44c066448e1e33715fad07073d8d73a96c01c5a97e4f3d"; z_c0="2|1:0|10:1579430517|4:z_c0|92:Mi4xQm9LaUN3QUFBQUFBOE9WMngyc0tEaVlBQUFCZ0FsVk5kWUFSWHdERmdoT05DQTlOQzRlQ3dyNlUxcGpDNXNrTTZR|808586eea6f0703f6756db2226bef05b2f93c494db43e450e09c09bf58651ccb"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1579430476; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1579430525|1579428973',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihu.pipelines.ZhihuTwistMysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

HOST = '192.168.227.129'
DBNAME = 'zhihu'
USER = 'root'
PASSWD = '123456'

SQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SQL_DATE_FORMAT = '%Y-%m-%d'