import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new variables from the original dataset
    """

    # --- Copy to avoid mutating original df ---
    df = df.copy()

    # --- Total nights ---
    df['total_nights'] = (
        df['stays_in_weekend_nights'] + 
        df['stays_in_week_nights']
    )

    # --- Total guests ---
    df['total_guests'] = (
        df['adults'] + 
        df['children'] + 
        df['babies']
    )

    # --- Total revenue ---
    df['total_revenue'] = df['adr'] * df['total_nights']

    # --- Identify the season by month ---
    def get_season(month):
        if month in ['December', 'January', 'February']:
            return 'Winter'
        elif month in ['March', 'April', 'May']:
            return 'Spring'
        elif month in ['June', 'July', 'August']:
            return 'Summer'
        else:
            return 'Fall'
    
    df['season'] = df['arrival_date_month'].apply(get_season)

    return df
