import uuid


class Codec:
    def __init__(self):
        self.urlMap = {}

    def encode(self, longUrl):
        id = uuid.uuid4()
        self.urlMap[id] = longUrl
        return "http://tinyurl.com" + '/' + id

    def decode(self, shortUrl):
        id = shortUrl.split('/')[-1]
        return self.urlMap[id]
