import pandas as pd
from src.banks.classes import CDT, CDT_INTERVALS

ID = "BAN100"
REQUEST_URL = "https://www.ban100.com.co/productos/cdt"

try:
    import requests
    session = requests.Session()
    response = session.get(REQUEST_URL)
    # Read tables from the page
    tables = pd.read_html(response.text)

    # Create a empty dataframe 
    df = pd.DataFrame()

    # Only get the first two tables
    for i in range(2):
        table = tables[i] 

        # Delete 0 row
        table.drop("Plazo Días", axis=1, inplace=True)

        # Get the first number of the interval
        table.columns = [str(col.split('-')[0]) if '-' in col else str(col.split(' ')[0]) for col in table.columns]
        
        # Transform the porcentage to float
        table.replace('%', '', regex=True, inplace=True)
        table.replace(',', '', regex=True, inplace=True)
        table = table.astype(float)
        table = table.apply(lambda x: round(x/10000, 4))

        # Bind the tables
        df = pd.concat([df, table], axis=1)
        
    # Select only the columns that are in the CDT_INTERVALS list    
    df = df[CDT_INTERVALS]

    # Transpose the table and convert it to a dictionary
    dic = df.T.to_dict()
    #print(dic)
    cdt = CDT(ID, "CDT", dic)
    cdt.write()

except Exception as e:
    raise Exception("Error in Ban100.py", e)