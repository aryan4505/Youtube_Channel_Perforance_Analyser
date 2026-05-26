import os

os.makedirs("outputs/reports", exist_ok=True)

def create_report(df):

    report = f"""
YouTube Analysis Report
=======================

Total Videos:
{len(df)}

Average Views:
{df['Views'].mean()}

Average Likes:
{df['Likes'].mean()}

Most Viewed Video:
{df.loc[df['Views'].idxmax()]['Title']}
"""

    with open(
        "outputs/reports/report.txt",
        "w"
    ) as file:

        file.write(report)