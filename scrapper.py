import requests

r = requests.get('https://www.reddit.com/r/memes/top.json?count=20',
                 headers={'User-agent': 'Reddit bot 0.1'})
data = r.json()
image_urls = [item['data']['url'] for item in data['data']['children']]

print(image_urls)