from selenium import webdriver
import time 

"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
""" 
def getHtml(url, loadmore = False, waittime = 2):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time.sleep(waittime)
    if loadmore:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                next_button.click()
                time.sleep(waittime)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html

# for test
url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国"
html = getHtml(url)
print(html) 
