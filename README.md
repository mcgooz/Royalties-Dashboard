# Royalties Dashboard

A Streamlit app to visualise and analyse track royalties for Symphonic Distribution artists/clients.  

Try it out here: https://royalties-dashboard.streamlit.app/

Manually tracking monthly royalties from CSV reports is tedious and error-prone. This dashboard automates the process, turning raw data into clear, visual insights in seconds.

## Features

- **Simple Imports**: Upload your standard royalty CSV reports – no complex setup required.  
- **Top Level Filters**: Quickly narrow down your data by date range or specific artists to focus on what matters.
- **Granular Analysis**: Dive deep into performance by individual track, digital service provider (Spotify, Apple Music), or country to uncover trends. 

## How To

**Try It Out**: A sample royalty report, `demo_report.csv`, is included in the `demo_csv` folder. Download the raw file and upload it via the form to explore the dashboard.

1. **Upload Your Data**: Click 'Browse files' and select your royalty report, or drag and drop (must be a CSV file from Symphonic Distribution). The app will automatically process and validate the data.
2. **Filter Your View**: Use the sidebar filters to select a specific reporting period or focus on royalties for a single artist
3. **Dive into Details**: Choose a track from the dropdown menu to instantly see its performance broken down by DSP and country in the charts below.
4. **Profit**: Watch those fractions of pennies roll on in!

## Stack
Python, Pandas, Streamlit, Altair, Frankfurter API