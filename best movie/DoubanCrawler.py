import expanddouban as edb
from bs4 import BeautifulSoup


class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link


class OutputData:
    def __init__(self, category, location, percent):
        self.category = category
        self.location = location
        self.percent = percent


def getLocations():
    result = []
    base_url = getMovieUrl()
    html = edb.getHtml(base_url)
    soup = BeautifulSoup(html, "html.parser")
    ul_list = soup.find("div", class_="tags").select('ul[class="category"]')
    if len(ul_list) == 4:
        for li in ul_list[2].find_all("li"):
            location = li.find('span', class_="tag").get_text()
            if location != "全部地区":
                result.append(location)

    return result


def getMovieUrl(category=None, location=None):
    """
    通过参数生成url
    :param category: 分类
    :param location: 地区
    :return: 电影url
    """
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags={}"
    tag_list = ["电影"]
    if category:
        tag_list.append(category)
    if location:
        tag_list.append(location)

    tags = ",".join(tag_list)

    return url.format(tags)


def getMovies(category, location, load_more=False, wait_time=2):
    html = edb.getHtml(getMovieUrl(category, location), loadmore=load_more, waittime=wait_time)

    return parseHtml(html, category, location)


def parseHtml(html, category, location):
    result = []
    soup = BeautifulSoup(html, "html.parser")

    divs = soup.find("div", class_="list-wp")
    for a in divs.find_all("a"):
        info_link, cover_link, name, rate = parseHref(a)
        m = Movie(name, rate, location, category, info_link, cover_link)
        result.append(m)

    return result


def parseHref(a):
    info_link = a.get('href')
    image = a.select('div[class="cover-wp"] > span[class="pic"] > img')
    if len(image) > 0:
        cover_link = image[0].get('src')
    else:
        cover_link = ""

    name_node = a.select('p > span[class="title"]')
    if len(name_node) > 0:
        name = name_node[0].get_text()
    else:
        name = ""

    rate_node = a.select('p > span[class="rate"]')
    if len(rate_node) > 0:
        rate = rate_node[0].get_text()
    else:
        rate = ""

    return info_link, cover_link, name, rate


def saveFile(data, filename="movies.csv"):
    f = open(filename, 'w')
    if isinstance(data, list):
        for movie in data:
            attrs = vars(movie)
            # print(', '.join("%s: %s" % item for item in attrs.items()))
            row = ','.join("%s" % item for item in attrs.values())
            f.write(row + "\n")

    f.close()


def start_crawler_task(categorys=[]):
    locations = getLocations()
    my_movies = []
    for category in categorys:
        for location in locations:
            # print("start get {} {}'s movies ".format(category, location))
            my_movies.extend(getMovies(category, location, True))

    saveFile(my_movies)

    # 生成报告
    output = analyseData(readFile("movies.csv"))
    saveFile(output, "output.txt")


def readFile(data_file):
    result = {}
    with open(data_file, 'r') as f:
        for line in f:
            row_list = line.strip().split(',')
            location = row_list[2]
            category = row_list[3]
            if category in result:
                if location in result[category]:
                    result[category][location] += 1
                else:
                    result[category][location] = 1
            else:
                result[category] = {location: 1}
    return result


def analyseData(result):
    output = []
    for item in result:
        sorted_data = sorted(result[item].items(), key=lambda x: x[1], reverse=True)
        sum_data = sum(result[item].values())
        for location, value in sorted_data[:3]:
            o = OutputData(item, location, "{:.2%}".format(value / sum_data))
            output.append(o)
    return output


start_crawler_task(['科幻', '剧情', '动作'])
