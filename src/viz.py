import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")

def plot_cancellations(df):
    """
    Visualiza la distribución de cancelaciones vs reservas completadas.
    Incluye estadísticas descriptivas (totales, porcentajes).
    """
    # Calcular estadísticas
    cancellation_counts = df['is_canceled'].value_counts()
    cancellation_pct = df['is_canceled'].value_counts(normalize=True) * 100
    
    print("Estadísticas de Cancelaciones:")
    print(f"Total de reservas: {len(df):,}")
    print(f"Reservas completadas: {cancellation_counts.loc[False]:,} ({cancellation_pct.loc[False]:.1f}%)")
    print(f"Reservas canceladas:  {cancellation_counts.loc[True]:,} ({cancellation_pct.loc[True]:.1f}%)")
    print(f"Tasa de cancelación: {cancellation_pct.loc[True]:.1f}% (métrica crítica de negocio)\n")
    
    # Visualizar
    plt.figure(figsize=(8, 5))
    sns.countplot(x='is_canceled', data=df, palette=['#2ecc71', '#e74c3c'])
    plt.title("Distribución de Cancelaciones vs Completadas", fontsize=14, fontweight='bold')
    plt.xlabel("Estado de Reserva (0=Completada, 1=Cancelada)", fontsize=11)
    plt.ylabel("Número de Reservas", fontsize=11)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_lead_time_vs_cancel(df):
    """
    Compara la distribución del lead time entre reservas completadas y canceladas.
    Incluye estadísticas descriptivas por grupo (media, mediana, desv. estándar, etc).
    """
    # Estadísticas por grupo
    lead_time_by_cancel = df.groupby('is_canceled')['lead_time'].describe()
    print("Estadísticas de Lead Time por Estado de Cancelación:")
    print(lead_time_by_cancel)
    print()
    
    # Visualizar con boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='is_canceled', y='lead_time', data=df, palette=['#2ecc71', '#e74c3c'])
    plt.title("Lead Time: Comparación entre Reservas Completadas y Canceladas", 
              fontsize=14, fontweight='bold')
    plt.xlabel("Estado (0=Completada, 1=Cancelada)", fontsize=11)
    plt.ylabel("Lead Time (días)", fontsize=11)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_adr_by_hotel(df):
    """
    Visualiza la distribución de precios (ADR) por tipo de hotel.
    Incluye estadísticas descriptivas por hotel (media, mediana, desv. estándar, min, max).
    """
    # Estadísticas por hotel
    adr_by_hotel = df.groupby('hotel')['adr'].agg(['count', 'mean', 'median', 'std', 'min', 'max'])
    print("Estadísticas de ADR (Average Daily Rate) por Tipo de Hotel:")
    print(adr_by_hotel)
    print()
    
    # Visualizar
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='hotel', y='adr', data=df, palette='Set2')
    plt.title("Distribución de Precios Diarios (ADR) por Tipo de Hotel", 
              fontsize=14, fontweight='bold')
    plt.xlabel("Tipo de Hotel", fontsize=11)
    plt.ylabel("ADR - Average Daily Rate (€)", fontsize=11)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_revenue_by_segment(df):
    """
    Visualiza los ingresos promedio por segmento de mercado.
    Incluye etiquetas de valores en barras y estadísticas por segmento 
    (recuento, suma, media, mediana, tasa de cancelación).
    """
    # Estadísticas por segmento
    revenue_by_segment = df.groupby('market_segment').agg({
        'total_revenue': ['count', 'sum', 'mean', 'median'],
        'is_canceled': 'mean'
    }).round(2)
    
    print("Métricas de Ingresos por Segmento de Mercado:")
    print(revenue_by_segment)
    print()
    
    # Visualizar con valores en barras
    revenue_mean = df.groupby('market_segment')['total_revenue'].mean().sort_values(ascending=False)
    plt.figure(figsize=(11, 6))
    bars = plt.bar(revenue_mean.index, revenue_mean.values, 
                   color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6'][:len(revenue_mean)])
    plt.title("Ingresos Promedio por Segmento de Mercado", fontsize=14, fontweight='bold')
    plt.xlabel("Segmento de Mercado", fontsize=11)
    plt.ylabel("Ingresos Promedio (€)", fontsize=11)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Añadir valores en las barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'€{height:.0f}',
                 ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.show()


def plot_seasonality(df):
    """
    Visualiza la estacionalidad de las reservas por mes.
    Identifica picos de demanda (verano), valles (invierno) y variación porcentual.
    Incluye línea de promedio y colores diferenciados por temporada.
    """
    # Ordenar meses de forma correcta
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    reservas_por_mes = df['arrival_date_month'].value_counts().reindex(month_order)
    
    print("Estadísticas de Estacionalidad:")
    print("Número de reservas por mes:")
    print(reservas_por_mes)
    print()
    
    # Identificar picos y valles
    print(f"Mes más demandado: {reservas_por_mes.idxmax()} ({reservas_por_mes.max():,} reservas)")
    print(f"Mes menos demandado: {reservas_por_mes.idxmin()} ({reservas_por_mes.min():,} reservas)")
    print(f"Variación: {((reservas_por_mes.max() - reservas_por_mes.min()) / reservas_por_mes.min() * 100):.1f}%\n")
    
    # Visualizar
    plt.figure(figsize=(14, 6))
    colors = ['#e74c3c' if m in ['July', 'August', 'September'] else '#3498db' for m in month_order]
    bars = plt.bar(range(len(month_order)), reservas_por_mes.values, color=colors)
    
    plt.title("Estacionalidad de las Reservas: Demanda por Mes", fontsize=14, fontweight='bold')
    plt.xlabel("Mes de Llegada", fontsize=11)
    plt.ylabel("Número de Reservas", fontsize=11)
    plt.xticks(range(len(month_order)), month_order, rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Añadir promedio como línea
    avg_line = reservas_por_mes.mean()
    plt.axhline(y=avg_line, color='green', linestyle='--', linewidth=2, label=f'Promedio ({avg_line:.0f})')
    plt.legend()
    
    # Añadir valores en las barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{int(height):,}',
                 ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()


def plot_duration_vs_revenue(df):
    """
    Visualiza la relación entre duración de estancia e ingresos totales.
    Calcula correlación de Pearson e incluye línea de tendencia polinómica para reservas ≤30 noches.
    Identifica y reporta outliers (estancias > 30 noches).
    """
    # Calcular correlación
    correlation = df['total_nights'].corr(df['total_revenue'])
    print("Análisis de Duración vs Ingresos:")
    print(f"Correlación de Pearson: {correlation:.3f}")
    print(f"Interpretación: {'Relación fuerte y positiva' if correlation > 0.7 else 'Relación moderada'}\n")
    
    # Estadísticas
    print(f"Duración promedio: {df['total_nights'].mean():.1f} noches")
    print(f"Ingresos promedio: €{df['total_revenue'].mean():.2f}\n")
    
    # Visualizar scatter plot con tendencia
    plt.figure(figsize=(12, 6))
    
    # Scatter plot
    plt.scatter(df['total_nights'], df['total_revenue'], 
                alpha=0.3, s=20, color='#3498db', edgecolors='none')
    
    # Línea de tendencia (solo para estancias ≤30 noches)
    df_filtered = df[df['total_nights'] <= 30]
    z = np.polyfit(df_filtered['total_nights'], df_filtered['total_revenue'], 1)
    p = np.poly1d(z)
    nights_sorted = np.sort(df_filtered['total_nights'].unique())
    plt.plot(nights_sorted, p(nights_sorted), "r--", linewidth=2, label='Tendencia (≤30 noches)')
    
    plt.title("Relación entre Duración de Estancia e Ingresos", fontsize=14, fontweight='bold')
    plt.xlabel("Duración Total de Estancia (noches)", fontsize=11)
    plt.ylabel("Ingresos Totales (€)", fontsize=11)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Nota sobre outliers
    outliers = df[df['total_nights'] > 30]
    print(f"Nota: {len(outliers):,} registros con estancias > 30 noches (outliers excluidos de la tendencia)")
