# urllib.request  ->  contains functions for opening and reading URLs

# urllib.request.Request(url, data, headers, origin_req_host, method=None)

from urllib.request import urlopen
obj = urlopen("https://www.tutorialspoint.com/static/images/simply-easy-learning.jpg")
data = obj.read()
img = open("img.jpg", "wb")
img.write(data)
img.close()


# from urllib.request import Request, urlopen
# obj = Request("https://www.tutorialspoint.com/")
# resp = urlopen(obj)
# data = resp.read()
# print (data)
