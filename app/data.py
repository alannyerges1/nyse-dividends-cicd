import csv
from pathlib import Path

# ----- MOCK DATA MODE -----
# Simple static yields so your app/pipeline work immediately.
# We'll replace this in Phase B with a live API.

MOCK_YIELDS = {
    "T": 0.072, "XOM": 0.033, "KO": 0.031, "MO": 0.087, "PM": 0.052,
    "IBM": 0.041, "VZ": 0.065, "CVX": 0.032, "PFE": 0.061, "O": 0.056
}

def load_nyse_symbols(csv_path="app/tickers.csv"):
    symbols = []
    path = Path(csv_path)
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("exchange", "").upper() == "NYSE":
                symbols.append(row["symbol"].strip().upper())
    return symbols

def get_top_dividends(limit=10):
    syms = load_nyse_symbols()
    rows = []
    for s in syms:
        dy = float(MOCK_YIELDS.get(s, 0.0))
        rows.append({
            "symbol": s,
            "name": s,           # mock name = symbol
            "sector": "",        # empty in mock
            "dividend_yield": dy # fraction (0.05 == 5%)
        })
    rows.sort(key=lambda r: r["dividend_yield"], reverse=True)
    return rows[:limit]
