import pandas as pd
import inspect

def table(column_name, *dataframes):
    """
    Creates a DataFrame by combining a specified column from multiple DataFrames.
    
    Parameters:
    column_name: str
        The name of the column to be extracted from each DataFrame.
    dataframes: variable number of pandas.DataFrame
        DataFrames from which the specified column will be extracted.
    
    Returns:
    pandas.DataFrame
        A new DataFrame with the specified column from each of the provided DataFrames.
    """
    if not dataframes:
        raise ValueError("No dataframes provided")

    # Inspect the calling frame to try to get DataFrame variable names
    frame = inspect.currentframe()
    try:
        df_names = []
        for df in dataframes:
            for var_name, var_val in frame.f_back.f_locals.items():
                if var_val is df:
                    df_names.append(var_name)
                    break
            else:
                df_names.append("UnnamedDataFrame")
    finally:
        del frame

    # Create an empty DataFrame
    combined_df = pd.DataFrame()

    # Loop through each DataFrame and its inferred name
    for df, name in zip(dataframes, df_names):
        if column_name in df.columns:
            combined_df[name] = df[column_name]
        else:
            # If the column is not in a DataFrame, insert missing values
            combined_df[name] = pd.NA

    return round(combined_df,2)
