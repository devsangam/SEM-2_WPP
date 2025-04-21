import pandas as pd
asking_prices = pd.Series([5000, 7000, 12000, 15000, 3000])
fair_prices = pd.Series([5500, 7500, 11000, 18000, 3500])
good_deals = asking_prices[asking_prices < fair_prices].index.tolist()
print("Indices of good deals:", good_deals)