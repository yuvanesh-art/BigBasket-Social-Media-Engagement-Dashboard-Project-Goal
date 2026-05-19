def analyze_engagement(df):

    total_likes = df['Likes'].sum()

    total_comments = df['Comments'].sum()

    total_shares = df['Shares'].sum()

    print("Total Likes:", total_likes)

    print("Total Comments:", total_comments)

    print("Total Shares:", total_shares)
