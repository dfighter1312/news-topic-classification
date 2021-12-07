import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "evnexpress_contents"
    with open('filtered_links.txt') as f:
        start_urls = f.readlines()
    # start_urls = [
    #     'https://e.vnexpress.net/news/business/economy/car-registration-fee-cut-by-half-again-4394956.html',
       
    # ]

    def url_to_classes(self, url):
        # def find_nth_slash(string, n):
        #     for i, c in enumerate(string):
        #         if c == '/':
        #             n -= 1
        #             if n == 0:
        #                 return i
        #     return None
        #  'https://e.vnexpress.net/news/business/economy/car-registration-fee-cut-by-half-again-4394956.html',
        
        parts = url.split('/')
        if parts[4] in ['news', 'world']:
            return parts[4], parts[4]
        else:
            return parts[4], parts[5]

    def parse(self, response):
        main_class, sub_class = self.url_to_classes(response.request.url,)
        yield {
            'main_class': main_class,
            'sub_class': sub_class,
            'title': response.css('h1.title_post::text').get(),
            'body': ''.join(response.css('div.fck_detail p::text').getall()),
            'tag': ','.join([re.sub(r"[\n\t]+", "",tag) for tag in response.css('h4.tag_item a::text').getall()])
        }