# which-bci-api

Tells you which Blockchain.info API your API code works for.

## Usage

Provide your API code as a command-line argument. Example:

`python which-bci-api.py b6525454-19f2-45c6-af32-8b1a795b2d37`

Sample output:

```
$ python which-bci-api.py b6525454-19f2-45c6-af32-8b1a795b2d37
Your code looks like valid UUID format.
Your API code, b6525454-19f2-45c6-af32-8b1a795b2d37, is a valid Create-Wallet API code.
	Create-Wallet API codes are requested here: https://blockchain.info/api/api_create_code
	Create-Wallet API Documentation can be found here: https://blockchain.info/api/create_wallet
	To request a Receive-Payments API code instead, visit: https://api.blockchain.info/v2/apikey/request/
```

## Requirements

Tested with Python 2.7
