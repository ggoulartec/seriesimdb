import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    def parse(self, response):
        for series in response.css('.titleColumn'):
            yield {
                'titulo': series.css('.titleColumn a::text').get(),
                'ano': series.css('.secondaryInfo::text').get(),
                'nota': response.css('strong::text').get()
            }
