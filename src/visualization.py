import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_videos(df):

    top_videos = df.sort_values(
        by="Views",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12,6))

    sns.barplot(
        x="Views",
        y="Title",
        data=top_videos
    )

    plt.title("Top 10 Most Viewed Videos")

    plt.show()

def correlation_heatmap(df):

    import matplotlib.pyplot as plt
    import seaborn as sns

    correlation = df[
        ["Views", "Likes", "Comments"]
    ].corr()

    plt.figure(figsize=(8,5))

    sns.heatmap(
        correlation,
        annot=True
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/correlation_heatmap.png"
    )

    plt.close()

import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs/charts", exist_ok=True)

def generate_graphs(df):

    # Top videos
    top_videos = df.sort_values(
        by="Views",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12,6))

    sns.barplot(
        x="Views",
        y="Title",
        data=top_videos
    )

    plt.title("Top 10 Videos")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/top_videos.png"
    )

    plt.close()

    # Upload trends
    uploads = (
        df.groupby(
            df["Published_Date"].dt.to_period("M")
        ).size()
    )

    uploads.index = uploads.index.astype(str)

    plt.figure(figsize=(12,6))

    uploads.plot()

    plt.title("Upload Trends")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/upload_trends.png"
    )

    plt.close()