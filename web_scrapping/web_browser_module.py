import webbrowser
import requests
# webbrowser.open('http://automatetheboringstuff.com')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
