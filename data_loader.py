import pandas as pd

def load_gdp_data(path: str):
    raw = pd.read_csv(path)
    raw.columns = ["Label", "Value"]

    # Detect rows that look like quarterly data (YYYY Qx OR YYYYQx)
    mask = raw["Label"].str.contains(r"\d{4}\s?Q[1-4]", regex=True, na=False)

    if not mask.any():
        raise ValueError("No quarterly data found. Check CSV format.")

    start_idx = raw[mask].index[0]

    df = raw.iloc[start_idx:].copy()
    df.columns = ["Quarter", "GDP_Growth"]

    df["GDP_Growth"] = pd.to_numeric(df["GDP_Growth"], errors="coerce")

    # Extract year and quarter safely
    df["Year"] = df["Quarter"].str.extract(r"(\d{4})").astype(int)
    df["Q"] = df["Quarter"].str.extract(r"Q([1-4])").astype(int)

    df["Date"] = pd.PeriodIndex(
        year=df["Year"],
        quarter=df["Q"],
        freq="Q"
    ).to_timestamp()

    return df.sort_values("Date").reset_index(drop=True)
