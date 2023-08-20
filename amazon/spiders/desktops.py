import scrapy
import time
from datetime import datetime

class DesktopsSpider(scrapy.Spider):
    name = "desktops"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/Best-Sellers-Desktop-Computers/zgbs/electronics/565098"]

    def __init__(self, *args, **kwargs):
        super(DesktopsSpider, self).__init__(*args, **kwargs)
        self.crawl_time = datetime.now().isoformat()

    def parse(self, response):
        cards = response.css('div.p13n-grid-content')
        for card in cards:
            rank = card.css('span.zg-bdg-text::text').get()
            description = card.css('a.a-link-normal span div::text').get()
            rating = card.css('span.a-icon-alt::text').get()
            number_of_ratings = int(card.css('span.a-size-small::text').get().replace(',',''))
            price = card.css('span.a-size-base span::text').get()
            yield {
                'crawl_time': self.crawl_time,
                'rank' : rank,
                'description' : description,
                'rating' : rating,
                'number_of_ratings' : number_of_ratings,
                'price' : price
            }
            # will yield later, I'm going to bed now
        next_page = response.css('li.a-last a::attr(href)').get()
        time.sleep(2)
        if next_page:
            next_page = 'https://www.amazon.com/' + next_page
            yield response.follow(next_page, callback=self.parse)