import matplotlib.pyplot as plt

def create_chart(df):

    platform_analysis = df.groupby(
        'Platform'
    )['Likes'].sum()

    platform_analysis.plot(kind='bar')

    plt.title(
        'Platform-wise Likes'
    )

    plt.show()
