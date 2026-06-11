from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path("data/Titanic-Dataset.csv")


@st.cache_data
def load_data(uploaded_file=None) -> pd.DataFrame:
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)

    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    return pd.DataFrame()


def find_column(df: pd.DataFrame, *names: str) -> str | None:
    normalized_columns = {column.lower(): column for column in df.columns}
    for name in names:
        column = normalized_columns.get(name.lower())
        if column is not None:
            return column
    return None


st.set_page_config(
    page_title="Titanic Dashboard",
    layout="wide",
)

st.title("Titanic Dashboard")
st.caption("EDA interactivo del dataset del Titanic")

uploaded_file = st.sidebar.file_uploader("Sube un CSV del Titanic", type=["csv"])
df = load_data(uploaded_file)

if df.empty:
    st.info(
        "Para empezar, sube un CSV desde la barra lateral o guarda el dataset como "
        "`data/Titanic-Dataset.csv`."
    )
    st.stop()

st.sidebar.header("Filtros")

filtered_df = df.copy()
survived_column = find_column(filtered_df, "survived")
sex_column = find_column(filtered_df, "sex")
age_column = find_column(filtered_df, "age")
class_column = find_column(filtered_df, "class", "pclass")

if sex_column:
    sex_options = sorted(filtered_df[sex_column].dropna().unique())
    selected_sex = st.sidebar.multiselect("Sexo", sex_options, default=sex_options)
    filtered_df = filtered_df[filtered_df[sex_column].isin(selected_sex)]

if class_column:
    class_options = sorted(filtered_df[class_column].dropna().unique())
    selected_class = st.sidebar.multiselect(
        "Clase",
        class_options,
        default=class_options,
    )
    filtered_df = filtered_df[filtered_df[class_column].isin(selected_class)]

total_passengers = len(filtered_df)
survival_rate = None
average_age = None

if survived_column and total_passengers:
    survival_rate = filtered_df[survived_column].mean() * 100

if age_column:
    average_age = filtered_df[age_column].mean()

metric_cols = st.columns(3)
metric_cols[0].metric("Pasajeros", f"{total_passengers:,}")
metric_cols[1].metric(
    "Supervivencia",
    f"{survival_rate:.1f}%" if survival_rate is not None else "N/D",
)
metric_cols[2].metric(
    "Edad media",
    f"{average_age:.1f}" if pd.notna(average_age) else "N/D",
)

st.divider()

chart_cols = st.columns(2)

with chart_cols[0]:
    if survived_column and sex_column:
        survival_by_sex = (
            filtered_df.groupby(sex_column, as_index=False)[survived_column]
            .mean()
            .assign(**{survived_column: lambda data: data[survived_column] * 100})
        )
        fig = px.bar(
            survival_by_sex,
            x=sex_column,
            y=survived_column,
            labels={sex_column: "Sexo", survived_column: "Supervivencia (%)"},
            title="Supervivencia por sexo",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Faltan columnas `survived` y/o `sex` para este grafico.")

with chart_cols[1]:
    if survived_column and class_column:
        survival_by_class = (
            filtered_df.groupby(class_column, as_index=False)[survived_column]
            .mean()
            .assign(**{survived_column: lambda data: data[survived_column] * 100})
        )
        fig = px.bar(
            survival_by_class,
            x=class_column,
            y=survived_column,
            labels={class_column: "Clase", survived_column: "Supervivencia (%)"},
            title="Supervivencia por clase",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Faltan columnas de supervivencia o clase para este grafico.")

if age_column:
    fig = px.histogram(
        filtered_df,
        x=age_column,
        nbins=30,
        labels={age_column: "Edad"},
        title="Distribucion de edad",
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Vista previa de datos")
st.dataframe(filtered_df, use_container_width=True)
