import pandas as pd
from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import (
    plot_cancellations,
    plot_lead_time_vs_cancel,
    plot_adr_by_hotel,
    plot_revenue_by_segment
)

def main():
    df = load_csv(RAW_PATH)
    df = clean(df)
    df = build_features(df)
    # assert_columns(df, ['column_1', 'column_2'])

    # --- Visualizations ---
    plot_cancellations(df)
    plot_lead_time_vs_cancel(df)
    plot_adr_by_hotel(df)
    plot_revenue_by_segment(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")

def main():
    print("🚀 Starting pipeline...")

    # Load
    print("📥 Loading data...")
    df = pd.read_csv(RAW_PATH)
    print(f"Data shape: {df.shape}")

    # Validation
    print("🔍 Validating columns...")

    required_columns = [
        'hotel',
        'is_canceled',
        'lead_time',
        'adr',
        'stays_in_weekend_nights',
        'stays_in_week_nights',
        'adults',
        'children',
        'babies',
        'arrival_date_month',
        'market_segment'
    ]

    assert_columns(df, required_columns)

    print("✅ Columns validation passed")

    # Clean
    print("🧼 Cleaning data...")
    df = clean(df)
    print(f"After cleaning: {df.shape}")

    # Features
    print("⚙️ Creating features...")
    df = build_features(df)

    # Save
    print("💾 Saving processed data...")
    df.to_csv(OUT_PATH, index=False)

    print("✅ Pipeline finished successfully!")

if __name__ == "__main__":
    main()
