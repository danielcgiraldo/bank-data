# Contributing to the Project

Thank you for considering contributing to our project! We welcome contributions from the community to help improve and expand the bank information database. There are several ways you can contribute to this project:

## 1. Adding Support for More Banks

To add support for a new bank, follow these steps:

1. Create a Python file inside the src/banks directory with the code used to scrap the information.
2. Ensure the Python file follows this structure:

    ```python
     ID = "<bank-id>"
     REQUEST_URL = "<scrapped-url>"
    ```

3. Use the classes defined in `src/banks/classes` to ensure consistency in data processing and JSON file generation.
4. Don't forget to add the new bank to the project's README and update the `data/banks.json` file to include the bank's information.

## 2. Verify, Add, or Update Savings Account Information

You can help by verifying, adding, or updating information related to savings accounts and their interest rates. This information is stored in the `data/saving.json` file. Please ensure that the data is accurate and up-to-date.

## 3. Review and Report Issues

You can contribute by reviewing the existing data and verifying its authenticity. If you find any inaccuracies or issues with the project, please raise them as GitHub issues. Reporting issues helps us improve the quality of the project.
