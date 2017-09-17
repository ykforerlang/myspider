import urllib2
import re

def getStar(url):
    res = urllib2.urlopen(url)
    html = res.read()
    return getStarFromHtml(html)


def getStarFromHtml(html):

    indexStart = html.index('ratings-on-weight')
    indexEnd = html.index('interest_sect_level')

    partHtml = html[indexStart: indexEnd]


    reR = re.sub(r'<.*?>', '=======', partHtml)
    reRArray = reR.split('=======')

    newRe = []
    for ele in reRArray:
        trimEle = ele.strip()
        if (trimEle != ''):
            newRe.append(trimEle)


    return {
        '1': newRe[10],
        '2': newRe[8],
        '3': newRe[6],
        '4': newRe[4],
        '5': newRe[2]
    }