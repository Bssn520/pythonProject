import urllib
import urllib.request

data={}
data['word']="菜鸟教程"

url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values

data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)
