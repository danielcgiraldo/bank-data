import pandas as pd
from src.banks.classes import CDT, CDT_INTERVALS

ID = "POPULAR"
REQUEST_URL = "https://www.bancopopular.com.co/wps/portal/bancopopular/inicio/informacion-interes/tasas"

try:

    table = pd.read_html(REQUEST_URL)[0]

    table.columns = table.columns.map(lambda x: x[1].split('-')[0])


    # Get initial value 
    table['CDT Desmaterializado Monto en pesos'] = table['CDT Desmaterializado Monto en pesos'].str.split(' ').str[2]

    # Convert money format to float
    table['CDT Desmaterializado Monto en pesos'] = table['CDT Desmaterializado Monto en pesos'].str.replace('.', '')
    table['CDT Desmaterializado Monto en pesos'] = table['CDT Desmaterializado Monto en pesos'].astype(int)


    # Set CDT Desmaterializado Monto en pesos as index
    table.set_index(['CDT Desmaterializado Monto en pesos'], inplace=True) 


    # Convert XX,XX% to float and divide by 100
    table.replace('%', '', regex=True, inplace=True)
    table.replace(',', '.', regex=True, inplace=True)
    table = table.astype(float)
    table = table.apply(lambda x: round(x / 100,4))

    # Remove column that its name is not in the CDT_INTERVALS list
    table = table[CDT_INTERVALS]

    # Transpose table
    table = table.T

    cdt = CDT(ID, table.to_dict())
    cdt.write()

except Exception as e:
    print("Error in popular.py", e)
