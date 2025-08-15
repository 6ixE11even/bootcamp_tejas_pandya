# creating statistic summary function
import pandas as pd
def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    summary_df = df.describe()
    return summary_df