import urllib.request

response = urllib.request.urlopen('http://www.yahoo.com')
html = response.read()

if __name__=="__main__":

  print(html)
