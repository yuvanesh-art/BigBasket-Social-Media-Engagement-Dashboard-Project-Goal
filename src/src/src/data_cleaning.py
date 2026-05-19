def clean_data(df):

    # Remove Missing Values
    df.dropna(inplace=True)

    # Remove Duplicate Rows
    df.drop_duplicates(inplace=True)

    return df
