# Sorting and filtering functions

import altair as alt
import streamlit as st
import pandas as pd

import exchange

# Initial date filter, default is select all
def filter_by_date(df):
    # Convert to datetime for ordering
    dates_dt = pd.to_datetime(df["Activity Period"], format="%B %Y")
    sorted_dates = df.loc[dates_dt.argsort(), "Activity Period"].unique()


    selected_period = st.segmented_control(
        "Filter by reporting period",
        sorted_dates,
        default=list(sorted_dates),
        selection_mode="multi"
    )

    return selected_period


# Filter by Artist
def filter_by_artist(df):
    filtered_artist = df["Release Artists"].unique()

    selected_artist = st.segmented_control(
        "Filter by artist",
        filtered_artist,
        default=list(filtered_artist),
        selection_mode="multi"
    )

    return selected_artist


# Filter and group by track title
def group_by_track(df, tracks):
    filtered = df[df["Track Title"].isin(tracks)].copy()

    # Convert to EUR and add column 
    filtered["Royalty (EUR €)"] = exchange.convert(filtered["Royalty ($US)"])

    filtered["Streams"] = filtered.loc[filtered["Delivery"]== "Streaming", "Count"]
    filtered["Downloads"] = filtered.loc[filtered["Delivery"]== "Download", "Count"]


    # Group count and royalties per track, include mix version
    grouped = (
        filtered.groupby(["Track Title", "Mix Version"], dropna=False)
        .agg({
            "Streams": "sum",
            "Downloads": "sum",
            "Royalty ($US)": "sum",
            "Royalty (EUR €)": "sum"
        })
        .reset_index()
    )

    return grouped


# Filter and display by DSP
def dsp_view(df, option):
    dsp = "Digital Service Provider"
    if option is not None:
        details = df[df["Track Title"] == option].copy()

        details["Royalty (EUR €)"] = exchange.convert(details["Royalty ($US)"])

        grouped_by = (
            details.groupby([dsp], dropna=False)
            .agg({
                "Count": "sum",
                "Royalty (EUR €)": "sum"
            })
            .reset_index()
        ).sort_values(by="Count", ascending=False)

        source = grouped_by

        base = alt.Chart(source).encode(
            x=alt.X(
                "Digital Service Provider:N",
                sort="-y"   # sort by count
            )
        )
        
        bar = base.mark_bar(color="lavender").encode(
            y=alt.Y("Count:Q", axis=alt.Axis(title="Count"))
        )

        line = base.mark_line(color="navy", strokeWidth=2, interpolate="monotone").encode(
            y=alt.Y("Royalty (EUR €):Q", axis=alt.Axis(title="Royalty (EUR €)", orient="right"))
        )

        chart = alt.layer(bar, line).resolve_scale(
            y="independent"  # separate scales for bar and line
        ).properties(width=600)
        
        with st.expander("DSP", expanded=False):
            st.altair_chart(chart)


# Filter and display by Country (Territory)
def country_view(df, option):
    country = "Territory"
    if option is not None:
        details = df[df["Track Title"] == option]

        grouped_by = (
            details.groupby([country], dropna=False)
            .agg({
                "Count": "sum"
            })
            .reset_index()
        ).sort_values(by="Count", ascending=False)

        chart = alt.Chart(grouped_by).mark_bar(color="lavender").encode(
            x=alt.X(
                "Territory:N",
                sort="-y",
                axis=alt.Axis(labelFontSize=7)
            ),
            y=alt.Y(
                "Count:Q",
            )
        )

        with st.expander("Countries", expanded=False):
            st.altair_chart(chart, use_container_width=True)