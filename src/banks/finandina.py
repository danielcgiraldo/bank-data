import pandas as pd
from src.banks.classes import CDT
import re

ID = "FINANDINA"
REQUEST_URL = "https://www.bancofinandina.com/servicio-al-cliente/tasas-y-tarifas/tasas-vigentes/"

try:

    import requests

    session = requests.Session()

    headers = {
        'Host': 'www.bancofinandina.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    }

    response = session.get(REQUEST_URL, headers=headers)

    if response.status_code == 403:

        # Use cookies generated in the previous request
        response = session.get(REQUEST_URL, headers=headers)

        if response.status_code != 200:
            raise Exception("Access is forbidden to Finandina Webpage.")

    table = pd.read_html(response.text)[0]

    # Delete 0 row
    table = table.drop(0)

    # Delete last column
    table = table.drop(table.columns[-1], axis=1)

    table.columns = ["Days", int(table.columns[1][1].split(" ")[1].replace("$", "").replace(".", ""))]

    pattern = r'Mayor a (\d{3}) días'

    def replace_match(match):
        return f'días {match.group(1)}'

    table['Days'] = table['Days'].str.replace(pattern, replace_match, regex=True)

    # Set only first number from days range
    table["Days"] = table['Days'].str.split(' ').str[1]

    # Set days as index
    table.set_index(["Days"], inplace=True)

    # Convert XX,XX% to float and divide by 100
    table.replace('%', '', regex=True, inplace=True)
    table = table.astype(float)
    table = table.apply(lambda x: round(x / 100,4))

    table.columns = table.columns.astype(int)

    cdt = CDT(ID, "CDT digital", table.to_dict())
    cdt.write()

except Exception as e:
    print("Error in finandina.py", e)
