import pandas as pd
import numpy as np

def annualize_metric(metric, periods_per_year):
    """Annualize a daily metric such as return or standard deviation."""
    return metric * np.sqrt(periods_per_year)

def portfolios(weights, returns, period='daily'):
    """
    Calculate the expected return and volatility of portfolios.

    :param weights: DataFrame containing the weights of each stock in each portfolio.
    :param returns: DataFrame containing the returns of each stock.
    :param period: String indicating the time period ('daily', 'weekly', 'monthly', 'yearly').
    :return: DataFrame with portfolio names, expected returns, and volatility.
    """
    periods_per_year = {'daily': 252, 'weekly': 52, 'monthly': 12, 'yearly': 1}
    portfolio_returns = returns.dot(weights)

    # Calculate expected portfolio return and volatility
    expected_return = portfolio_returns.mean() * periods_per_year[period]
    volatility = portfolio_returns.std() * np.sqrt(periods_per_year[period])

    # Create a DataFrame for expected return and volatility
    portfolio_metrics = pd.DataFrame({
        'Portfolio': weights.columns,
        'Expected Returnc (%)': expected_return,
        'Volatility (%)': volatility
    })

    return portfolio_metrics.set_index('Portfolio')

# Example usage:
# Assuming weights_df is your weights DataFrame and returns_df is your returns DataFrame
# portfolios(weights_df, returns_df, 'daily')

