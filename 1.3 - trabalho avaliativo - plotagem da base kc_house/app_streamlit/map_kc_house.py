#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import folium

# imports streamlit
import streamlit as st
from streamlit_folium import folium_static

def create_map(dataset, max_desired_price, max_acceptable_price):
    map = folium.Map(location=[dataset['lat'].mean(), dataset['long'].mean()], zoom_start=10)
    
    for index, row in dataset.iterrows():
        
        if row['price'] <= max_desired_price:
            color = 'green'
        elif row['price'] <= max_acceptable_price:
            color = 'orange'
        else:
            color = 'red'

        
        if row['price'] <= max_acceptable_price:
            folium.CircleMarker(
                location=[row['lat'], row['long']],
                radius=5,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=f"Preço: ${row['price']}"
            ).add_to(map)
    return map

# ------------------ CONSTRUÇÃO DA APLICAÇÃO WEB -----------------------------

# Título do aplicativo
st.title("Análise de Preços de Casas")

# carregando dados
arquivo = 'kc_house_data.csv'
dataset = pd.read_csv(arquivo, sep=',' ,header=0)
dataset = dataset[dataset['price'] <= 1000000]

# Entradas do usuário
max_desired_price = st.slider("Valor máximo desejavel", min_value=int(dataset['price'].min()), max_value=int(dataset['price'].max()))
max_acceptable_price = st.slider("Valor máximo aceitavel", min_value=int(dataset['price'].min()), max_value=int(dataset['price'].max()))

# Plotagem do mapa
if st.button("Plotar Mapa"):
    mapa = create_map(dataset, max_desired_price, max_acceptable_price)
    folium_static(mapa)



## DIVINDO A TELA EM COLUNAS --------------------------------
# col1, col2 = st.columns([1, 3])

# with col1:
#     st.header("Parâmetros")
#     max_desired_price = st.slider("Valor máximo desejável", min_value=int(dataset['price'].min()), max_value=int(dataset['price'].max()))
#     max_acceptable_price = st.slider("Valor máximo aceitável", min_value=int(dataset['price'].min()), max_value=int(dataset['price'].max()))
#     plot_button = st.button("Plotar Mapa")

# with col2:
#     if plot_button:
#         st.header("Mapa")
#         mapa = create_map(dataset, max_desired_price, max_acceptable_price)
#         folium_static(mapa)