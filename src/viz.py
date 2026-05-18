import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")

def plot_cancellations(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x='is_canceled', data=df)
    plt.title("Distribución de Cancelaciones")
    plt.xlabel("Cancelado")
    plt.ylabel("Número de reservas")
    plt.tight_layout()
    plt.show()


def plot_lead_time_vs_cancel(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(x='is_canceled', y='lead_time', data=df)
    plt.title("Lead Time vs Cancelación")
    plt.tight_layout()
    plt.show()


def plot_adr_by_hotel(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(x='hotel', y='adr', data=df)
    plt.title("Precio (ADR) por tipo de hotel")
    plt.tight_layout()
    plt.show()


def plot_revenue_by_segment(df):
    plt.figure(figsize=(10,5))
    df.groupby('market_segment')['total_revenue'].mean().sort_values().plot(kind='bar')
    plt.title("Revenue medio por segmento")
    plt.ylabel("Revenue medio")
    plt.tight_layout()
    plt.show()