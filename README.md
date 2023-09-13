# Bank Data JSON

## Raw Data

| Description                             | File        | URL                                                                                     |
| :-------------------------------------- | :---------- | :-------------------------------------------------------------------------------------- |
| Information of related to a Bank ID     | bank.json   | <https://raw.githubusercontent.com/danielcgiraldo/bank-data-json/main/data/bank.json>   |
| CDT and FIC interest rates (automatic)  | data.json   | <https://raw.githubusercontent.com/danielcgiraldo/bank-data-json/main/data/data.json>   |
| Saving Accounts interest rates (manual) | saving.json | <https://raw.githubusercontent.com/danielcgiraldo/bank-data-json/main/data/saving.json> |

## Supported Banks

### CDTs

| Name            | ID        | Source                                                                                     |
| :-------------- | :-------- | :----------------------------------------------------------------------------------------- |
| Bancolombia     | BANCOL    | <https://www.bancolombia.com/personas/productos-servicios/inversiones/inversion-virtual>   |
| Banco Finandina | FINANDINA | <https://www.bancofinandina.com/servicio-al-cliente/tasas-y-tarifas/tasas-vigentes/>       |
| Banco Pibank    | PIBANK    | <https://www.pibank.co/cdt-pibank/>                                                        |
| Banco Popular   | POPULAR   | <https://www.bancopopular.com.co/wps/portal/bancopopular/inicio/informacion-interes/tasas> |

### FICs

#### Bancolombia

| Name       | Source                                                                                                       |
| :--------- | :----------------------------------------------------------------------------------------------------------- |
| Fiducuenta | <https://www.bancolombia.com/personas/productos-servicios/inversiones/fondos-inversion-colectiva/fiducuenta> |
| Fidurenta  | <https://www.bancolombia.com/personas/productos-servicios/inversiones/fondos-inversion-colectiva/fidurenta>  |

## Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── src/
│   ├── __init__.py
│   └── banks/
│       └── <bank-name>.py
├── data/
├── .gitignore
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md

```

## Contributing

If you want to contribute to this project, please read the [CONTRIBUTING](CONTRIBUTING.md) file.

## Disclaimer

This project is entirely independent and has no affiliation, association, authorization, endorsement, or official connection with any of the banks mentioned above, or any of their subsidiaries or affiliates. All names of banks, as well as any related names, marks, emblems, and images, are registered trademarks of their respective owners.

The information provided on this platform, including details about Certificate of Deposit (CD) interest rates, loans, savings accounts, and related financial data, is strictly for educational purposes. It should not be considered as personalized investment advice. It is highly advisable to consult with a licensed financial advisor or directly with the respective bank before making any financial decisions, including investments in CDs, loans, or savings accounts. None of the information listed should be interpreted as an offer to buy or sell securities.
