
import streamlit as st
from PIL import Image
import os
from streamlit_pdf_viewer import pdf_viewer


# ============================================================
# FUNCTION TO DISPLAY PDF
# ============================================================

def show_pdf(file_path):
    pdf_viewer(file_path)


id="jlwm133"

# ============================================================
# FUNCTION TO DISPLAY SVG
# ============================================================

def show_svg(file_path):

    st.image(
        file_path,
        use_container_width=True
    )
# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    layout="wide",
    page_title="Cartographie Portage à Domicile"
)

st.title("Cartographie des communes - Portage à domicile")

# ============================================================
# REGIONS AND FILES
# ============================================================

regions = {

    "Com.Com. Ambert": [
        "ambert1.svg",
        "ambert2.svg",
        "ambert.pdf"
    ],

    "AVT Thiers": [
        "Thiers1.svg",
        "Thiers2.svg",
        "thiers.pdf"
    ],

    "CCAS Clermont-Ferrand": [
        "Clermont-Ferrand1.svg",
        "Clermont-Ferrand2.svg",
        "clermont-Ferrand.pdf"
    ],

    "CCAS Pont-du-Château": [
        "Pont-du-Chateau1.svg",
        "Pont-du-Chateau2.svg",
        "Pont-du-chateau.pdf"
    ],

    "Com.Com. Dômes Sancy Artense": [
        "Dômes Sancy Artense1.svg",
        "Dômes Sancy Artense2.svg",
        "ComCom-Dômes Sancy-Artense.pdf"
    ],

    "Cebazat-SISPA": [
        "Cebazat1.svg",
        "Cebazat2.svg",
        "Cebazat.pdf"
    ],

    "CCAS Beaumont": [
        "Beaumont1.svg",
        "Beaumont2.svg",
        "beaumont.pdf"
    ],

    "CiAS Riom Limagne et Volcans": [
        "CiAS Riom Limagne et Volcans1.svg",
        "CiAS Riom Limagne et Volcans2.svg",
        "CiAS Riom Limagne et Volcans.pdf"
    ],
    
    "SIVOS de Billom": [
        "Billom1.svg",
        "Billom2.svg",
        "billom.pdf"
    ],

    "Ceyrat Pôle Social et Proximité": [
        "Ceyrat1.svg",
        "Ceyrat2.svg",
        "ceyrat.pdf"
    ],

    "Etap-Auvergne 43": [
        "Etap auvergne1.svg",
        "Etap auvergne2.svg",
        "etap-auvergne.pdf"
    ],

    "Mond'Arverne Communauté": [
        "Mond'arverne1.svg",
        "Mond'arverne2.svg",
        "mondarverne.pdf"
    ],

    "CCAS Aubiere": [
        "Aubiere1.svg",
        "Aubiere2.svg",
        "aubiere.pdf"
    ],

    "SIVOM de la Vallée de l’Anse": [
        "SIVOM de la Vallée de l’Anse1.svg",
        "SIVOM de la Vallée de l’Anse2.svg",
        "SIVOM de la Vallée de l’Anse.pdf"
    ],

    "Com.Com. Chavanon Combrailles et Volcans Pontaumur": [
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur1.svg",
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur2.svg",
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur.pdf"
    ],
}

# ============================================================
# LAYOUT
# ============================================================

col1, col2 = st.columns([1, 1])

# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    st.subheader("Carte des territoires")

    main_map_path = "carte.svg"

    if os.path.exists(main_map_path):

        if main_map_path.lower().endswith(".svg"):
            show_svg(main_map_path)

        else:
            st.image(main_map_path, use_container_width=True)

    else:
        st.warning(f"⚠️ Image introuvable : '{main_map_path}'")

    st.markdown("### 🔍 Sélectionnez une région :")

    selected_region = st.selectbox(
        "Choisissez une région :",
        list(regions.keys())
    )

# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    st.subheader(f"Infographies : {selected_region}")

    file_paths = regions[selected_region]

    for file_path in file_paths:

        if os.path.exists(file_path):

            # SVG DISPLAY
            if file_path.lower().endswith(".svg"):
                show_svg(file_path)

            # PNG / JPG DISPLAY
            elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
                img = Image.open(file_path)
                st.image(img, use_container_width=True)

            # PDF DISPLAY
            elif file_path.lower().endswith(".pdf"):
                show_pdf(file_path)

            else:
                st.warning(f"Format non supporté : {file_path}")

        else:
            st.error(f"⚠️ Fichier introuvable : '{file_path}'")
