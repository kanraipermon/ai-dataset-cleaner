import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import argparse

def clean_dataset(input_file, output_file, drop_duplicates, fill_missing, detect_outliers, report):
    df = pd.read_csv(input_file)

    if drop_duplicates:
        df = df.drop_duplicates()

    if fill_missing:
        if fill_missing == "mean":
            df = df.fillna(df.mean(numeric_only=True))
        elif fill_missing == "median":
            df = df.fillna(df.median(numeric_only=True))
        elif fill_missing == "zero":
            df = df.fillna(0)

    if detect_outliers:
        numeric_df = df.select_dtypes(include=[np.number]).dropna()
        iso = IsolationForest(contamination=0.05, random_state=42)
        preds = iso.fit_predict(numeric_df)
        df = df.loc[numeric_df.index[preds == 1]]

    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned dataset saved to {output_file}")

    if report:
        print("\n📊 Data Summary:")
        print(df.describe())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Dataset Cleaner Utility")
    parser.add_argument("--input", required=True, help="Input CSV file path")
    parser.add_argument("--output", required=True, help="Output CSV file path")
    parser.add_argument("--drop-duplicates", action="store_true", help="Remove duplicate rows")
    parser.add_argument("--fill-missing", choices=["mean", "median", "zero"], help="Fill missing numeric values")
    parser.add_argument("--detect-outliers", action="store_true", help="Detect and remove outliers")
    parser.add_argument("--report", action="store_true", help="Print dataset summary report")

    args = parser.parse_args()
    clean_dataset(args.input, args.output, args.drop_duplicates, args.fill_missing, args.detect_outliers, args.report)
