# -*- coding: utf-8 -*-

# Scrapy settings for tianyancha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 调度器的类和去重的类替换为scrapy_redis提供的类
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

# Redis连接配置
REDIS_URL = 'redis://:1111@39.106.189.108:6379'

# MongoDB连接配置
MONGO_URI = 'mongodb://39.106.189.108:27017/'

# 配置调度队列
# 优先级队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 先进先出队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# 后进先出队列(栈)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# 配置持久化
# 此配置是可选的，默认是False。scrapy_redis默认会在爬取完成后清空爬取队列和去重指纹集合。设置为True之后，不会自动清空。
SCHEDULER_PERSIST = False

# 配置重爬
# 此配置是可选的，默认是False。如果配置了持久化或者强制中断了爬虫，那么爬取队列和指纹集合不会被清空，
# 爬虫重新启动之后就会接着上次爬取，如果想重新爬取，设置为True。
SCHEDULER_FLUSH_ON_START = False

BOT_NAME = 'tianyancha'

SPIDER_MODULES = ['tianyancha.spiders']
NEWSPIDER_MODULE = 'tianyancha.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Cookie': 'TYCID=7abe93109bb011e9a20641c848bcf009; undefined=7abe93109bb011e9a20641c848bcf009; ssuid=5120513320; _ga=GA1.2.895057816.1562047464; _gid=GA1.2.494401681.1562047464; aliyungf_tc=AQAAAA9N2yXZwgUA8dX5cjRtkJ32V2Dt; csrfToken=8ooxkq4zILoXEiSCUvZe2DEZ; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1562073852; _gat_gtag_UA_123487620_1=1; token=5d8a4cd1f0094ac0be2effbb8525808d; _utm=b3a4f5927fc948aca36790501e9e753b; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522Quiet.G%2522%252C%2522integrity%2522%253A%252214%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjA3Mzg3OSwiZXhwIjoxNTkzNjA5ODc5fQ.gVXUQlToau2SRfQsJtUAv2h-xvh8wwBUYe8gzJlcL4Ixr08L1Ver3W_KtLOf0-FoyXA6Lvq5d9UA2CXSdIzlJQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213383306337%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MjA3Mzg3OSwiZXhwIjoxNTkzNjA5ODc5fQ.gVXUQlToau2SRfQsJtUAv2h-xvh8wwBUYe8gzJlcL4Ixr08L1Ver3W_KtLOf0-FoyXA6Lvq5d9UA2CXSdIzlJQ; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1562073899',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tianyancha.middlewares.TianyanchaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'tianyancha.middlewares.TianyanchaDownloaderMiddleware': 543,
    'tianyancha.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # Pipeline配置
    # 此配置是可选的，默认是不启动Pipeline。scrapy_redis实现了一个存储到Redis的Item Pipeline。
    # 启用了这个Pipeline的话，爬虫会把生成的Item存储到Redis数据库中。
    # 'scrapy_redis.pipelines.RedisPipeline': 300,
    'tianyancha.pipelines.TianyanchaPipeline_mongodb': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
