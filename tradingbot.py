from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PKTZTO5YL2CHO1E29GBB"
API_SECRET = "xOopCzPqUETGDj1hCWOORZb5Uf7gAt8X29UTJmVG"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self):
        pass
    def on_trading_iteration(self):
        pass

start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, 
                        parameters={})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters ={}
)