import streamlit as st
from PIL import Image
import os
from streamlit_pdf_viewer import pdf_viewer


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def show_pdf(file_path):
    pdf_viewer(file_path)

def show_svg(file_path):
    st.image(file_path, use_container_width=True)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    layout="wide",
    page_title="Cartographie Portage à Domicile"
)

st.title("Cartographie des communes - Portage à domicile")


# ============================================================
# REGIONS AND FILES (SVG + PDF)
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
        "Cebazat SISPA.pdf"
    ],
    "CCAS Beaumont": [
        "Beaumont1.svg",
        "Beaumont2.svg",
        "beaumont.pdf"
    ],
    "CIAS Riom Limagne et Volcans": [
        "CiAS Riom Limagne et Volcans1.svg",
        "CIAS Riom Limagne et Volcans.svg",
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
        "Aubiere.pdf",
    ],
    "SIVOM de la Vallée de l’Anse": [
        "SIVOM de la Vallée de l’Anse1.svg",
        "SIVOM de la Vallée de l’Anse2.svg",
        "SIVOM de la Vallée de l’Anse.pdf"
    ],
    "Com.Com. Chavanon Combrailles et Volcans": [
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur1.svg",
        "Com.Com. Chavanon Combrailles et Volcans.svg",
        "Com.Com. Chavanon Combrailles et Volcans Pontaumur.pdf"
    ],
}


# Helper function to render image files (SVG, PNG, JPG)
def render_image(file_path):
    if file_path.lower().endswith(".svg"):
        show_svg(file_path)
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(file_path)
        st.image(img, use_container_width=True)


# ============================================================
# ROW 1: Main Map (Left) & Selection Dropdown (Right)
# ============================================================

col_map, col_select = st.columns([1, 1])

with col_map:
    st.subheader("Carte des territoires")
    main_map_path = "carte.svg"

    if os.path.exists(main_map_path):
        render_image(main_map_path)
    else:
        st.warning(f"⚠️ Image introuvable : '{main_map_path}'")

with col_select:
    st.markdown("### 🔍 Sélectionnez une région :")
    selected_region = st.selectbox(
        "Choisissez une région :",
        list(regions.keys())
    )
    st.write(f"Région active : **{selected_region}**")

st.markdown("---")


# ============================================================
# FILE PROCESSING FOR SELECTED REGION
# ============================================================

file_paths = regions[selected_region]
valid_files = [f for f in file_paths if os.path.exists(f)]
image_files = [f for f in valid_files if f.lower().endswith((".svg", ".png", ".jpg", ".jpeg"))]
pdf_files = [f for f in valid_files if f.lower().endswith(".pdf")]


# ============================================================
# ROW 2: Geographical Region Map (Left) & Infographics (Right)
# ============================================================

col_geo, col_info = st.columns([1, 1])

# Left Side: Primary regional map (1st SVG/Image)
with col_geo:
    st.subheader(f"Carte géographique : {selected_region}")
    if image_files:
        render_image(image_files[0])
    else:
        st.warning("⚠️ Aucune carte disponible pour cette région.")

# Right Side: Infographic layout (2nd SVG/Image)
with col_info:
    st.subheader("Données Infographiques")
    if len(image_files) > 1:
        render_image(image_files[1])
    else:
        st.info("ℹ️ Pas d'infographie additionnelle pour cette région.")

st.markdown("---")


# ============================================================
# ROW 3: Améliorer File (Left) & Verbatim / PDF Container (Right)
# ============================================================

col_ameliorer, col_pdf_verbatim = st.columns([1, 1])

# Left Side: Persistent Améliorer file (supports .svg or .png)
with col_ameliorer:
    # Set to .svg by default; change to "ameliorer.png" if your file is PNG format
    always_visible_map = "ameliorer.svg" if os.path.exists("ameliorer.svg") else "ameliorer.png"
    
    if os.path.exists(always_visible_map):
        render_image(always_visible_map)
    else:
        st.warning(f"⚠️ Image permanente introuvable : '{always_visible_map}'")

# Right Side: PDF directly inside the Verbatim framed container
with col_pdf_verbatim:
    st.subheader("💬 Verbatim / Documents")
    if pdf_files:
        with st.container(border=True):
            show_pdf(pdf_files[0])
    else:
        st.info("ℹ️ Aucun document PDF associé disponible pour cette région.")
