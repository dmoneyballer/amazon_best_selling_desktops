import scrapy


class DesktopsSpider(scrapy.Spider):
    name = "desktops"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/Best-Sellers-Desktop-Computers/zgbs/electronics/565098"]

    def parse(self, response):
        ranks = response.css('span.zg-bdg-text::text').getall()
        descriptions = response.css('a.a-link-normal span div._cDEzb_p13n-sc-css-line-clamp-3_g3dy1::text').getall()
        ratings = response.css('span.a-icon-alt::text').getall()
        number_of_ratings = response.css('span.a-size-small::text').getall()
        #clean the desktop computer text in the list
        number_of_ratings = [int(val.replace(',', '')) for val in number_of_ratings if val.replace(',', '').isdigit()]
        prices = response.css('span.p13n-sc-price::text').getall()
        # I'm suspect of the prices there ^^ not 100% sure they are right. they deviate from what I see in the ui...
        for i, rank in enumerate(ranks):
            print(1+i, rank, ratings[i], descriptions[i], ratings[i], number_of_ratings[i], prices[i])
        #will yield later, I'm going to bed now