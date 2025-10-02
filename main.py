# Main script

import streamlit as st

import sorting
import utils


def main():
    st.markdown(
        """
        <style>
            /* Reduce top/bottom padding */
            .block-container {
                padding-top: 1rem;
                padding-bottom: 5rem;
            }

            /* Center the main title */
            h1 {
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Royalties Dashboard")
    st.image("assets/records1.jpg")

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