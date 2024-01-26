import pandas as pd
import numpy as np

def weights(stocks, extra):
    """
    Creates portfolios where each stock is fully weighted in one portfolio, 
    and additional portfolios have random weights.

    Parameters:
    stocks (pandas.DataFrame): DataFrame with stock returns.
    extra (int): Number of additional portfolios with random weights.

    Returns:
    pandas.DataFrame: A DataFrame with portfolio weights for each stock.
    """
    num_stocks = len(stocks.columns)
    total_portfolios = num_stocks + extra
    portfolio_names = [f'P{i+1}' for i in range(total_portfolios)]

    # Initialize DataFrame for weights
    weights_df = pd.DataFrame(index=stocks.columns, columns=portfolio_names)

    # Assign full weight to each stock in one portfolio
    for i, stock in enumerate(stocks.columns):
        weights_df.iloc[:, i] = 0
        weights_df.at[stock, f'P{i+1}'] = 1

    # Assign random weights for the additional portfolios
    for i in range(num_stocks, total_portfolios):
        random_weights = np.random.random(num_stocks)
        normalized_weights = random_weights / random_weights.sum()
        weights_df[f'P{i+1}'] = normalized_weights

    return weights_df


