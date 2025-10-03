# Utility helpers

import streamlit as st
import pandas as pd

REQUIRED_COLUMNS = [
    "Label",
    "Release Name",
    "Release Version",
    "Release Artists",
    "UPC Code",
    "Catalogue",
    "Track Title",
    "Mix Version",
    "ISRC Code",
    "Track Artists",
    "Digital Service Provider",
    "Activity Period",
    "Territory",
    "Delivery",
    "Content Type",
    "Sale or Void",
    "Count",
    "Royalty ($US)"
]

@st.cache_data
def load_csv(uploaded_file):
    # Load and cache (valid) csv
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Could not read file: {e}")
        return None
     
    # Tidy column names
    df.columns = df.columns.str.strip()

    # Ensure correct colums are present
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        st.warning(f"Cannot find the required data. Please upload a valid Symphonic Distribution report in CSV format.", icon=":material/warning:")
        return None

    return df


def select(tracks):
    tracklist = [track for track in tracks]
    option = st.selectbox(
        "Select a track to see more details",
        tracklist,
        index=None
    )
    return option