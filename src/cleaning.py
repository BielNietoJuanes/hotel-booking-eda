import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - Handle null values
    - Fix data types
    - Drop unnecessary columns
    - Remove duplicates
    """

    # --- Copy to avoid mutating original df ---
    df = df.copy()

    # --- Basic validation ---
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    # --- Handle missing values ---
    if 'children' in df.columns:
        df['children'] = df['children'].fillna(0)
    
    if 'country' in df.columns:
        df['country'] = df['country'].fillna('Unknown')
    
    # --- Fix data types ---
    if 'is_canceled' in df.columns:
        df['is_canceled'] = df['is_canceled'].astype(bool)

    # --- Drop unnecessary columns ---
    if 'company' in df.columns:
        df = df.drop(columns=['company'])

    # --- Remove duplicates ---
    df = df.drop_duplicates()

    return df
