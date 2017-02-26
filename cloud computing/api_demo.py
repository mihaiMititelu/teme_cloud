import urllib
from urllib import request
from pprint import *

response = urllib.request.urlopen("https://newsapi.org/v1/articles?source=techcrunch&apiKey=7f5a58e4dbd246c6a89d7fb8ff3c44da").read()
pprint(response.decode('utf-8'))
