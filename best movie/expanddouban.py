from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
 
 
def getHtml(url):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time = 1 #second for the broswer to wait
    WebDriverWait(browser, time)
    while True:
        try:
            next_button = browser.find_element_by_class_name("more")
            next_button.click()
            print("click")
        except:
            break
    html = browser.page_source
    browser.quit()
    return html

# for test
url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国"
html = getHtml(url)
print(html)
