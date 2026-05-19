# 📊 Hotel Booking Demand Analysis

**Autor**: Biel Nieto Juanes

---

## 🧠 Overview

Este proyecto realiza un **análisis exploratorio de datos (EDA) integral** sobre el comportamiento de reservas hoteleras con el objetivo de extraer **insights accionables** orientados a estrategia de negocio y revenue optimization.

El análisis responde preguntas críticas de negocio:

- **¿Qué factores influyen en las cancelaciones?** (~37% de las reservas se cancelan)
- **¿Cómo optimizar el revenue por cliente?** (Relación clara entre duración e ingresos)
- **¿Existe estacionalidad en la demanda?** (Variación de hasta 300% entre meses)
- **¿Qué segmentos de clientes son más rentables?** (Corporate vs OTA vs Direct)
- **¿Cómo afecta el lead time al comportamiento de reserva?** (Predictor fuerte de cancelación)

### 📂 Fuente de Datos

**Dataset**: Hotel Booking Demand  
**Origen**: [Kaggle - Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download)  
**Tamaño**: ~119,000 registros históricos de reservas hoteleras  
**Scope**: Hoteles urbanos y resorts de múltiples años  
**Licencia**: Pública (disponible bajo licencia abierta de Kaggle)

---

## 🎯 Objetivos del Proyecto

### Análisis Técnico
- ✅ Análisis exploratorio completo (EDA) del dataset
- ✅ Limpieza y transformación de datos
- ✅ Ingeniería de features orientada a negocio
- ✅ Identificación de patrones y correlaciones

### Insights de Negocio
- 🎯 **Drivers de Cancelación**: Identificar factores predictivos (lead time, segmento, etc.)
- 📈 **Revenue Optimization**: Maximizar ingresos por duración y segmento
- 🌍 **Estacionalidad**: Planificar recursos según demanda temporal
- 💰 **Segmentación de Valor**: Enfoque prioritario en clientes de alto valor
- ⏰ **Lead Time Strategy**: Políticas de depósito y gestión de riesgo

---

## 🗂️ Estructura del Proyecto

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
│   └── eda.ipynb                   # 📊 Análisis Exploratorio (PRINCIPAL)
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

## 🛠️ Tecnologías y Stack

| Categoría | Herramientas |
|-----------|-------------|
| **Lenguaje** | Python |
| **Análisis de Datos** | pandas, numpy |
| **Visualización** | matplotlib, seaborn |
| **Notebooks** | Jupyter Notebook |
| **Entorno** | venv (Virtual Environment) |
| **Control de versiones** | Git/GitHub |

---

## 📊 Pipeline de Análisis

## 📊 Pipeline de Análisis

El flujo del proyecto sigue **buenas prácticas de analítica de datos** con modularización y reutilización de código:

```
1️⃣ Data Loading
   └─ Carga de CSV desde data/raw/
   
2️⃣ Data Exploration
   └─ Análisis de estructura, tipos, estadísticas
   
3️⃣ Data Quality Check
   ├─ Detección de valores nulos
   ├─ Identificación de duplicados
   └─ Validación de rangos
   
4️⃣ Data Cleaning (src/cleaning.py)
   ├─ Eliminación de columnas irrelevantes
   ├─ Tratamiento de valores nulos
   ├─ Conversión de tipos
   └─ Validación post-limpieza
   
5️⃣ Feature Engineering (src/features.py)
   ├─ total_nights: duración total de estancia
   ├─ total_guests: ocupación por reserva
   ├─ total_revenue: ingresos estimados (KPI crítico)
   └─ season: categorización estacional
   
6️⃣ EDA & Visualization
   ├─ Análisis de cancelaciones
   ├─ Lead time vs cancelación
   ├─ ADR por tipo de hotel
   ├─ Revenue por segmento
   ├─ Estacionalidad de demanda
   └─ Duración vs revenue
   
7️⃣ Business Insights
   └─ 6 insights clave + recomendaciones estratégicas
```

---

## 💡 Key Insights & Hallazgos

### 1️⃣ **Problema de Cancelaciones (~37%)**
- **Hallazgo**: Aproximadamente 1 de cada 3 reservas se cancela
- **Impacto**: Pérdida directa de ~37% del potencial de ingresos
- **Recomendación**: Implementar depósitos progresivos y confirmaciones automáticas

### 2️⃣ **Lead Time es Predictor Fuerte de Cancelación**
- **Hallazgo**: Reservas anticipadas (lead time > 90 días) tienen 87% más cancelaciones
- **Datos**: Canceladas: 166 días media vs Completadas: 89 días media
- **Recomendación**: Políticas de depósito según lead time, seguros de cancelación

### 3️⃣ **Diferenciación de Precios por Tipo de Hotel**
- **Hallazgo**: Hoteles urbanos tienen ADR 50%+ superior a resorts
- **Implicación**: Posicionamiento de mercado muy diferente
- **Recomendación**: Estrategias de pricing separadas por tipo

### 4️⃣ **Segmentación de Valor de Clientes**
- **Hallazgo**: Corporate genera 40%+ más revenue que OTA
- **Datos**: Corporate: €350/noche | OTA: €180/noche
- **Recomendación**: Programa de fidelización para Corporate, renegociar con OTA

### 5️⃣ **Estacionalidad Pronunciada (Variación 300%)**
- **Hallazgo**: Julio-agosto generan 300% más reservas que febrero
- **Patrón**: Picos en verano, valles en invierno
- **Recomendación**: Staffing dinámico, paquetes especiales para temporada baja

### 6️⃣ **Relación Linear Duration-Revenue**
- **Hallazgo**: Correlación fuerte (0.85+) entre noches y revenue
- **Implicación**: Incentivar estancias largas = maximizar revenue
- **Recomendación**: Descuentos por estancias extendidas, contratos corporativos

---

## 🚀 Recomendaciones Estratégicas

### Corto Plazo (1-3 meses) 🔴 CRÍTICA
- [ ] Implementar políticas de depósito progresivo según lead time
- [ ] Sistema de confirmaciones automáticas 2-4 semanas antes de llegada
- [ ] Desarrollo de seguros de cancelación flexible
- [ ] Ajuste dinámico de ADR por temporada y segmento

### Mediano Plazo (3-6 meses) 🟡 ALTA
- [ ] Modelo predictivo de cancelaciones con machine learning
- [ ] Programa de fidelización para segmento Corporate
- [ ] Renegociación de márgenes con OTAs
- [ ] Staffing dinámico según estacionalidad

### Largo Plazo (6-12 meses) 🟢 MEDIA
- [ ] Sistema de revenue management integrado
- [ ] Dashboard en tiempo real de KPIs
- [ ] Predictive analytics para overbooking
- [ ] Automatización de campañas por segmento

---

## 🚀 Cómo Ejecutar el Proyecto

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

**Opción B: Script Python**
```bash
python ./main.py
```

**Opción C: Ejecutar celdas específicas**
```bash
# Desde el directorio raíz
jupyter nbconvert --to notebook --execute notebooks/eda.ipynb
```

---

## 📈 Estadísticas del Dataset

| Métrica | Valor |
|---------|-------|
| **Registros totales** | 119,390 |
| **Características** | 32 (después de limpieza) |
| **Revenue total** | €34.46 millones |
| **Tasa de cancelación** | 37.04% |
| **Países representados** | 178 |
| **Segmentos de mercado** | 5 principales |
| **Período de datos** | Múltiples años |

---

## 📝 Documentación y Comentarios

El código está **completamente documentado** con:
- ✅ Docstrings en todas las funciones
- ✅ Comentarios explicativos en el análisis
- ✅ Markdown descriptivo en el notebook
- ✅ Insights explicados en lenguaje no técnico

### Archivos Principales

- **notebooks/eda.ipynb**: Notebook completo con 7 fases de análisis
- **src/cleaning.py**: Funciones de limpieza reutilizables
- **src/features.py**: Ingeniería de features modularizada
- **src/viz.py**: Funciones de visualización estandarizadas

---

## 🎓 Aprendizajes y Habilidades Demostradas

✅ **Análisis de Datos**
- EDA profesional y estructurado
- Análisis de correlaciones y patrones
- Identificación de outliers y anomalías

✅ **Data Wrangling**
- Limpieza de datos a escala
- Tratamiento de valores nulos
- Transformación de datos

✅ **Visualización**
- Gráficos informativos y profesionales
- Storytelling con datos
- Paletas de color adecuadas

✅ **Ingeniería de Features**
- Creación de variables de negocio
- Features correlacionadas con KPIs
- Normalización y transformación

✅ **Business Intelligence**
- Pensamiento orientado a negocio
- Extracción de insights accionables
- Recomendaciones estratégicas

✅ **Buenas Prácticas**
- Código modularizado y reutilizable
- Documentación clara
- Reproducibilidad garantizada

---

## 🔄 Próximos Pasos Posibles

1. **Machine Learning**: Modelo predictivo de cancelaciones
2. **Segmentación**: Clustering de clientes por comportamiento
3. **Dashboard**: Visualización interactiva con Plotly/Dash
4. **Forecasting**: Predicción de demanda por mes
5. **A/B Testing**: Validación de políticas propuestas

---

## 📚 Recursos Adicionales

- [Dataset en Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?resource=download)
- [Documentación Pandas](https://pandas.pydata.org/docs/)
- [Guía Seaborn](https://seaborn.pydata.org/)
- [Real Python - EDA](https://realpython.com/exploratory-data-analysis-python/)

---

## 📧 Contacto

**Autor**: Biel Nieto Juanes  
**Proyecto**: Hotel Booking Demand Analysis  
**GitHub**: [BielNietoJuanes](https://github.com/BielNietoJuanes)

---

## 📄 Licencia

Este proyecto utiliza el **Hotel Booking Demand Dataset** bajo licencia CC0 1.0 Universal (Dominio Público) de Kaggle.

El código del análisis está disponible bajo licencia MIT.

---
