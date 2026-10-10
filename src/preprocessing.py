import pandas as pd

def encoding_columns(df, date=None, time=None, int=None, float=None, category=None):
    
    df[date] = df[date].astype("datetime64[us]")
    
    df[time] = df[time].astype("timedelta64[us]")
    
    for i in int:
        df[i] = pd.to_numeric(df[i], downcast="integer")
        
    for f in float:
        df[f] = pd.to_numeric(df[f], downcast="float")
        
    df[category] = df[category].astype("category")
    
    return df
        