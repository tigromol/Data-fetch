from datetime import datetime
from iexfinance.stocks import get_historical_intraday

date = datetime(2010, 11, 27)

print(len(get_historical_intraday("DJD", date)))