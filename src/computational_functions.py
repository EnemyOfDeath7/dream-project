import pandas as pd
import numpy as np

def calc_sleep_hours(df):
    diff = df["wake_up"] - df["fall_asleep"]
    mask = diff < pd.Timedelta(0)
    diff.loc[mask] += pd.Timedelta(days=1)

    df["sleep_duration"] = diff
    df["sleep_hours"] = diff.dt.total_seconds() / 3600
    
    return df
        
def calc_num_cols(df):
    num_cols = df.select_dtypes(include=[np.number], exclude=[np.timedelta64])
    num_cols = num_cols.drop("participant_id", axis=1)
    
    return num_cols