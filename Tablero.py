import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

# Título
st.title("🖌️ Tablero para dibujo")

# Sidebar con propiedades
with st.sidebar:
    st.subheader("⚙️ Propiedades del Tablero")

    # Dimensiones
    st.subheader("📐 Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 1000, 600, 50)
    canvas_height = st.slider("Alto del tablero", 200, 800, 400, 50)

    # Herramienta de dibujo
    drawing_mode = st.selectbox(
        "🖍️ Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Configuración de estilo
    stroke_width = st.slider("✏️ Selecciona el ancho de línea", 1, 30, 10)
    stroke_color = st.color_picker("🎨 Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("🌌 Color de fondo", "#000000")

# Crear el canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",   # Color de relleno transparente
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}"
)

# Guardar y descargar dibujo
if canvas_result.image_data is not None:
    # Convertir a imagen PIL
    img = Image.fromarray((canvas_result.image_data).astype("uint8"))

    # Mostrar preview
    st.subheader("📷 Vista previa del dibujo")
    st.image(img, caption="Tu dibujo", use_container_width=True)

    # Botón de descarga
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="⬇️ Descargar dibujo en PNG",
        data=byte_im,
        file_name="mi_dibujo.png",
        mime="image/png"
    )
