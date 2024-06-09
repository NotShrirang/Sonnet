import bs4
import requests

def get_image_src(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    imgs = soup.findAll('img')
    imgs = [img['src2'] for img in imgs if 'src2' in img.attrs]
    final_url = imgs[0].replace("w=42&h=42&", "w=1920&h=1080&")
    return final_url