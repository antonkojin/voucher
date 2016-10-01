import falcon
from scrapy.crawler import CrawlerProcess
from tabaccai.tabaccai.spiders.addresses import AddressesSpider

def crawl(comune):
    process = CrawlerProcess()
    process.crawl(AddressesSpider, comune=comune)
    process.start()

class TabaccaiResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = crawl("milano")

app = falcon.API()

tabaccai = TabaccaiResource()

app.add_route('/tabaccai', tabaccai)
