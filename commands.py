from urllib2 import quote
import requests
from flask import Flask

def calc(query):
    return ''

def weather(query):
    url = ''
    if query is None or query == '':
        return 'I need a location to get the weather!'

    url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q=" + (quote(query)) + "&format=json&num_of_days=1&date=today&key=e4zcjce65nyscwr8jqsj8wwr"
    resp = requests.get(url).content
    print resp
    return resp


def xkcd(query):
    return ''

def image():
    return ''

def help():
    return ''
