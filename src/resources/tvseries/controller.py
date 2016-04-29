import json

import falcon
from bs4 import BeautifulSoup
import requests

class TorrentController:

    def on_get(self, request, response, **kwargs):
        scrape_url = 'https://eztv.ag/search/%s' % (kwargs.get('show'))
        page = requests.get(scrape_url)
        soup = BeautifulSoup(page.content)

        torrent_array = []

        for item in soup.findAll('tr', class_='forum_header_border'):
            inner_item = item.findAll(class_='forum_thread_post')
            name = inner_item[1].text
            torrent_array.append({
                'name': name.replace('\n', ''),
                'links': [item['href'] for item in inner_item[2].findAll('a')],
                'size': inner_item[3].text
            })

        response.body = json.dumps({
            'title': soup.title.string.replace('\n', ''),
            'torrents': torrent_array
        })

        response.status = falcon.HTTP_200


torrent = TorrentController()
