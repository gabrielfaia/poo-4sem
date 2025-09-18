from webscrapy import *

urls = [
    "https://www.unisantos.br",
    "https://www.uol.com.br",
]

if __name__ == '__main__':
    ws = WebScrapy(urls)
    print(ws)