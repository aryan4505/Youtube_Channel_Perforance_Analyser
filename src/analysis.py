def add_engagement_metrics(df):

    df["Engagement_Rate"] = (
        (df["Likes"] + df["Comments"])
        / df["Views"]
    ) * 100

    df["Upload_Month"] = (
        df["Published_Date"].dt.month_name()
    )

    df["Upload_Day"] = (
        df["Published_Date"].dt.day_name()
    )

    return df

def upload_trend_analysis(df):

    monthly_uploads = (
        df.groupby(
            df["Published_Date"].dt.to_period("M")
        ).size()
    )

    return monthly_uploads