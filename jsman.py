#!/usr/bin/python
import urllib2
import json
import sys
import os


def search(query):
    query = query.replace(" ", "\%20")
    baseurl = "https://developer.mozilla.org/en-US/search?format=json&q="
    url = baseurl + query
    data = urllib2.urlopen(url).read()
    return json.loads(data)


def getFirstResult(searchResult):
    firstEntry = searchResult['documents'][0]
    return (firstEntry['title'], firstEntry['url'])


def openUrl(url):
    os.system("firefox " + url)


def main():
    query = " ".join(sys.argv[1:])
    print "Searching \"" + query + "\"..."
    result = search(query)
    title, url = getFirstResult(result)
    print "Found: " + title
    print url
    openUrl(url)

if __name__ == '__main__':
    main()
