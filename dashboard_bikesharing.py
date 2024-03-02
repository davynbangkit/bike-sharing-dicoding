import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard: Bike Sharing Data Analytics")

st.header("Snapshot Bike-sharing ")

df_day = pd.read_csv("dataset/day_cleaned.csv")
df_hour = pd.read_csv("dataset/hour_cleaned.csv")

tab_day, tab_hour = st.tabs(["Cleaned day.csv", "Cleaned hour.csv"])

tab_day.write(df_day.head())
tab_hour.write(df_hour.head())


# 1. Data Bar Chart Frekuensi Pola Pengunaan Sepeda
def show_pattern_usage(df_hours_usage):
    df_hours_usage = df_hour[["hr", "holiday", "cnt"]].copy()

    df_hours_usage.groupby("hr").agg({"cnt": "sum"})

    return df_hours_usage


# 2. Data Line Chart Frekuensi Pola Pengunaan Sepeda
def freq_comparison_usage(df_hours_comparison):
    df_hours_comparison = df_hour[["hr", "registered", "cnt"]].copy()
    return df_hours_comparison


# 3. Data Scatter Plot korelasi berdasarkan musim dan indikator cuaca
def scatter_season_usage(df_day_correlation):
    df_day_correlation = df_day[["season", "hum", "temp", "atemp", "cnt"]].copy()
    return df_day_correlation


# 4. Data Bar Chart berdasarkan musim dan indikator cuaca
def show_season_usage(df_season_usage):
    df_season_usage = df_day[["season", "cnt"]].copy()

    df_season_usage.groupby("season").agg({"cnt": "sum"})

    return df_season_usage


st.header("Bike-sharing Graph")

# Bagian penggunaan berdasarkan jam
st.subheader("Hourly usage graph")

col_bar_pattern, col_line_freq = st.columns(2)
col_bar_pattern_explanations, col_line_freq_explanations = st.columns(2)

col_bar_pattern.bar_chart(data=show_pattern_usage(df_hour), x="hr", y="cnt")

with col_bar_pattern_explanations.expander("Penjelasan Peak Hours Bike-sharing"):
    st.write(
        "Sesuai dengan analisis di atas, pola distribusi penggunaan sepeda dalam sehari menunjukkan pola kenaikan yang cukup tinggi pada jam 08.00, 17.00, dan 18.00. Hal ini dapat menyiratkan bahwa rata - rata pengguna bike-sharing adalah para pekerja"
    )

col_line_freq.line_chart(
    data=freq_comparison_usage(df_hour), x="hr", y=["registered", "cnt"]
)

with col_line_freq_explanations.expander("Penjelasan Perbandingan Pengguna"):
    st.write(
        "Dalam line chart di atas, terdapat visualisasi perbandingan untuk jumlah pengguna sepeda dan pengguna yang melakukan pendaftaran terhadap aplikasi. Hasilnya, tidak terdapat perbedaan yang jauh di antara angka keduanya, menyiratkan bahwa hampir sebagian besar pengguna telah melek akan teknologi dan dapat menggunakan sistem secara lancar."
    )
    
# Bagian penggunaan berdasarkan musim
st.subheader("Seasonly usage graph")
col_scatter_season, col_bar_season = st.columns(2)

col_scatter_season.scatter_chart(data=scatter_season_usage(df_day), x="temp", y="cnt")

col_bar_season.bar_chart(
    data=show_season_usage(df_hour), x="season", y="cnt"
)

with st.expander("Penjelasan Penggunaan dalam tiap - tiap musim"):
    st.write(
        "Melalui visualisasi kluster di atas, dapat dilihat bahwa sebagian besar pengguna menggunakan sepeda pada tiap musim, kecuali pada musim winter atau dingin."
    )
