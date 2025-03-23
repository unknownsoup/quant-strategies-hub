import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = os.getenv('APCA_API_KEY_ID')
SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Get our account information.
account = trading_client.get_account()

print('${} is available as buying power.'.format(account.buying_power))