from datetime import date
from bs4 import BeautifulSoup
import requests
import json

JSON_FILE = "data/indicators.json"

with open(JSON_FILE, 'r') as f:
    current_data = json.load(f)

    # =============== TASA USURA ===============

    REQUEST_URL = "https://www.dian.gov.co/scripts/HEconomics?type=Indicators"

    response = requests.get(REQUEST_URL).json()

    if response["statusMessage"] == "OK":
        TASA_USURA = response["results"][-1]["amount"]
        TASA_USURA = round(float(TASA_USURA.replace("%", "")) / 100, 4)
        current_data["TASA_USURA"] = {
            "last_update": str(date.today()),
            "value": TASA_USURA
        }

    # =============== IBR ===============

    REQUEST_URL = "https://totoro.banrep.gov.co/analytics/saw.dll?Go&NQUser=publico&NQPassword=publico123&Action=prompt&path=%2Fshared%2FSeries%20Estad%C3%ADsticas_T%2F1.%20IBR%2F1.16.IBR_Principal_2&Options=rdf&lang=es"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'host': 'totoro.banrep.gov.co'
    }

    session = requests.Session()

    session.get(REQUEST_URL, headers=headers)

    response = session.get(REQUEST_URL, headers=headers)

    response = session.get(REQUEST_URL, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    soup.css.select("table table.CVTable tr")

    data = soup.css.select("table table.CVTable tr")[0]
    data = data.css.select("table div.PivotContainer table tr")[-1]
    data = data.css.select("table tr td")[2].text

    data = data.replace("%", "")
    IBR = round(float(data.replace(",", ".")) / 100, 5)

    current_data["IBR"] = {
        "last_update": str(date.today()),
        "value": IBR
    }

# =====================================

    # Write new data
    with open(JSON_FILE, 'w') as f:
        json.dump(current_data, f, indent=4)
