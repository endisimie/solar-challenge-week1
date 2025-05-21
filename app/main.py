### app/main.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils import load_data, plot_boxplots, generate_summary_table, plot_avg_ghi_bar, run_stat_tests

st.set_page_config(page_title="West Africa Solar Insights", layout="wide")
st.title("Solar Irradiance Comparison Dashboard")

# Sidebar Controls
st.sidebar.header("Controls")
show_stats = st.sidebar.checkbox("Show Summary Statistics", True)
show_boxplots = st.sidebar.checkbox("Show Boxplots", True)
show_pvalues = st.sidebar.checkbox("Show Statistical Test Results", True)
show_bar = st.sidebar.checkbox("Show Average GHI Ranking", True)

# Load data
df = load_data()

# Display Summary Table
if show_stats:
    st.subheader("Summary Statistics")
    summary_df = generate_summary_table(df)
    st.dataframe(summary_df)

# Boxplots
if show_boxplots:
    st.subheader("Boxplots by Country")
    plot_boxplots(df)

# Statistical Test Results
if show_pvalues:
    st.subheader("Kruskal-Wallis Test Results")
    run_stat_tests(df)

# GHI Bar Chart
if show_bar:
    st.subheader("Average GHI Ranking")
    plot_avg_ghi_bar(df)