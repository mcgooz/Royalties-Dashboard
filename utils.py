# Utility helpers

import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(uploaded_file):
    # Load and cache csv
    return pd.read_csv(uploaded_file)

def select(tracks):
    tracklist = [track for track in tracks]
    option = st.selectbox(
        "Select a track to see more details",
        tracklist,
        index=None
    )
    return option