from yfinance import Ticker
from datetime import datetime, timedelta

NASDAQ_STOCKS_LIST = ["AAPL","ADBE", "ADI", "ADP", "ADSK","ALGN", "ALXN", "AMAT", "AMD", "AMGN","AMZN", "ANSS", "ASML",
        "ATVI", "AVGO", "BIDU", "BIIB", "BKNG", "BMRN", "CDNS", "CDW", "CERN","CHKP", "CHTR", "CMCSA", "COST", "CPRT",
        "CSCO", "CSX", "CTAS","CTSH", "CTXS", "DLTR", "DOCU", "DXCM", "EA", "EBAY", "EXC", "EXPE","FAST", "FB", "FISV",
        "FOX", "FOXA","GILD", "GOOG", "GOOGL", "IDXX", "ILMN", "INCY", "INTC", "INTU", "ISRG", "JD", "KDP", "KHC",
        "KLAC","LBTYA", "LBTYK", "LRCX", "LULU", "MAR", "MCHP","MDLZ", "MELI", "MNST", "MRNA", "MSFT", "MU",
        "MXIM","NFLX", "NTES", "NVDA", "NXPI", "ORLY", "PAYX", "PCAR", "PDD", "PEP", "PYPL","QCOM", "REGN", "ROST",
        "SBUX", "SGEN", "SIRI", "SNPS", "SPLK", "SWKS", "TCOM", "TMUS", "TSLA", "TTWO", "TXN", "ULTA", "VRSK", "VRSN",
        "VRTX", "WBA", "WDAY", "XEL", "XLNX", "ZM"]


def get_diff_year(stock: Ticker, date:datetime, interval:str ="1d"):
    history = stock.history(start=date, interval=interval)
    year_ago = history.loc[history.index[0]].at["Open"]
    now = history.loc[history.index[-1]].at["Open"]
    return (now - year_ago) / year_ago * 100


def get_diff_days_back(stock: Ticker, days_back: int, interval:str ="1d"):
    days_back_datetime = datetime.now() - timedelta(days=days_back)
    return get_diff_year(stock, days_back_datetime, interval)

    
