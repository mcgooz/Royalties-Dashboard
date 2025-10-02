# Main script

import streamlit as st

import sorting
import utils


def main():
    st.title("Royalties")

    uploaded_file = st.file_uploader("Upload a CSV", type="csv")
    
    if uploaded_file is not None:
        df = utils.load_csv(uploaded_file)
        tracks = df["Track Title"].unique()
        dates = sorting.filter_by_date(df)

        df_dated = df[df["Activity Period"].isin(dates)]

        grouped = sorting.group_by_track(df_dated, tracks).sort_values(by="Count", ascending=False)
        
        
        with st.expander("Overview", expanded=True):            
            st.dataframe(grouped, selection_mode="single-row", hide_index=True)

        option = utils.select(tracks)
        sorting.dsp_view(df_dated, option)
        sorting.country_view(df_dated, option)

if __name__ == "__main__":
    main()