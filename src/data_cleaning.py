import pandas as pd

def clean_video_data(df):

    numeric_cols = ["Views", "Likes", "Comments"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col])

    df["Published_Date"] = pd.to_datetime(
        df["Published_Date"]
    )

    return df

def save_data(df, path):

    df.to_csv(path, index=False)

    print("Data Saved Successfully")


import pandas as pd

def clean_data(df):

    numeric_cols = [
        "Views",
        "Likes",
        "Comments"
    ]

    for col in numeric_cols:

        df[col] = pd.to_numeric(df[col])

    df["Published_Date"] = pd.to_datetime(
        df["Published_Date"]
    )

    df["Engagement_Rate"] = (
        (df["Likes"] + df["Comments"])
        / df["Views"]
    ) * 100

    return df

def save_csv(df):

    df.to_csv(
        "outputs/reports/channel_analysis.csv",
        index=False
    )

    print("CSV File Saved")