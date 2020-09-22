from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

with urllib.request.urlopen('https://canvas.dongseo.ac.kr/') as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

print(html)