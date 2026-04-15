import streamlit as st
import pandas as pd

# 1. Configuration de la page (onglet du navigateur)
st.set_page_config(
    page_title="FraîchVrac App",
    page_icon="🥛",
    layout="centered"
)

# 2. Titre principal et style
st.title("🥛 FraîchVrac - Ton App Compagnon")
st.write("Bienvenue Marcel ! Trouve ton lait frais, local et sans déchet.")

# 3. Menu de navigation sur le côté (Sidebar)
st.sidebar.header("Menu")
menu = st.sidebar.radio(
    "Navigation", 
    ["📍 Trouver un distributeur", "🔍 Scanner & Provenance", "🎁 Ma Fidélité"]
)

# --- SECTION 1 : CARTE ET STOCKS ---
if menu == "📍 Trouver un distributeur":
    st.header("Où est mon lait local ?")
    st.write("Localise les distributeurs FraîchVrac les plus proches de toi.")
    
    # Données pour la carte (Coordonnées de test autour de Lille/Icam)
    # Utilisation de LAT et LON pour assurer la compatibilité
    map_data = pd.DataFrame({
        'LAT': [50.633, 50.629, 50.637],
        'LON': [3.058, 3.055, 3.065],
        'Nom': ['Marché Central', 'Place de la Mairie', 'Icam']
    })

    # Affichage de la carte avec un zoom forcé à 13 (ville/quartier)
    st.map(map_data, zoom=13)
    
    st.divider()
    
    st.subheader("📊 État des stocks en temps réel")
    stocks = pd.DataFrame({
        'Distributeur': ['Marché Central', 'Place de la Mairie', 'Icam'],
        'Distance': ['400m', '1.2km', '2.5km'],
        'Lait disponible (L)': [5, 25, 42],
        'Hygiène UV': ['✅ OK', '✅ OK', '⏳ Cycle en cours']
    })
    st.table(stocks)
    st.info("💡 Le distributeur du Marché Central est bientôt vide, dépêche-toi !")

# --- SECTION 2 : PROVENANCE ET SCAN ---
elif menu == "🔍 Scanner & Provenance":
    st.header("Traçabilité du produit")
    st.write("Scannez le QR Code sur la machine pour tout savoir sur votre lait.")
    
    # Simulation d'un scan
    if st.button("📱 Simuler le scan du QR Code"):
        st.success("✅ Connexion au distributeur établie !")
        
        st.subheader("🏠 Origine du Lait")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Producteur :** La Ferme des Peupliers")
            st.write("**Localisation :** Verlinghem (12 km)")
            st.write("**Label :** Agriculture Biologique 🌿")
        with col2:
            st.write("**Heure de collecte :** 05:30 ce matin")
            st.write("**Température cuve :** 3.2°C")
            st.write("**DLC :** Dans 4 jours")

        st.divider()
        
        st.subheader("🛡️ Hygiène & Sécurité")
        st.info("Ce distributeur a été désinfecté par lampes UV-C à 14h20 après le dernier passage.")
        
        st.subheader("💰 Ton impact")
        st.write("- **Prix :** 1.20€ / Litre")
        st.write("- **Économie :** -0.35€ par rapport au supermarché.")

# --- SECTION 3 : FIDÉLITÉ ---
elif menu == "🎁 Ma Fidélité":
    st.header("Espace Marcel - Fidélité")
    
    # Indicateurs clés
    col1, col2 = st.columns(2)
    col1.metric(label="Mes Points", value="150 pts", delta="+10 pts")
    col2.metric(label="Plastique évité", value="12 kg", delta="1.5 kg")
    
    st.write("### Ton prochain cadeau")
    st.write("Encore 50 points pour obtenir un litre gratuit !")
    st.progress(75)
    
    st.divider()
    
    st.write("🏆 **Derniers badges obtenus :**")
    st.write("- 🥛 **Apprenti Vracqueur** (1er achat)")
    st.write("- 🚜 **Ami des Fermiers** (5 achats locaux)")
