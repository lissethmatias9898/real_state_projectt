import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Analisis de sector Inmobiliario",
    page_icon="https://www.flaticon.es/icono-gratis/analisis_8089662"
)
st.sidebar.title("Filtos")

#sidebar

cities = ["Guayaquil","Quito","Manta"]
with st.sidebar:
    city_selected = st.multiselect(
        "Ciudaddes disponible",
        options= cities,
        placeholder="Escoja la ciudad"
        
    )
    
    st.slider(
        label="Rango de precios",
        min_value=0,
        max_value=200000,
        step=1000
        
    )
    
#dataframe load =================================================================================================

df = pd.read_csv("houses.csv")

if city_selected:
    filas_seleccionadas = df[df["CITY"].isin(city_selected)] #es una condicion de filtrado
    df = filas_seleccionadas


max_price = int(df["PRICE_USD"].max())

#sidebar 2=========================================================================================================
with st.sidebar:
    min_value, max_value = st.slider(
        label = "rango de precios",
        min_value = 0,
        max_value = max_price,
        value = (0, max_price),
        step = 10000
    )

df = df[
    (df["PRICE_USD"]>= min_value)&
    (df["PRICE_USD"]<=max_value)
]

total_properties = len(df)
average_price = df["PRICE_USD"].mean()
median_price = df["PRICE_USD"].median()
average_area = df["CONSTRUCTION_AREA_SQM"].median()

#page =================================================================================================

st.title("Analisis de sector Inmobiliario")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total de propiedades",
        value=total_properties
    )
    
with col2:
    st.metric(
        label="Precio promedio",
        value=f"$ {average_price:,.2f} m²"
    )

with col3:
    st.metric(
        label="Mediana de precio",
        value=f"$ {median_price:,.2f}"
    )

with col4:
    st.metric(
        label="Area promedio",
        value=average_area
    )
  
col_map, col_df = st.columns(2)

# df = pd.DataFrame(
#     {
#         "latitude": [-2.19616],
#         "longitude": [-79.88621]
#     }
# )



with col_map:
    st.map(df)


with col_df:
    st.dataframe(
        df,
        hide_index= True,
        column_config={
            "ID":None,
            "TYPE":"Tipo",
            "BEDROOMS": "Habitaciones",
            "BATHROOMS": "Baños",
            "PARKING_SPOTS": "Parqueaderos",
            "CONSTRUCTION_AREA_SQM": "Área (m²)",
            "LATITUDE":None,
            "LONGITUDE":None,
            "CITY":"Ciudad",
            "PRICE_USD": st.column_config.NumberColumn(
                label="Precio",
                format="$ %d"
                
            ),
            "LINK": st.column_config.LinkColumn(
                label="Vinculo",
                display_text="ver"
            )
            
        }
    )