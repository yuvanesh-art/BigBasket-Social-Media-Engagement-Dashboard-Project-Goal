import pandas as pd

def load_data():

    df = pd.read_csv(
        'data/raw/social_media_data.csv'
    )

    return df
