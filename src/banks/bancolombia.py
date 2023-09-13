import pandas as pd
from banks.classes import CDT

ID = "BANCOL"
REQUEST_URL = "https://www.bancolombia.com/personas/productos-servicios/inversiones/inversion-virtual"

try:

    table = pd.read_html(REQUEST_URL)[0]

    """
    Parse Monto/Plazo
    """

    # Check if last row has "Mayor a [number]" and remove "Mayor a"
    if table['Monto/Plazo'].str.contains('Mayor a').any():
        table['Monto/Plazo'] = table['Monto/Plazo'].str.replace('Mayor a ', '')

    # Remove all after first number
    table['Monto/Plazo'] = table['Monto/Plazo'].str.split(' ').str[0]

    # Convert money format to float
    table['Monto/Plazo'] = table['Monto/Plazo'].str.replace('$', '')
    table['Monto/Plazo'] = table['Monto/Plazo'].str.replace('.', '')
    table['Monto/Plazo'] = table['Monto/Plazo'].str.replace(',', '.')
    table['Monto/Plazo'] = table['Monto/Plazo'].astype(int)

    # Monto/Plazo to be used as index
    table.set_index(['Monto/Plazo'], inplace=True)

    """
    Parse Column names
    """

    # Remove "días" from column names
    table.columns = table.columns.str.replace('días', '')

    # Keep only first number from days range
    table.columns = table.columns.str.split('-').str[0]

    # Column names as int
    table.columns = table.columns.astype(int)

    """
    Parse Cells
    """

    # Convert XX,XX% to float and divide by 100
    table.replace('%', '', regex=True, inplace=True)
    table = table.astype(float)
    table = table.apply(lambda x: round(x / 100,4))

    # Invert table
    table = table.T

    cdt = CDT(ID, table.to_dict())
    cdt.write()
    
except:
    print("Error in bancolombia.py")
