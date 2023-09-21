from bs4 import BeautifulSoup
import requests

ID = "DAVIVIENDA"
REQUEST_URL = "https://www.davivienda.com/wps/portal/personas/nuevo"

try:
    
    headers = {
        "Host": "www.davivienda.com",
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    session = requests.Session()
    portal = session.get("https://www.davivienda.com/wps/portal/personas/nuevo", headers=headers)


    portal_soap = BeautifulSoup(portal.text, 'html.parser')

    header = portal_soap.select("header div.aqui-puedo nav.aqui-puedo a:-soup-contains('Inversiones')")[0]

    construir_mi_futuro = session.get("https://www.davivienda.com/wps/portal/personas/nuevo/" + header.get('href'), headers=headers)

    construir_mi_futuro_soap = BeautifulSoup(construir_mi_futuro.text, 'html.parser')

    card = (construir_mi_futuro_soap.select("div.container div#productos div.producto h4:-soup-contains('CDT')")[0].parent.parent)

    cdt = session.get("https://www.davivienda.com/wps/portal/personas/nuevo/personas/aqui_puedo/construir_mi_futuro/inversiones/" + card.select("a")[0].get('data-href'), headers=headers)

    cdt_soap = BeautifulSoup(cdt.text, 'html.parser')

    pdf_link = "https://www.davivienda.com/" + (cdt_soap.select("a:-soup-contains('Ver tasas y tarifas')")[0].get('href'))

    print(pdf_link)


except Exception as e:
    print("Error in davivienda.py", e)
