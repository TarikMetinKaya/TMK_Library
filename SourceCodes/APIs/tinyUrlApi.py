import requests

def urlShortener(URL,tinyUrlApiToken):
    try:
        url_main = f'https://api.tinyurl.com/create?api_token={tinyUrlApiToken}'
        myobj = {
          "url": URL,
          "domain": "tiny.one",
        }

        x = requests.post(url_main, data = myobj).json()

        return x['data']['tiny_url']
    except Exception as e:
        print(e)
        return URL
