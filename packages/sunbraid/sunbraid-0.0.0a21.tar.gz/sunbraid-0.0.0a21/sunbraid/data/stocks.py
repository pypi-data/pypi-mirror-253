
def get_sp500(days=30, sectors=None):
    """
    Get the S&P 500 data for the last `days` days.
    
    Parameters
    ----------
    days: int
        Number of days to be included in the list.

    sector: list[str]
        Sectors include: [Industrials, Financials, Health Care, Materials,
        Information Technology, Consumer Discretionary, Consumer Staples, 
        Real Estate, Utilities,  Energy, Communication Services ]
        See full list in https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

    """
    
    import yfinance as yf
    from datetime import datetime, timedelta
    import pandas as pd
    import requests

    # Automatic parameters
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=days)).strftime('%Y-%m-%d')


    # Load Data
    def get_sp500_list():
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
        html = requests.get(url).text
        df = pd.read_html(html, header=0)[0]
        return df[['Symbol', 'Security', 'GICS Sector', 'GICS Sub-Industry', 'Headquarters Location']]

    sp500_companies = get_sp500_list()
    if sectors is not None:
        if type(sectors)==str:
            sectors = [sectors]
        sp500_companies = sp500_companies[sp500_companies['GICS Sector'].isin(sectors)]


    # Create an empty DataFrame to store all data
    all_data = pd.DataFrame()

    for symbol in sp500_companies['Symbol']:
        try:
            stock_data = yf.download(symbol, start=start_date, end=end_date, progress=False).reset_index()
            ticker = yf.Ticker(symbol)

            # Fetch metadata
            metadata = yf.Ticker(symbol).info
            for key in ['industry', 'sector', 'longName', 'totalDebt', 'longBusinessSummary', 'targetMedianPrice','recommendationMean', 'recommendationKey', 'numberOfAnalystOpinions', 'sharesOutstanding']:
                stock_data[key] = metadata.get(key)
            
            stock_data['Market Cap'] = stock_data['Close'] * stock_data['sharesOutstanding']
            stock_data['Symbol'] = symbol
            # Append to the main DataFrame
            all_data = pd.concat([all_data, stock_data], ignore_index=True)
        except Exception as e:
            print(f"Error fetching data for symbol {symbol}: {e}")
    return all_data
