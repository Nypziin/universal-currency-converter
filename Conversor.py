import requests
import xml.etree.ElementTree as ET


class Conversor:
    def __init__(self, valor, moeda_inicial, moeda_final):
        self.valor = valor
        self.moeda_inicial = moeda_inicial
        self.moeda_final = moeda_final

    def verificar_moeda(self):
        xml_content = requests.get('https://economia.awesomeapi.com.br/xml/available/uniq').text
        tags = ET.fromstring(xml_content)

        status_moeda_inicial = False
        status_moeda_final = False

        for tag in tags:
            if self.moeda_inicial == tag.tag:
                status_moeda_inicial = True
            elif self.moeda_final == tag.tag:
                status_moeda_final = True

        return status_moeda_inicial, status_moeda_final

    def converter(self):
        dados_request = requests.get(f'https://economia.awesomeapi.com.br/json/last/{self.moeda_inicial}-{self.moeda_final}')
        bid = dados_request.json()
        return f"{self.valor} {self.moeda_inicial} = {float(bid[f'{self.moeda_inicial}{self.moeda_final}']['bid']) * self.valor} {self.moeda_final}"


Conversor(10, 'USD', 'BRL').converter()





