import bs4, requests

res = requests.get('https://www.amazon.in/')
print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, 'html.parser')