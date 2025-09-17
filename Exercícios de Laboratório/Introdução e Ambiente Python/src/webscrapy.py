import requests

class WebScrapy:
    def __init__(self, urls):
        self.urls = urls  

    def __str__(self):
        txt = ""
        for url in self.urls:
            resposta = requests.get(url)
            html = resposta.text

            start_index = html.find('<title>')
            end_index = html.find('</title>')

            if start_index != -1 and end_index != -1:
                titulo = html[start_index + 7:end_index]
            else:
                titulo = 'Sem titulo'

            txt += f"Titulo: {titulo}\n"
        return txt
