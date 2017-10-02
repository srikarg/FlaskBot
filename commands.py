from urllib2 import quote
import requests
from flask import Flask, jsonify

def calc(query):
    return str(eval(query))

def xkcd(query):
    url = 'http://xkcd.com/info.0.json'
    ret = requests.get(url).json()['img']
    return '<img src="' + ret + '"/>'
