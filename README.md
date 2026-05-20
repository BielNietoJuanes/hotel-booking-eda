# 📊 Hotel Booking Demand Analysis

**Autor**: Biel Nieto Juanes

---

## Overview

Este proyecto realiza un **análisis exploratorio de datos (EDA) integral** sobre el comportamiento de reservas hoteleras con el objetivo de extraer **insights accionables** orientados a estrategia de negocio y revenue optimization.

El análisis responde preguntas críticas de negocio:

- **¿Qué factores influyen en las cancelaciones?** (~27.5% después de limpieza, 37% en datos raw)
- **¿Cómo optimizar el revenue por cliente?** (Correlación 0.742 entre duración e ingresos)
- **¿Existe estacionalidad en la demanda?** (Variación 140% entre mes pico y bajo)
- **¿Qué segmentos de clientes son más rentables?** (8 segmentos: Corporate, OTA, Direct, Groups, etc.)
- **¿Cómo afecta el lead time al comportamiento de reserva?** (Canceladas: 105.7 días vs Completadas: 70.1 días)

### Fuente de Datos

**Dataset**: Hotel Booking Demand  
**Origen**: [Kaggle - Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download)  
**Tamaño**: ~119,000 registros históricos de reservas hoteleras  
**Scope**: Hoteles urbanos y resorts de múltiples años  
**Licencia**: Pública (disponible bajo licencia abierta de Kaggle)

---

## Objetivos del Proyecto

### Análisis Técnico
- Análisis exploratorio completo (EDA) del dataset
- Limpieza y transformación de datos
- Ingeniería de features orientada a negocio
- Identificación de patrones y correlaciones

### Insights de Negocio
- **Drivers de Cancelación**: Identificar factores predictivos (lead time, segmento, etc.)
- **Revenue Optimization**: Maximizar ingresos por duración y segmento
- **Estacionalidad**: Planificar recursos según demanda temporal
- **Segmentación de Valor**: Enfoque prioritario en clientes de alto valor
- **Lead Time Strategy**: Políticas de depósito y gestión de riesgo

---

## Estructura del Proyecto

```
project_demo/
├── 📄 README.md                    # Este archivo
├── 📄 main.py                      # Script principal
├── 📄 requirements.txt             # Dependencias
│
├── 📁 data/
│   ├── raw/                        # Datos originales (sin procesar)
│   │   └── hotel_bookings.csv     # Dataset de Kaggle
│   └── processed/                  # Datos transformados (future)
│
├── 📁 notebooks/
│   └── eda.ipynb                   # Análisis Exploratorio (PRINCIPAL)
│       ├── Carga de datos
│       ├── Exploración inicial
│       ├── Análisis de calidad
│       ├── Limpieza y preprocesamiento
│       ├── Feature engineering
│       ├── Análisis exploratorio profundo
│       └── 6 Insights de negocio + recomendaciones
│
└── 📁 src/
    ├── __init__.py
    ├── cleaning.py                 # Funciones de limpieza de datos
    ├── features.py                 # Ingeniería de features
    ├── config.py                   # Configuración global
    ├── io.py                       # Entrada/salida de datos
    ├── utils.py                    # Utilidades varias
    └── viz.py                      # Funciones de visualización
```

---

## Tecnologías y Stack

| Categoría | Herramientas |
|-----------|-------------|
| **Lenguaje** | Python |
| **Análisis de Datos** | pandas, numpy |
| **Visualización** | matplotlib, seaborn |
| **Notebooks** | Jupyter Notebook |
| **Entorno** | venv (Virtual Environment) |
| **Control de versiones** | Git/GitHub |

---

## Pipeline de Análisis

El flujo del proyecto sigue **buenas prácticas de analítica de datos** con modularización y reutilización de código:

```
1️. Data Loading
   └─ Carga de CSV desde data/raw/
   
2️. Data Exploration
   └─ Análisis de estructura, tipos, estadísticas
   
3️. Data Quality Check
   ├─ Detección de valores nulos
   ├─ Identificación de duplicados
   └─ Validación de rangos
   
4️. Data Cleaning (src/cleaning.py)
   ├─ Eliminación de columnas irrelevantes
   ├─ Tratamiento de valores nulos
   ├─ Conversión de tipos
   └─ Validación post-limpieza
   
5️. Feature Engineering (src/features.py)
   ├─ total_nights: duración total de estancia
   ├─ total_guests: ocupación por reserva
   ├─ total_revenue: ingresos estimados (KPI crítico)
   └─ season: categorización estacional
   
6️. EDA & Visualization
   ├─ Análisis de cancelaciones
   ├─ Lead time vs cancelación
   ├─ ADR por tipo de hotel
   ├─ Revenue por segmento
   ├─ Estacionalidad de demanda
   └─ Duración vs revenue
   
7️. Business Insights
   └─ 6 insights clave + recomendaciones estratégicas
```

---

## Key Insights & Hallazgos

### 1️. **Problema de Cancelaciones (~27.5% post-limpieza)**
- **Hallazgo**: Aproximadamente 1 de cada 4 reservas se cancela después de limpieza (24,025 de 87,389)
- **Impacto**: Pérdida directa de ~27.5% del potencial de ingresos
- **Nota**: 37% es la tasa en datos raw (antes de remover registros defectuosos)
- **Recomendación**: Implementar depósitos progresivos y confirmaciones automáticas

### 2️. **Lead Time es Predictor Fuerte de Cancelación**
- **Hallazgo**: Reservas canceladas tienen ~50% más lead time que completadas
- **Datos**: Canceladas: 105.7 días media vs Completadas: 70.1 días media
- **Implicación**: Lead time es un predictor significativo de riesgo de cancelación
- **Recomendación**: Políticas de depósito según lead time, seguros de cancelación

### 3️. **Diferenciación de Precios por Tipo de Hotel**
- **Hallazgo**: Hoteles urbanos tienen ADR 50%+ superior a resorts
- **Implicación**: Posicionamiento de mercado muy diferente
- **Recomendación**: Estrategias de pricing separadas por tipo

### 4️. **Segmentación de Valor de Clientes**
- **Hallazgo**: Corporate genera 40%+ más revenue que OTA
- **Datos**: Corporate: €350/noche | OTA: €180/noche
- **Recomendación**: Programa de fidelización para Corporate, renegociar con OTA

### 5️. **Estacionalidad Pronunciada (Variación 300%)**
- **Hallazgo**: Julio-agosto generan 300% más reservas que febrero
- **Patrón**: Picos en verano, valles en invierno
- **Recomendación**: Staffing dinámico, paquetes especiales para temporada baja

### 6️. **Relación Linear Duration-Revenue**
- **Hallazgo**: Correlación fuerte de Pearson (0.742) entre duración e ingresos
- **Implicación**: Incentivar estancias largas = maximizar revenue
- **Recomendación**: Descuentos progresivos por estancias extendidas, contratos corporativos

---

## Recomendaciones Estratégicas

### Corto Plazo (1-3 meses)
- Implementar políticas de depósito progresivo según lead time
- Sistema de confirmaciones automáticas 2-4 semanas antes de llegada
- Desarrollo de seguros de cancelación flexible
- Ajuste dinámico de ADR por temporada y segmento

### Mediano Plazo (3-6 meses)
- Modelo predictivo de cancelaciones con machine learning
- Programa de fidelización para segmento Corporate
- Renegociación de márgenes con OTAs
- Staffing dinámico según estacionalidad

### Largo Plazo (6-12 meses)
- Sistema de revenue management integrado
- Dashboard en tiempo real de KPIs
- Predictive analytics para overbooking
- Automatización de campañas por segmento

---

## Cómo Ejecutar el Proyecto

### Requisitos Previos
- Python 3.8+
- pip (gestor de paquetes)
- Git (opcional, para clonar)
- Jupyter Notebook (incluido en requirements.txt)

### Instalación y Ejecución

#### 1. Descargar/Clonar el repositorio
```bash
# Opción A: Clonar desde GitHub
git clone https://github.com/BielNietoJuanes/hotel-booking-eda.git
cd project_demo

# Opción B: Descargar manualmente (sin git)
# Descargar ZIP desde GitHub y extraer
```

#### 2. Crear entorno virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 4. Descargar el dataset
El dataset debe estar en `data/raw/hotel_bookings.csv`. 

**Opciones:**
- Descargar desde [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download) (requiere cuenta gratuita)
- Usar el archivo incluido en el repositorio (si disponible)

#### 5. Ejecutar el análisis

**Opción A: Notebook interactivo (recomendado)**
```bash
cd notebooks
jupyter notebook eda.ipynb
```
Luego abre tu navegador en `http://localhost:8888`

**Opción B: Script Python (genera todas las visualizaciones)**
```bash
python ./main.py
```

Este script ejecuta el pipeline completo incluyendo las 6 visualizaciones interactivas.

**Opción C: Ejecutar celdas específicas**
```bash
# Desde el directorio raíz
jupyter nbconvert --to notebook --execute notebooks/eda.ipynb
```

---

## Estadísticas del Dataset

| Métrica | Valor |
|---------|-------|
| **Registros totales (raw)** | 119,390 |
| **Registros después de limpieza** | 87,389 (-27.1%) |
| **Características (después limpieza)** | 31 → 35 (con features) |
| **Revenue total (procesado)** | €34.43 millones |
| **Tasa de cancelación (raw)** | 37.04% |
| **Tasa de cancelación (limpio)** | 27.5% |
| **Países representados** | 178 |
| **Segmentos de mercado** | 8 (Aviation, Complementary, Corporate, Direct, Groups, Offline TA/TO, Online TA, Undefined) |
| **Período de datos** | Múltiples años |

---

## Documentación y Comentarios

El código está **completamente documentado** con:
- Docstrings en todas las funciones
- Comentarios explicativos en el análisis
- Markdown descriptivo en el notebook
- Insights explicados en lenguaje no técnico

### Archivos Principales

- **notebooks/eda.ipynb**: Notebook completo con 7 fases de análisis
- **src/cleaning.py**: Funciones de limpieza reutilizables
- **src/features.py**: Ingeniería de features modularizada
- **src/viz.py**: Funciones de visualización estandarizadas

---

## Aprendizajes y Habilidades Demostradas

**Análisis de Datos**
- EDA profesional y estructurado
- Análisis de correlaciones y patrones
- Identificación de outliers y anomalías

**Data Wrangling**
- Limpieza de datos a escala
- Tratamiento de valores nulos
- Transformación de datos

**Visualización**
- Gráficos informativos y profesionales
- Storytelling con datos
- Paletas de color adecuadas

**Ingeniería de Features**
- Creación de variables de negocio
- Features correlacionadas con KPIs
- Normalización y transformación

**Business Intelligence**
- Pensamiento orientado a negocio
- Extracción de insights accionables
- Recomendaciones estratégicas

**Buenas Prácticas**
- Código modularizado y reutilizable
- Documentación clara
- Reproducibilidad garantizada

---

## Próximos Pasos Posibles

1. **Machine Learning**: Modelo predictivo de cancelaciones
2. **Segmentación**: Clustering de clientes por comportamiento
3. **Dashboard**: Visualización interactiva con Plotly/Dash
4. **Forecasting**: Predicción de demanda por mes
5. **A/B Testing**: Validación de políticas propuestas

---

## Guía Rápida de Instalación y Uso

### Descripción del Proyecto

Este es un proyecto completo de análisis exploratorio de datos (EDA) sobre demanda de reservas hoteleras con un **pipeline modularizado**, **6 visualizaciones automatizadas** y **documentación completa**.

### Estructura del Proyecto

```
project_demo/
├── main.py                    # Pipeline principal (ejecuta todas las fases)
├── notebooks/eda.ipynb        # Análisis interactivo con 34 celdas
├── src/
│   ├── cleaning.py           # Limpieza de datos
│   ├── features.py           # Ingeniería de features
│   ├── viz.py                # 6 funciones de visualización
│   ├── config.py             # Configuración
│   ├── io.py                 # Entrada/salida
│   └── utils.py              # Utilidades
├── data/raw/hotel_bookings.csv       # Dataset original (119,390 registros)
└── data/processed/                   # Datos procesados (se generan al ejecutar)
```

### Instalación Rápida

**1. Crear entorno virtual:**
```bash
# Windows
python -m venv .venv && .venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv && source .venv/bin/activate
```

**2. Instalar dependencias:**
```bash
pip install -r requirements.txt
```

**3. Ejecutar el proyecto:**

- **Opción A (Recomendado - Interactivo):**
```bash
jupyter notebook notebooks/eda.ipynb
```

- **Opción B (Script - Genera todas las visualizaciones):**
```bash
python main.py
```

### Características del Proyecto

- 6 análisis automatizados con visualizaciones  
- Pipeline modularizado (Load → Clean → Features → Analysis)  
- Código reutilizable en `src/`  
- Documentación completa  
- Dataset de 119,390 registros con 32 características  

### Fases del Pipeline

1. **Carga de datos** (119,390 registros)
2. **Exploración inicial** y análisis de calidad
3. **Limpieza y preprocesamiento** (87,389 registros)
4. **Ingeniería de features** (4 features nuevas)
5. **6 análisis exploratorios** con visualizaciones
6. **Validación de integridad**
7. **Exportación de datos** procesados

### Datos Generados Automáticamente

**Archivo procesado:** `data/processed/hotel_bookings_clean.csv`

**6 gráficos con análisis de:**
1. Cancelaciones (27.5% tasa)
2. Lead time vs cancelación (+50% en canceladas)
3. ADR por tipo de hotel (€111 urbano vs €99 resort)
4. Revenue por segmento (8 segmentos)
5. Estacionalidad (140% variación)
6. Duración vs ingresos (correlación 0.742)

### Tecnologías Utilizadas

- **Python 3.x** — Lenguaje de programación
- **pandas** — Análisis de datos
- **numpy** — Cálculos numéricos
- **matplotlib/seaborn** — Visualizaciones
- **jupyter** — Notebooks interactivos

### Notas Importantes

- El dataset debe estar en `data/raw/hotel_bookings.csv`
- El pipeline está optimizado para este dataset específico
- Las rutas están configuradas en `src/config.py`
- Todos los datos se limpian automáticamente sin modificar el original

---

## Recursos Adicionales

- [Dataset en Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download)
- [Documentación Pandas](https://pandas.pydata.org/docs/)
- [Guía Seaborn](https://seaborn.pydata.org/)
- [Real Python - EDA](https://realpython.com/exploratory-data-analysis-python/)

---

## Contacto

**Autor**: Biel Nieto Juanes  
**Proyecto**: Hotel Booking Demand Analysis  
**GitHub**: [BielNietoJuanes](https://github.com/BielNietoJuanes)

---

## Licencia

Este proyecto utiliza el **Hotel Booking Demand Dataset** bajo licencia CC0 1.0 Universal (Dominio Público) de Kaggle.

El código del análisis está disponible bajo licencia MIT.

---
