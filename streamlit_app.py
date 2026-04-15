import streamlit as st
import pandas as pd
import numpy as np

# Configuration de la page
st.set_page_config(page_title="FraîchVrac App", page_icon="🥛")

st.title("🥛 FraîchVrac - Ton App Compagnon")

# Menu de navigation sur le côté
menu = st.sidebar.radio("Navigation", ["📍 Trouver un distributeur", "🔍 Scanner & Provenance", "🎁 Ma Fidélité"])

if menu == "📍 Trouver un distributeur":
    st.header("Où est mon lait local ?")
    st.write("Localise les distributeurs FraîchVrac les plus proches de toi[cite: 49, 61].")
    
    # Création des données pour la carte (Exemple de coordonnées à Lille/Icam)
    map_data = pd.DataFrame({
        'lat': [50.633, 50.629, 50.637],
        'lon': [3.058, 3.055, 3.065],
        'nom': ['Marché Central', 'Place de la Mairie', 'Près de l\'Icam']
    })

    # Affichage de la carte 
    st.map(map_data)
    
    st.subheader("État des stocks en temps réel")
    stocks = pd.DataFrame({
        'Distributeur': ['Marché Central', 'Place de la Mairie', 'Icam'],
        'Distance': ['400m', '1.2km', '2.5km'],
        'Lait disponible (L)': [5, 25, 42],
        'Hygiène UV': ['✅ OK', '✅ OK', '⏳ Cycle en cours']
    })
    st.table(stocks)

elif menu == "🔍 Scanner & Provenance":
    st.header("Traçabilité du produit")
    st.write("Scannez le QR Code sur la machine pour tout savoir sur votre lait[cite: 43, 69].")
    
    if st.button("Simuler le scan du distributeur"):
        st.divider()
        st.subheader("🏠 Provenance & Origine")
        
        # Détails de provenance basés sur votre projet 
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Producteur :** Ferme des Peupliers")
            st.write("**Lieu :** Verlinghem (12 km)")
        with col2:
            st.write("**Collecte :** Ce matin à 05h30")
            st.write("**Label :** Agriculture Biologique")
            
        st.success("🛡️ Hygiène certifiée par lampes UV-C.")
        st.info("Ce lait est vendu 1.20€ / Litre (Économie de 0.30€ vs supermarché)[cite: 79].")

elif menu == "🎁 Ma Fidélité":
    st.header("Mes Points FraîchVrac")
    st.metric(label="Mes Points", value="150 pts")
    st.write("Marcel, tu as déjà évité l'utilisation de **12 bouteilles en plastique** ! [cite: 83]")
    st.progress(75)
