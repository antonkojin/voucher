# -*- coding: utf-8 -*-
import scrapy

class AddressesSpider(scrapy.Spider):
    name = "addresses"
    start_urls = [
        'http://serviziweb.tabaccai.it/voucherinps/VistaAdesioni.aspx',
    ]

    def __init__(self, comune=None, *args, **kwargs):
        super(AddressesSpider, self).__init__(*args, **kwargs)
        self.comune = comune

    def parse(self, response):
        formdata = {
            "ctl00$ContentPlaceHolder1$tbCap": "",
            "ctl00$ContentPlaceHolder1$tbComune": self.comune,
        }
        form_request = scrapy.FormRequest.from_response(response, formdata=formdata, callback=self.after_query)
        self.logger.info("form request: %s", form_request.body)
        return form_request

    def after_query(self, response):
        requests = []
        requests.append(scrapy.FormRequest.from_response(response, callback=self.parse_tabaccai))
        pages = response.xpath("//table[@id='ctl00_ContentPlaceHolder1_GridView1']/tr[@class='pager']//a/text()")
        for page in pages:
            formdata = {
                "__EVENTTARGET": "ctl00$ContentPlaceHolder1$GridView1",
                "__EVENTARGUMENT": "Page$" + page.extract()
            }
            self.logger.info("request page: %s", page)
            requests.append(scrapy.FormRequest.from_response(response, formdata=formdata, callback=self.parse_tabaccai))
        self.logger.debug("requests: " +  str(map( (lambda form: form.body), requests )))
        return requests

    def parse_tabaccai(self, response):
        trs = response.xpath("//table[@id='ctl00_ContentPlaceHolder1_GridView1']/tr")
        addresses = trs[1:-2]
        items = []
        for line in addresses:
            from tabaccai.tabaccai.items import Address
            address = Address()
            address['indirizzo'] = line.xpath("td[1]/text()").extract()
            address['cap'] = line.xpath("td[2]/text()").extract()
            address['comune'] = line.xpath("td[3]/text()").extract()
            address['provincia'] = line.xpath("td[4]/text()").extract()
            self.logger.info("indirizzo: %s", address)
            items.append(address)
        return items
