import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="FraîchVrac App", page_icon="🥛")

# Titre principal
st.title("🥛 FraîchVrac - Ton App Compagnon")
st.write("Bienvenue ! Trouve ton lait frais, local et sans déchet.")

# Menu de navigation sur le côté
menu = st.sidebar.radio("Navigation", ["📍 Trouver un distributeur", "🔍 Scanner un QR Code", "🎁 Ma Fidélité"])

if menu == "📍 Trouver un distributeur":
    st.header("Distributeurs à proximité")
    
    # Fausse base de données de distributeurs pour l'exemple
    data = pd.DataFrame({
        'Lieu': ['Place de la Mairie', 'Marché Central', 'Supermarché Bio'],
        'Stock Lait (L)': [15.5, 2.0, 40.0],
        'Statut Hygiène': ['Validé UV', 'Validé UV', 'Nettoyage en cours']
    })
    
    st.dataframe(data, hide_index=True)
    st.info("💡 Astuce : Le distributeur du Marché Central est presque vide !")

elif menu == "🔍 Scanner un QR Code":
    st.header("Traçabilité du produit")
    st.write("Simulons le scan d'un distributeur ou d'un pot...")
    
    if st.button("Simuler le scan du QR Code"):
        st.success("✅ Produit authentifié avec succès !")
        st.write("**Ferme d'origine :** La Ferme des Peupliers")
        st.write("**Date de collecte :** Aujourd'hui à 06h00")
        st.write("**Label :** Agriculture Biologique (AB)")

elif menu == "🎁 Ma Fidélité":
    st.header("Mes Points FraîchVrac")
    
    # Affichage stylisé des points
    st.metric(label="Points actuels", value="150 pts", delta="+10 pts (Dernier achat)")
    
    st.progress(75) # Barre de progression visuelle
    st.write("Encore 50 points pour obtenir 10% de réduction sur ton prochain plein !")
