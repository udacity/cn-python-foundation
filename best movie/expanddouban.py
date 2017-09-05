import scrapy
from scrapy import Selector
from selenium import webdriver

class MovieSpider(scrapy.Spider):
    name = "movie_spider"
    allowed_domains = ['douban.com']
    start_url = ['https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=%E7%94%B5%E5%BD%B1,%E7%BE%8E%E5%9B%BD,%E5%96%9C%E5%89%A7']

    def start_request(self):
        self.driver = webdriver.Firefox()
        driver.get(self.start_url)
        while True:
            next_url = driver.find_element_by_xpath('//div[@class="more"]/a')
            try:
                # parse the body your webdriver has
                self.parse(driver.page_source)
                # click the button to go to next page
                next_url.click()
            except:
                break
        driver.close()

    def parse(self, body):
        # create Selector from html string
        sel = Selector(text=body)
        # parse it
        for article in sel.css('.list-wp'):
            item = dict()
            item['title'] = article.css('.title::text').extract_first()
            item['rate'] = article.css('.rate::text').extract_first()
            # extract link (::attr(href))
            yield item
