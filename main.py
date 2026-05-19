# ============================================
# BigBasket Social Media Engagement Dashboard
# Main File
# ============================================

# Import Functions
from src.data_collection import load_data

from src.data_cleaning import clean_data

from src.engagement_analysis import analyze_engagement

from src.visualization import create_chart

# ============================================
# STEP 1 — Load Dataset
# ============================================

print("Loading Dataset...")

df = load_data()

print("Dataset Loaded Successfully!")

# ============================================
# STEP 2 — Clean Dataset
# ============================================

print("\nCleaning Dataset...")

df = clean_data(df)

print("Data Cleaning Completed!")

# ============================================
# STEP 3 — Create Engagement Rate
# ============================================

print("\nCalculating Engagement Rate...")

df['Engagement_Rate'] = (
    (
        df['Likes'] +
        df['Comments'] +
        df['Shares']
    ) / df['Reach']
) * 100

print("Engagement Rate Added!")

# ============================================
# STEP 4 — Analyze Engagement
# ============================================

print("\nRunning Engagement Analysis...")

analyze_engagement(df)

# ============================================
# STEP 5 — Generate Visualization
# ============================================

print("\nGenerating Charts...")

create_chart(df)

# ============================================
# STEP 6 — Save Processed Dataset
# ============================================

df.to_csv(
    'data/processed/processed_social_data.csv',
    index=False
)

print("\nProcessed Dataset Saved!")

# ============================================
# STEP 7 — Dashboard Insights
# ============================================

top_platform = df.groupby(
    'Platform'
)['Likes'].sum().idxmax()

print("\n========== DASHBOARD INSIGHTS ==========")

print(f"Top Platform: {top_platform}")

best_content = df.groupby(
    'Content_Type'
)['Engagement_Rate'].mean().idxmax()

print(f"Best Content Type: {best_content}")

average_engagement = round(
    df['Engagement_Rate'].mean(),
    2
)

print(
    f"Average Engagement Rate: "
    f"{average_engagement}%"
)

print("========================================")

# ============================================
# END OF PROJECT
# ============================================

print(
    "\nBigBasket Dashboard Generated Successfully!"
)
