# Main script

import streamlit as st

import sorting
import styles
import utils


def main():
    st.set_page_config(page_title="Royalties Dashboard", page_icon=None, layout="wide", initial_sidebar_state=None, menu_items=None)
    st.html(styles.custom_css)
    st.title("Royalties Dashboard")
    st.image("assets/records1.jpg", width="stretch")

    uploaded_file = st.file_uploader("Upload a CSV", type="csv")

    if not uploaded_file:
        st.html(
            "<span><a style='text-decoration: none' href='https://github.com/mcgooz/Royalties-Dashboard/blob/main/demo_csv/example_report.csv' target='_blank' rel='noopener noreferrer''>Grab a demo CSV file here</a></span>")
    
    if uploaded_file is not None:

        # Load data from pd read util    
        df = utils.load_csv(uploaded_file)
        if df is not None:
            tracks = df["Track Title"].unique()

            col1, col2 = st.columns(2)

            with col1:  
                dates = sorting.filter_by_date(df)

            with col2:
                artists = sorting.filter_by_artist(df)

            df_filtered = df.copy()

            if dates:
                df_filtered = df_filtered[df_filtered["Activity Period"].isin(dates)]

            if artists:
                df_filtered = df_filtered[df_filtered["Track Artists"].isin(artists)]

            # grouped = sorting.group_by_track(df_filtered, tracks).sort_values(by="Streams", ascending=False)
            grouped = sorting.group_by_track(df_filtered, tracks)
            
            
            with st.expander("Overview", expanded=True):            
                st.dataframe(grouped, selection_mode="single-row", hide_index=True)

            # Only pass filtered tracks (date, artist) to dropdown
            filtered_tracks = df_filtered["Track Title"].unique()
            option = utils.select(filtered_tracks)

            sorting.dsp_view(df_filtered, option)
            sorting.country_view(df_filtered, option)

if __name__ == "__main__":
    main()