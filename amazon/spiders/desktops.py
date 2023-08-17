import scrapy


class DesktopsSpider(scrapy.Spider):
    name = "desktops"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/Best-Sellers-Desktop-Computers/zgbs/electronics/565098"]

    def parse(self, response):
        ranks = response.css('span.zg-bdg-text::text').getall()
        descriptions = response.css('a.a-link-normal span div::text').getall()
        ratings = response.css('span.a-icon-alt::text').getall()
        number_of_ratings = response.css('span.a-size-small::text').getall()
        #clean the desktop computer text in the list
        number_of_ratings = [int(val.replace(',', '')) for val in number_of_ratings if val.replace(',', '').isdigit()]
        # prices = response.css('span.p13n-sc-price::text').getall()
        # this prices seems right because when I use xpath I get the same
        prices = response.xpath("//span[@class='a-size-base']//span/text()").getall()
        # I'm suspect of the prices there ^^ not 100% sure they are right. they deviate from what I see in the ui...
        print('grabbed stuff')
        print(len(ranks),len(descriptions),len(ratings),len(number_of_ratings),len(prices))
        print(descriptions,prices)
        # for i, rank in enumerate(ranks):
        #     print(1+i, rank, ratings[i], descriptions[i], ratings[i], number_of_ratings[i], prices[i])
        # will yield later, I'm going to bed now
        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page:
            next_page = 'https://www.amazon.com/' + next_page
            yield response.follow(next_page, callback=self.parse)