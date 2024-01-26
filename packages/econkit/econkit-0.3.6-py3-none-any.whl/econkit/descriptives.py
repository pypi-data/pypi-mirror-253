import pandas as pd
import numpy as np
from scipy.stats import kurtosis

def descriptives(data):
    all_descriptives = []  # List to store descriptive statistics for each column
    statistics_labels = ["Mean", "Median", "Min", "Max", "St. Deviation", "Quartile Deviation", "Kurtosis Fisher", "Kurtosis Pearson", "Skewness", "Co-efficient of Q.D"]
    
    first_column = True  # Flag to check if it's the first column

    for name in data.columns:
        if pd.api.types.is_numeric_dtype(data[name]):
            column_data = data[name].dropna()

            # Calculate statistics
            statistics_values = [
                round(column_data.mean(), 2), 
                round(column_data.median(), 2),
                round(column_data.min(), 2), 
                round(column_data.max(), 2), 
                round(column_data.std(), 2), 
                round((np.percentile(column_data, 75) - np.percentile(column_data, 25)) / 2, 2),
                round(kurtosis(column_data, fisher=True, nan_policy='omit'), 4),
                round(kurtosis(column_data, fisher=False, nan_policy='omit'), 4),
                round(column_data.skew(), 4),
                round((np.percentile(column_data, 75) - np.percentile(column_data, 25)) / 2 / column_data.median(), 4) if column_data.median() != 0 else 0
            ]

            if first_column:
                # Include 'STATISTICS' labels for the first column
                descriptive_df = pd.DataFrame({'STATISTICS': statistics_labels, name: statistics_values})
                first_column = False
            else:
                # Do not include 'STATISTICS' labels for subsequent columns
                descriptive_df = pd.DataFrame({name: statistics_values})

            # Add the DataFrame of this column to the list
            all_descriptives.append(descriptive_df)

    # Concatenate all DataFrames for a consolidated table
    result_df = pd.concat(all_descriptives, axis=1)
    return result_df

# Example usage:
# result = descriptives(your_dataframe)
# print(result)

