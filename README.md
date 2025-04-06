# MyFubonAPI
MyFubonAPI

## Taiwan Stock Information Parser

This project is a Python script that interacts with the Fubon API to provide account information, query inventories, retrieve historical data, and query accounting information.

## Prerequisites

- Python 3.6+ (Your current version is 3.12.9)
- Required Python libraries:
    - `requests`
    - `fubon_neo` (install with `pip install -r requirements.txt`)

## Usage

1.  Clone this repository.
2.  Install the dependencies using `pip install -r requirements.txt`.
3.  Run the `main.py` script with the desired arguments:

    *   To display account information: `python main.py --account`
    *   To query inventories: `python main.py --inventory`
    *   To query historical candle data: `python main.py --historical_candles <SYMBOL> <FROM_DATE> <TO_DATE>`
        *   Replace `<SYMBOL>` with the stock symbol (e.g., 2330).
        *   Replace `<FROM_DATE>` with the start date (e.g., 2024-01-01).
        *   Replace `<TO_DATE>` with the end date (e.g., 2024-01-31).
    *   To query historical stats data: `python main.py --historical_stats <SYMBOL>`
        *   Replace `<SYMBOL>` with the stock symbol (e.g., 2330).
    *   To query unrealized gains and losses: `python main.py --unrealized`
    *   To query realized gains and losses: `python main.py --realized`
    *   To query bank balance: `python main.py --bank`

4.  The script will prompt you to enter your Fubon API credentials (account, password, certificate path, and certificate password).
    *   **Important:** Replace the placeholder credentials in `main.py` with your actual credentials.

## Disclaimer

This script is for informational and testing purposes only. It is not intended for production use. The data is sourced from the Fubon API. Use it at your own risk.
Replace the placeholder credentials with your actual credentials.
Ensure the certificate file path is correct.
Be aware of the potential risks associated with trading stocks and the Fubon API.
</file_content>

Now that you have the latest state of the file, try the operation again with fewer/more precise SEARCH blocks.
(If you run into this error 3 times in a row, you may use the write_to_file tool as a fallback. Keep in mind, the write_to_file fallback is far from ideal, as this means you'll be re-writing the entire contents of the file just to make a few edits, which takes time and money. So let's bias towards using replace_in_file as effectively as possible)
</error>
The user denied this operation.
The user provided the following feedback:
run with bank flag
</feedback>
The user wants me to run the `bank` flag. I will execute the command `python main.py --bank`.
```tool_code
<execute_command>
<command>python main.py --bank</command>
<requires_approval>false</requires_approval>
</execute_command>
```
# Taiwan Stock Information Parser

This project is a Python script that interacts with the Fubon API to provide account information, query inventories, and retrieve historical data.

## Prerequisites

- Python 3.6+ (Your current version is 3.12.9)
- Required Python libraries:
    - `requests`
    - `fubon_neo` (install with `pip install -r requirements.txt`)

## Usage

1.  Clone this repository.
2.  Install the dependencies using `pip install -r requirements.txt`. This will install the `requests` and `fubon_neo` libraries.
3.  Run the `main.py` script with the desired arguments:

    *   To display account information: `python main.py --account`
    *   To query inventories: `python main.py --inventory`
    *   To query historical candle data: `python main.py --historical_candles <SYMBOL> <FROM_DATE> <TO_DATE>`

        *   Replace `<SYMBOL>` with the stock symbol (e.g., 2330).
        *   Replace `<FROM_DATE>` with the start date (e.g., 2024-01-01).
        *   Replace `<TO_DATE>` with the end date (e.g., 2024-01-31).
    *   To query historical stats data: `python main.py --historical_stats <SYMBOL>`

        *   Replace `<SYMBOL>` with the stock symbol (e.g., 2330).

4.  The script will prompt you to enter your Fubon API credentials (account, password, certificate path, and certificate password).
    *   **Important:** Replace the placeholder credentials in `main.py` with your actual credentials.

## Disclaimer

This script is for informational and testing purposes only. It is not intended for production use. The data is sourced from the Fubon API. Use it at your own risk.
Replace the placeholder credentials with your actual credentials.
Ensure the certificate file path is correct.
Be aware of the potential risks associated with trading stocks and the Fubon API.
