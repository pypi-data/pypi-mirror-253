import requests, json

class BaseAPI:
    def __init__(self):
        ...

    def json_load(self, file, mode='r', encoding='utf-8', **kwargs):
        with open(file, mode=mode, encoding=encoding, **kwargs) as f:
            data = json.load(f)
        return data

    def json_dump(self, data, file, mode='w+', encoding='utf-8', indent=4, **kwargs):
        with open(file, mode=mode, encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=indent, **kwargs)

    def _get(self, url, data={}):
        jdata = json.dumps(data)
        r = requests.get(url=url, data=jdata)
        return r.json()

    def _post(self, url, data={}):
        # https://developers.weixin.qq.com/community/develop/doc/000024b3058f40fa792e40b2656000
        jdata = json.dumps(data, ensure_ascii=False)
        latin1 = jdata.encode("utf-8").decode('latin1')
        r = requests.post(url=url, data=latin1)
        return r.json()
