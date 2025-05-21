### app/utils.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import kruskal

def load_data():
    files = ["data/benin_clean.csv", "data/sierraleone_clean.csv", "data/togo_clean.csv"]
    country_names = ["Benin", "Sierra Leone", "Togo"]
    df_list = []
    for file, country in zip(files, country_names):
        data = pd.read_csv(file)
        data['Country'] = country
        df_list.append(data)
    df = pd.concat(df_list, ignore_index=True)
    return df

def generate_summary_table(df):
    summary = df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std'])
    return summary.round(2)

def plot_boxplots(df):
    metrics = ['GHI', 'DNI', 'DHI']
    for metric in metrics:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Country', y=metric, data=df, ax=ax, palette='Set2')
        ax.set_title(f"Boxplot of {metric} by Country")
        st.pyplot(fig)

def run_stat_tests(df):
    metrics = ['GHI', 'DNI', 'DHI']
    for metric in metrics:
        groups = [df[df['Country'] == country][metric] for country in df['Country'].unique()]
        stat, p = kruskal(*groups)
        st.write(f"**{metric}**: Kruskal-Wallis H-test p-value = {p:.4f}")
        if p < 0.05:
            st.success("Statistically significant differences between countries.")
        else:
            st.info("No statistically significant difference detected.")

def plot_avg_ghi_bar(df):
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=avg_ghi.values, y=avg_ghi.index, palette='viridis', ax=ax)
    ax.set_xlabel("Average GHI (W/m²)")
    ax.set_title("Average GHI by Country")
    st.pyplot(fig)