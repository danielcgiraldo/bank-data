# Bank Data JSON

![GitHub contributors](https://img.shields.io/github/contributors/danielcgiraldo/bank-data-json)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/danielcgiraldo/bank-data-json/main)
![GitHub issues](https://img.shields.io/github/issues/danielcgiraldo/bank-data-json)

This project aims to provide a JSON file with information related to banks in Colombia. The information is scraped from the banks' websites and stored in a JSON file. The project is open-source and available on GitHub.

## Raw Data

| Description                             | File        | URL                                                                                     |
| :-------------------------------------- | :---------- | :-------------------------------------------------------------------------------------- |
| Bank information        | bank.json   | <https://raw.githubusercontent.com/danielcgiraldo/bank-data-json/main/data/bank.json>   |
| CDT and FIC interest rates (automated)  | data.json   | <https://raw.githubusercontent.com/danielcgiraldo/bank-data-json/main/data/data.json>   |
| Savings account interest rates (manual) | saving.json | <https://raw.githubusercontent.com/danielcgiraldo/bank-data-json/main/data/saving.json> |

## Supported Banks

Obtain the official list of authorized banks in Colombia from [Banco de la República](https://www.banrep.gov.co/es/sistemas-pago/cenit/entidades-autorizadas).

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
