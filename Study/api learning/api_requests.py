import requests
# get to get a response from a web page
r = requests.get('https://xkcd.com/353/')
print(r)
# .text to get us a text from a web page
r = requests.get('https://xkcd.com/353/')
print(r.text)
# .content to get a contact from image in bytes
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)
# getting an image through the command
#r = requests.get('https://imgs.xkcd.com/comics/python.png')

#with open('Study/api learning/comic.png', 'wb') as f:
    #f.write(r.content)
# .status_code to check the status code
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.status_code)
# headers to get headers from the web page
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.headers)
# work with httpbin.org 
payload = {
    "page": 2,
    "count": 25
}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
# post method
payload = {
    "username": "peter",
    "password": "testing"
}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
# json response
payload = {
    "username": "peter",
    "password": "testing"
}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.json())