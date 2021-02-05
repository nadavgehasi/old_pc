import requests

GRAPHITE_SERVER = 'http://graphite'

REQUEST_URL = f"{GRAPHITE_SERVER}/render/?" + "target=summarize(hosts.{}.{},'1hour','last')&from=-1h&format=json"


def get_from_graphite(server, field):
    try:
        r = requests.get(REQUEST_URL.format(server, field))
        return r.json()[0][u'datapoints'][-1][0]
    except:
        return 0
