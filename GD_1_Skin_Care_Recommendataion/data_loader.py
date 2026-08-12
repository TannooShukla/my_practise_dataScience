import re
import ast
import numpy as np
import pandas as pd
from pathlib import Path
import streamlit as st

# =============================
# Data Loading
# =============================
@st.cache_data(show_spinner=True)
def load_data(path: Path):
    df = pd.read_csv(path)

    df.columns = [c.lower().strip() for c in df.columns]

    # ----- Price Cleaning -----
    def to_price(x):
        if pd.isna(x): return np.nan
        s = str(x)
        m = re.findall(r"[0-9]+(?:\\.[0-9]+)?", s)
        return float(m[0]) if m else np.nan

    df["price_numeric"] = df["price"].apply(to_price)

    # ----- Skin Type -----
    def parse_skin_type(x):
        if pd.isna(x): return []
        try:
            val = ast.literal_eval(str(x))
            if isinstance(val, list): return [v.strip() for v in val]
        except:
            pass
        return [p.strip() for p in str(x).split(',') if p.strip()]

    df["skin_type_list"] = df["skin_type"].apply(parse_skin_type)

    # ----- Concerns -----
    def parse_concern(x):
        if pd.isna(x): return []
        return [p.strip().lower() for p in str(x).split(',') if p.strip()]

    df["concern_list"] = df["concern"].apply(parse_concern)

    # ----- Text Field for Vectorizer -----
    df["text"] = (
        df["product_name"].fillna("").astype(str).str.lower() + " " +
        df["ingredients"].fillna("").astype(str).str.lower()
    )

    df["product_type"] = df["product_type"].fillna("").astype(str)

    return df

# =============================
# Dropdown Extraction
# =============================
@st.cache_data(show_spinner=False)
def get_dropdown_values(df):
    skin_types = sorted({s for lst in df["skin_type_list"] for s in lst})
    concerns = sorted({c for lst in df["concern_list"] for c in lst})
    product_types = sorted(df["product_type"].unique())

    pmin = int(df["price_numeric"].min())
    pmax = int(df["price_numeric"].max())

    return skin_types, concerns, product_types, (pmin, pmax)