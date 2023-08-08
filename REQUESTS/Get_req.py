import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.headers['content-type']) # Gives type of the content received from the webpage
print(r.encoding)
print(r.text)
print(r.json())
