import requests,time,os,random,json
cwd = os.getcwd()
from bs4 import BeautifulSoup
import logging
logging.getLogger("requests").setLevel(logging.WARNING)
s = requests.Session()

#example: https://ibox.co.id/product/apple-watch-ultra-with-alpine-loop-ibox

header= {
    'authority': 'ibox.co.id',                                                                                                                                                       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'referer': 'https://ibox.co.id/product/apple-iphone-11-new-package',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

def main():
    print(f"[*] [{time.strftime('%d-%m-%y %X')}] iBox Stock Checker!")
    url = input(f"[*] [{time.strftime('%d-%m-%y %X')}] Input URL: ")
    while True:
        try:
            s.headers.update(header)
            r = s.get(url,headers=header)
            get_datass = json.loads(r.text.split('<script id="__NEXT_DATA__" type="application/json">')[1].split('</script><script nomodule=""')[0])
            get_stock = get_datass['props']['pageProps']['dataProduct']['stock_status']
            title = get_datass['props']['pageProps']['dataProduct']['name']
            print(f"[*] [{time.strftime('%d-%m-%y %X')}] {title} | Stock: {get_stock}")
            if int(get_stock) > 0:
                try:print(f"{title} | Stock: {get_stock} | {url} ")
                except:
                    pass
        except:
            pass

main()
