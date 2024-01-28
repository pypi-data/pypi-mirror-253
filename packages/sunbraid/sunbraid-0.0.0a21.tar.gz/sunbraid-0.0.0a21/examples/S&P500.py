#%% Imports
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import requests
import matplotlib.pyplot as plt
import sunbraid as sun
from sunbraid.inline.line import lineplot
from sunbraid.head import render_page
from IPython.display import HTML
%load_ext autoreload
%autoreload 2

#%% Parameters
# Manual parameters
period_size = 30 # Days

# Automatic parameters
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=period_size)).strftime('%Y-%m-%d')

#%% Load Data
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import requests

def get_sp500_list():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = requests.get(url).text
    df = pd.read_html(html, header=0)[0]
    return df[['Symbol', 'Security', 'GICS Sector', 'GICS Sub-Industry', 'Headquarters Location']]

sp500_companies = get_sp500_list()
# Create an empty DataFrame to store all data
all_data = pd.DataFrame()

for symbol in sp500_companies['Symbol'].iloc[:30]:
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
all_data.head()

# %%

def post_fig(data, fig, ax):
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.ylim(data['Close'].min()*0.9, data['Close'].max()*1.1)

page = (
    render_page(
        lineplot(all_data, level=['Symbol'], 
        x='Date', y='Close', post_fig=post_fig,
        classes= 'magnifiable'
    ).style.set_table_attributes('class="table"').to_html(), 'save', 'SP500.html'
    )
)

# %%

# %%
