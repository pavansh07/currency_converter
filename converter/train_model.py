import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

# Load historical data
data = pd.read_csv('historical_exchange_rates.csv', parse_dates=['date'], index_col='date')

# Assume we're predicting USD to INR exchange rate
usd_to_inr = data['USD_INR']

# Fit ARIMA model
model = ARIMA(usd_to_inr, order=(5, 1, 0))
model_fit = model.fit()

# Save the model
with open('arima_model.pkl', 'wb') as f:
    pickle.dump(model_fit, f)
