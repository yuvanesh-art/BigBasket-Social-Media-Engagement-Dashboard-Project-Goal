from src.data_collection import load_data

from src.data_cleaning import clean_data

from src.engagement_analysis import analyze_engagement

df = load_data()

df = clean_data(df)

analyze_engagement(df)
