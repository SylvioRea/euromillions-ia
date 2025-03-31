
import streamlit as st
import os

st.set_page_config(
    page_title="DEBUG - EuroMillions IA",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧪 DEBUG - EuroMillions App")

st.markdown("Ce test permet de vérifier si **les pages sont bien détectées** et si le **menu latéral s'affiche** sur tous les appareils.")

st.info("🔍 Si vous voyez cette page, Streamlit fonctionne.")

# Affichage des fichiers de page si accessibles
st.subheader("📄 Fichiers de pages présents :")
try:
    files = os.listdir("pages")
    if files:
        for f in files:
            st.write("✅", f)
    else:
        st.error("❌ Aucun fichier trouvé dans /pages/")
except Exception as e:
    st.error("❌ Impossible de lire le dossier /pages/")
    st.exception(e)

# Bouton test
if st.button("Clique ici pour voir si ça marche"):
    st.success("🎉 Le bouton fonctionne ! Streamlit fonctionne bien.")

st.warning("➡️ Sur mobile, vérifie si un bouton ☰ apparaît en haut à gauche pour ouvrir le menu.")
