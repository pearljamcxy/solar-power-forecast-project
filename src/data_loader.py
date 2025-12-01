import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def load_and_clean_generation(path):
    df = pd.read_csv(path, parse_dates=['DATE_TIME'])

    # ---- Basic cleaning (you only do this once here) ----
    df = df.dropna(subset=['DC_POWER', 'AC_POWER'])
    df.drop('PLANT_ID', axis=1, inplace=True)
    df['HOUR'] = df['DATE_TIME'].dt.hour
    df['DATE'] = df['DATE_TIME'].dt.date

    # Inverter Efficiency
    df['INVERTER_EFF'] = df['AC_POWER'] / df['DC_POWER'].replace(0, float('nan'))

    return df

def load_and_clean_sensor(path):
    df = pd.read_csv(path, parse_dates=['DATE_TIME'])

    # ---- Basic cleaning (you only do this once here) ----
    df = df.dropna(subset=['MODULE_TEMPERATURE', 'IRRADIATION'])
    df.drop('PLANT_ID', axis=1, inplace=True)
    df['HOUR'] = df['DATE_TIME'].dt.hour
    df['DATE'] = df['DATE_TIME'].dt.date

    return df

def plot_dayly_timeseries(df, column="IRRADIATION"):
    # --- 1. 检查 datetime index ---
    if "DATE_TIME" in df.columns:
        df = df.set_index("DATE_TIME")
    df.index = pd.to_datetime(df.index)
    
    # --- 2. 每日平均（Dayly Mean） ---
    dayly_mean = df[column].resample("D").mean()
    
    # --- 3. 绘图 ---
    plt.figure(figsize=(20, 8))
    sns.set_style("whitegrid")

    # 原始曲线
    sns.lineplot(
        x=df.index,
        y=df[column],
        linewidth=1,
        label=f"{column} (raw)",
        alpha=0.6
    )

    # 每周均值曲线
    sns.lineplot(
        x=dayly_mean.index,
        y=dayly_mean.values,
        linewidth=3,
        marker="o",
        color="orange",
        label=f"{column} - Dayly Mean"
    )

    # --- 4. 视觉增强 ---
    plt.title(f"{column} vs Time (Dayly Average)", fontsize=18)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel(column, fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()