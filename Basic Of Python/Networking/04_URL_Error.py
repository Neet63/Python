# urllib.error  ->  carries definitions of the exceptions raised by urllib.request

from urllib.request import Request, urlopen
import urllib.error as err

obj = Request("http://www.nosuchserver.com")
try:
   urlopen(obj)
except err.URLError as e:
   print(e)