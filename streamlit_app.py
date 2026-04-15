import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(
    page_title="FraîchVrac App",
    page_icon="🥛",
    layout="centered"
)

# 2. Titre principal avec de la couleur
st.title("🥛 :blue[FraîchVrac] - Ton App Compagnon")
st.markdown("Bienvenue **:orange[Marcel]** ! Trouve ton lait frais, local et sans déchet.")

# 3. Menu de navigation (Sidebar)
st.sidebar.header("📋 :violet[Menu]")
menu = st.sidebar.radio(
    "Navigation", 
    ["📍 Trouver un distributeur", "🔍 Scanner & Provenance", "🫙 Préparer ma visite", "🎁 Ma Fidélité"]
)

# --- SECTION 1 : CARTE ET STOCKS ---
if menu == "📍 Trouver un distributeur":
    st.header(":green[Où est mon lait local ?]")
    st.write("Localise les distributeurs FraîchVrac les plus proches de toi[cite: 67].")
    
    map_data = pd.DataFrame({
        'latitude': [50.633, 50.629, 50.637],
        'longitude': [3.058, 3.055, 3.065]
    })

    st.map(map_data, zoom=13, size=20)
    st.divider()
    
    st.subheader("📊 :blue[État des stocks en temps réel]")
    stocks = pd.DataFrame({
        'Distributeur': ['Marché Central', 'Place de la Mairie', 'Icam'],
        'Distance': ['400m', '1.2km', '2.5km'],
        'Lait disponible (L)': [5, 25, 42],
        'Hygiène UV': ['✅ OK', '✅ OK', '⏳ En cours']
    })
    st.table(stocks)
    st.warning("💡 **Attention :** Le distributeur du Marché Central est bientôt vide !")

# --- SECTION 2 : PROVENANCE ET SCAN ---
elif menu == "🔍 Scanner & Provenance":
    st.header(":violet[Traçabilité du produit]")
    st.write("Scannez le QR Code sur la machine pour tout savoir sur votre lait[cite: 69].")
    
    if st.button("📱 Simuler le scan du QR Code"):
        st.success("✅ Connexion au distributeur établie !")
        
        st.subheader("🏠 :green[Origine du Lait]")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Producteur :** :orange[La Ferme des Peupliers]")
            st.write("**Localisation :** Verlinghem (12 km)")
            st.write("**Label :** :green[Agriculture Biologique 🌿]")
        with col2:
            st.write("**Heure de collecte :** :blue[05:30 ce matin]")
            st.write("**Température cuve :** :blue[3.2°C]")
            st.write("**DLC :** :red[Dans 4 jours]")

        st.divider()
        
        st.subheader("🛡️ :blue[Hygiène & Sécurité]")
        st.info("Ce distributeur a été désinfecté par lampes UV-C après le dernier passage[cite: 45].")

# --- SECTION 3 : PRÉPARER MA VISITE (NOUVEAU) ---
elif menu == "🫙 Préparer ma visite":
    st.header(":blue[Gérer mon budget et mes bocaux]")
    st.write("Pour que ce soit plus simple une fois devant la machine, anticipe tes achats ici !")

    st.subheader("1️⃣ :orange[Mes contenants]")
    contenant = st.selectbox(
        "Quel pot vas-tu amener aujourd'hui ? ", 
        ["Bouteille en verre 1L (Tare: 450g)", "Bocal 500ml (Tare: 250g)", "Je n'ai rien, je prendrai une consigne sur place [cite: 47]"]
    )

    st.subheader("2️⃣ :green[Estimer mon prix]")
    st.write("Le prix est de **1.20€ / Litre** (soit 0.12€ les 100ml).")
    
    # Curseur interactif pour choisir la quantité
    quantite_ml = st.slider("Quelle quantité de lait souhaites-tu tirer ? (en ml) [cite: 70]", min_value=100, max_value=2000, value=1000, step=100)
    
    # Calcul automatique
    prix_estime = (quantite_ml / 1000) * 1.20
    
    st.success(f"💶 **Prix estimé pour {quantite_ml} ml : {prix_estime:.2f} €**")
    st.info("Pas de surprises : devant la machine, tu pourras t'arrêter exactement quand tu le souhaites ! ")

# --- SECTION 4 : FIDÉLITÉ ---
elif menu == "🎁 Ma Fidélité":
    st.header(":orange[Espace Marcel - Fidélité]")
    
    col1, col2 = st.columns(2)
    col1.metric(label="Mes Points", value="150 pts", delta="+10 pts")
    col2.metric(label="Plastique évité", value="12 kg", delta="1.5 kg")
    
    st.write("### :violet[Ton prochain cadeau]")
    st.write("Encore **:red[50 points]** pour obtenir un litre gratuit ! [cite: 54]")
    st.progress(75)
    
    st.divider()
    
    st.write("🏆 **:orange[Derniers badges obtenus :]**")
    st.write("- 🥛 **Apprenti Vracqueur** (1er achat)")
    st.write("- 🚜 **Ami des Fermiers** (5 achats locaux)")
