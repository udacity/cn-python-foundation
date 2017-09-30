项目2 豆瓣上最好的电影
=====

项目概述
----

在这个项目中, 你将会从豆瓣电影的网页中获取各个地区、各个类别的高评分电影，收集他们的名称、评分、电影页面的链接和电影海报的链接。最后对收集的数据进行简单的统计。

这个项目不会提供任何 python 代码，你应该新建文件 `DoubanCrawler.py`, 并在其中逐个完成每个任务。注意这些任务并不是并列关系，后面的任务很可能需要用到前面任务的代码或函数，前面任务的对错也很可能会影响后面任务的对错。你可能会需要多次来回修改才能完成项目。

当然，即使你还没有全部完成，也可以提交项目来获取一些建议和反馈。


任务1: 获取每个地区、每个类型页面的URL
----
你可以从下面这个网址，按照分类和地区查看电影列表。

```
https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影
```
分解 URL 可以看到其中包含

-  `https://movie.douban.com/tag/#/`: 	豆瓣电影分类页面
-  `sort=S`: 按评分排序
-  `range=9,10`: 评分范围 9 ~ 10
-  `tags=电影`: 标签为电影

其中参数tags可以包含多个以逗号分隔的标签，你可以分别选取类型和地区来进行进一步的筛选，例如选择类型为`剧情`，地区为`美国`, 那么 URL 为

```
https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国
```

实现函数构造对应类型和地区的URL地址

```
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location)
	url = None
	retrun url
```
任务2: 获取电影页面 HTML
-----
获得URL后，我们可以获取 URL 对应页面的 HTML

在课程中，我们使用库 `requests` get 函数。

```
import requests
response = requests.get(url)
html = response.text
```

这样的做法对大多数豆瓣电影列表页面来说没什么问题。但有些列表需要多页显示，我们需要不断模拟点击**加载更多**按钮来显示这个列表上的全部电影。

这个任务虽然不难，但并不是课程的重点。因此我们已经为你完成了这个任务。你只需要导入我们已经写好的文件，并调用库就可以了

```
import expanddouban
html = expanddouban.getHtml(url)
```


任务3: 定义电影类
-----
电影类应该包含以下成员变量

- 电影名称
- 电影评分
- 电影类型
- 电影地区
- 电影页面链接
- 电影海报图片链接

同时，你应该实现电影类的构造函数。

```
name = “肖申克的救赎”
rate = 9.6
location = "美国"
category = "剧情"
info_link = "https://movie.douban.com/subject/1292052/"
cover_link = “https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg”

m = Movie(name, rate, location, category, info_link, cover_link)
```

任务4: 获得豆瓣电影的信息
-----
通过URL返回的HTML，我们可以获取网页中所有电影的名称，评分，海报图片链接和页面链接，同时我们在任务1构造URL时，也有类型和地区的信息，因为我们可以完整的构造每一个电影，并得到一个列表。

实现以下函数

```
"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location)
	return []
```

提示：你可能需要在这个任务中，使用前三个任务的代码或函数。

任务5: 构造电影信息数据表
-----
获取每个类型，每个地区的电影信息后，我们可以获得一个包含所有类型、所有地区，评分超过9分的完整电影对象的列表。将列表输出到文件 `movies.csv`，格式如下:

```
肖申克的救赎,9.6,美国,剧情,https://movie.douban.com/subject/1292052/,https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg
霍伊特团队,9.0,香港,动作,https://movie.douban.com/subject/1307914/,https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2329853674.jpg
....
```

任务6: 统计电影数据
-----
统计在每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比为多少？

请将你的结果输出文件 `output.txt`

项目提交
-----
在提交之前，根据项目评审标准检查你的项目。Udacity 的项目评审员会根据这个标准对你的项目给予反馈，并对你的代码给出有用的指导。

| 标准| 符合要求|
| ------------- |:-------------|
| 代码质量      | 你的代码应具有良好的结构与可读性，请遵循本课程所指出的最佳规范。 |
| 不打印任何内容      | 你的代码应不会打印任何内容，而只是创建或修改两个文件 `movies.csv` 和 `output.txt` |
| 完成任务1  | 实现函数`getMovieUrl`|
| 完成任务2  | 通过 URL 获得豆瓣电影页面的 HTML |
| 完成任务3  | 定义电影类，并实现其构造函数|
| 完成任务4  | 通过类型和地区构造URL，并获取对应的HTML。解析 HTML 中的每个电影元素，并构造电影对象列表 |
| 完成任务5  | 将电影信息输出到 `movies.csv`。 包含所有类别、地区以及对应的电影信息|
| 完成任务6  | 将电影的统计结果输出到 `output.txt`。包含在每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比为多少。|

请提交submit.zip, 包含以下文件：

- DoubanCrawler.py
- 不要包含其他任何文件

注意运行 `python DoubanCrawler.py` 后，脚本应该会在同一个文件夹生成 `movies.csv` 和 `output.txt` 两个文件。