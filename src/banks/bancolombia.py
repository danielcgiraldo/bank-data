import pandas as pd
import requests
from banks.classes import CDT, FIC, FICInterface, CDT_INTERVALS

ID = "BANCOL"
REQUEST_URL = "https://www.bancolombia.com/personas/productos-servicios/inversiones/inversion-virtual"

API_FIC = "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"
FICs = ["800180687", "800244627"]


def get_cdt():
    try:
        table = pd.read_html(REQUEST_URL)[0]

        """
        Parse Monto/Plazo
        """

        # Check if last row has "Mayor a [number]" and remove "Mayor a"
        if table['Monto/Plazo'].str.contains('Mayor a').any():
            table['Monto/Plazo'] = table['Monto/Plazo'].str.replace(
                'Mayor a ', '')

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


        # Remove column that its name is not in the CDT_INTERVALS list
        table = table[CDT_INTERVALS]

        """
        Parse Cells
        """

        # Convert XX,XX% to float and divide by 100
        table.replace('%', '', regex=True, inplace=True)
        table = table.astype(float)
        table = table.apply(lambda x: round(x / 100, 4))

        # Invert table
        table = table.T

        cdt = CDT(ID, table.to_dict())
        cdt.write()

    except Exception as e:
        print("Error in bancolombia.py CDT", e)


def get_fic():
    try:
        f = FIC(ID)
        for fic in FICs:
            response = requests.get(API_FIC + fic)
            data = response.json()
            fi = FICInterface(data["nombre"])
            fi.add("semanal", data["rentabilidad"]["dias"]["semanal"])
            fi.add("mensual", data["rentabilidad"]["dias"]["mensual"])
            fi.add("semestral", data["rentabilidad"]["dias"]["semestral"])
            fi.add("anioCorrido", data["rentabilidad"]["anios"]["anioCorrido"])
            fi.add("ultimoAnio", data["rentabilidad"]["anios"]["ultimoAnio"])
            f.add(fi)

        f.write()

    except Exception as e:
        print("Error in bancolombia.py FIC", e)


try:
    # CDT
    get_cdt()

    # Fondo de Inversion
    get_fic()


except:
    print("Error in bancolombia.py")
