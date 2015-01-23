#!/usr/bin/python
import urllib2
import json
import sys
import os
import platform
import webbrowser


def search(query):
    query = query.replace(" ", "\%20")
    baseurl = "https://developer.mozilla.org/en-US/search?format=json&q="
    url = baseurl + query
    data = urllib2.urlopen(url).read()
    return json.loads(data)


def getFirstResult(searchResult):
    if len(searchResult['documents']) == 0:
        return ("Not Found", None)
    firstEntry = searchResult['documents'][0]
    return (firstEntry['title'], firstEntry['url'])

def main():
    query = " ".join(sys.argv[1:])
    print "Searching \"" + query + "\"..."
    result = search(query)
    title, url = getFirstResult(result)
    if url is None:
        print title
    else:
        print "Found: " + title
        print url
        openUrl(url)
        webbrowser.open(url)

if __name__ == '__main__':
    main()
