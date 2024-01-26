import pandas as pd
import numpy as np
import scipy.stats

def correlation(df, method="Pearson", p="F"):
    def format_p_value(p_value):
        formatted = f"{p_value:0.3f}"
        if formatted.startswith("0."):
            return formatted[1:]
        return formatted

    # Filter out non-numeric columns
    numeric_df = df.select_dtypes(include=[np.number])

    if method == "Pearson":
        print("\n\n" + "=" * 21 + f"\n {method} Correlation\n" + "=" * 21)
    else:
        print("\n\n" + "=" * 27 + f"\n {method} Rank Correlation\n" + "=" * 27)

    corr_matrix = pd.DataFrame(index=numeric_df.columns, columns=numeric_df.columns)
    pmatrix = pd.DataFrame(index=numeric_df.columns, columns=numeric_df.columns)

    keys = numeric_df.columns.tolist()

    for i, key1 in enumerate(keys):
        for j, key2 in enumerate(keys):
            if i > j:
                continue

            data1 = numeric_df[key1].dropna()
            data2 = numeric_df[key2].dropna()

            common_index = data1.index.intersection(data2.index)
            data1 = data1.loc[common_index]
            data2 = data2.loc[common_index]

            if len(common_index) < 2:
                corr_matrix.at[key1, key2] = 'nan'
                corr_matrix.at[key2, key1] = 'nan'
                continue

            if method == 'Spearman':
                correlation, p_value = scipy.stats.spearmanr(data1, data2)
            elif method == 'Pearson':
                correlation, p_value = scipy.stats.pearsonr(data1, data2)

            pmatrix.at[key1, key2] = format_p_value(p_value)
            pmatrix.at[key2, key1] = format_p_value(p_value)

            stars = "     "
            if p_value < 0.001:
                stars = " *** "
            elif p_value < 0.01:
                stars = " **  "
            elif p_value < 0.05:
                stars = " *   "               
            elif p_value < 0.1:
                stars = " .   "
                
            correlation_str = f"{format_p_value(correlation)}{stars}"
            corr_matrix.at[key1, key2] = correlation_str
            corr_matrix.at[key2, key1] = correlation_str

    corr_matrix_str = corr_matrix.to_string(sparsify=True, justify='center')
    explanation = "\n\n--\nSignif. codes:  0.001 '***', 0.01 '**', 0.05 '*', 0.1 '.'"

    print("\n\n>> Correlation Matrix <<\n")
    print(corr_matrix_str + explanation)

    if p == "T":
        print("\n\n>> P-Value Matrix <<\n")
        print(pmatrix)
    elif p == "F":
        print("")

    print("\n")  # Newline character at the end of the entire analysis



