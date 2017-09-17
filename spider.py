import urllib2
import json

import star

doubanMovieUrl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=100&page_start=0'

response = urllib2.urlopen(doubanMovieUrl)

responseString = response.read()

responseJson = json.loads(responseString)

subjects = responseJson['subjects']

newsub = subjects[:]

def movieSort(movie1, movie2):
    if float(movie1['rate']) > float(movie2['rate']):
        return -1
    elif float(movie1['rate']) == float(movie2['rate']):
        return 0
    else:
        return 1


newsub.sort(movieSort)
topTen = newsub[0:10]


movieWithStarArray = []
for movie in topTen:
    movieStars = star.getStar(movie['url'])
    movieWithStar = {
        'title': movie['title'],
        'rate': movie['rate'],
        'stars': movieStars
    }
    movieWithStarArray.append(movieWithStar)

print 'our result:', movieWithStarArray

