import json
import pymongo
from mitmproxy import ctx

client = pymongo.MongoClient('localhost')
db = client['csdn']
collection = db['articles']


def response(flow):
    global collection
    url = 'https://39.96.132.69/cms-app/v2/home_page/psearch'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        art_csdns = data.get('data').get('hits')
        for art_csdn in art_csdns:
            data = {
                "nickname": art_csdn.get('_source').get('nickname'),
                "title": art_csdn.get('_source').get('title'),
                "created_at": art_csdn.get('_source').get('created_at'),
                "view_count": art_csdn.get('_source').get('view_count'),
                "description": art_csdn.get('_source').get('description'),
                "url": art_csdn.get('_source').get('url')
            }
            ctx.log.info(str(data))
            collection.insert(data)
