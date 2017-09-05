import scrapy
from scrapy import Selector
from selenium import webdriver

class MovieSpider(scrapy.Spider,url):
    name = "movie_spider"
    allowed_domains = ['douban.com']
    start_url = [url]

    def start_request(self):
        self.driver = webdriver.Firefox()
        driver.get(self.start_url)
        while True:
            next_url = driver.find_element_by_xpath('//div[@class="more"]/a')
            try:
                # click the button to go to next page
                next_url.click()
            except:
                break
                # parse the body your webdriver has
                self.parse(driver.page_source)
        driver.close()

    def parse(self, body):
        # create Selector from html string
        html = Selector(text=body)
        return html
        """
        # parse it
        for movie in html.css('.list-wp'):
            item = dict()
            item['title'] = movie.css('.title::text').extract_first()
            item['rate'] = movie.css('.rate::text').extract_first()
            # extract link (::attr(href))
            yield item
        """

def getHtml(url):
    movie = MovieSpider(url)
    return movie.start_request()
