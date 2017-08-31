import requests

def getHtml(url):
    response = requests.get(url)
    html = response.text
    return html
