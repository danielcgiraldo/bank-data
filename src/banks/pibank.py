import requests
from bs4 import BeautifulSoup
from src.banks.classes import CDT, CDTInterface

ID = "PIBANK"
REQUEST_URL = "https://www.pibank.co/cdt-pibank/"

try:

    response = requests.get(REQUEST_URL)

    soap = BeautifulSoup(response.text, 'html.parser')

    rates = soap.css.select(".hero-product .caja-pastillero span.super-text")

    pibank = CDT(ID, "CDT Pibank")
    m = CDTInterface(100000)
    for rate in rates:
        m.add(rate.find("span").text.split(" ")[0], float(
            rate.text.split(" ")[0].replace("%", "").replace(",", "."))/100)
    pibank.add(m)

    pibank.write()

except Exception as e:
    print("Error in pibank.py", e)
