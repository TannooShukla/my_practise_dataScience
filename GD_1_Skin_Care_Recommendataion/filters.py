# =============================
# Filtering Logic
# =============================

def filter_candidates(df, skin, concern, ptype, price_min, price_max):
    """
    Filters products by:
    ✅ Skin Type
    ✅ Concern
    ✅ Product Type
    ✅ Price Range
    """

    dff = df.copy()

    # Filter skin type
    dff = dff[[skin in stype for stype in dff["skin_type_list"]]]

    # Filter concern
    dff = dff[[concern in clist for clist in dff["concern_list"]]]

    # Filter product type
    dff = dff[dff["product_type"].str.lower() == ptype.lower()]

    # Filter price range
    dff = dff[(dff["price_numeric"] >= price_min) & (dff["price_numeric"] <= price_max)]

    return dff