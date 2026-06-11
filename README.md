# Titanic Dashboard

Dashboard interactivo en Streamlit para explorar el dataset del Titanic. El proyecto parte del EDA realizado en el notebook y convierte algunos hallazgos iniciales en una app visual con filtros, metricas y graficos.

## Estructura del proyecto

```text
Titanic-Dashboard/
|-- app.py
|-- data/
|   |-- Titanic-Dataset.csv
|-- notebooks/
|   |-- El_Dataset_Titanic_Jose_Melo.ipynb
|-- requirements.txt
|-- requirements/
|   |-- base.txt
|   |-- dev.txt
|   |-- prod.txt
```

## Archivos principales

- `app.py`: aplicacion principal de Streamlit.
- `data/Titanic-Dataset.csv`: dataset usado por la app.
- `notebooks/El_Dataset_Titanic_Jose_Melo.ipynb`: notebook con el EDA del Titanic.
- `requirements.txt`: dependencias para Streamlit Cloud.
- `requirements/dev.txt`: dependencias para trabajar en local.

## Requisitos

- Python 3.10 o superior
- pip

## Instalacion local

Desde la carpeta del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements/dev.txt
```

Si PowerShell bloquea la activacion del entorno virtual, ejecuta una vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Despues vuelve a activar el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Ejecutar en Streamlit

Con el entorno virtual activado, ejecuta:

```powershell
streamlit run app.py
```

Streamlit abrira la app en el navegador. Normalmente estara disponible en:

```text
http://localhost:8501
```

## Dataset

La app carga automaticamente:

```text
data/Titanic-Dataset.csv
```

Tambien puedes subir otro CSV desde la barra lateral de la app. El dataset actual incluye columnas como:

- `Survived`
- `Pclass`
- `Sex`
- `Age`
- `Fare`
- `Embarked`

## Publicar en Streamlit Cloud

1. Sube este repositorio a GitHub.
2. Entra en Streamlit Cloud.
3. Crea una nueva app desde el repositorio.
4. Selecciona `app.py` como archivo principal.
5. Streamlit Cloud instalara las dependencias desde `requirements.txt`.

## Siguientes mejoras

- Incorporar mas graficos del notebook EDA.
- Anadir limpieza de datos en un modulo separado.
- Mostrar conclusiones del analisis dentro de la app.
