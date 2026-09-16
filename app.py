import streamlit as st
import requests

# ============================================================
# Configuración de la página
# ============================================================
import math
import streamlit as st

st.title(" Área y Perímetro de Figuras")

figura = st.selectbox(
    "Elige una figura:",
    ["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo"],
)

st.markdown("---")

if figura == "Rectángulo":
    st.header("Rectángulo")
    st.markdown("**Fórmulas:**")
    st.latex(r"A = b \cdot h")
    st.latex(r"P = 2(b + h)")

    b = st.number_input("Base", min_value=0.0, value=5.0)
    h = st.number_input("Altura", min_value=0.0, value=3.0)

    if st.button("Calcular"):
        area = b * h
        perimetro = 2 * (b + h)
        st.success(f"Área = {area:.2f}")
        st.info(f"Perímetro = {perimetro:.2f}")

elif figura == "Cuadrado":
    st.header("Cuadrado")
    st.markdown("**Fórmulas:**")
    st.latex(r"A = l^2")
    st.latex(r"P = 4l")

    l = st.number_input("Lado", min_value=0.0, value=4.0)

    if st.button("Calcular"):
        area = l ** 2
        perimetro = 4 * l
        st.success(f"Área = {area:.2f}")
        st.info(f"Perímetro = {perimetro:.2f}")

elif figura == "Triángulo":
    st.header("Triángulo")
    st.markdown("**Fórmulas:**")
    st.latex(r"A = \frac{b \cdot h}{2}")
    st.latex(r"P = a + b + c")

    b = st.number_input("Base", min_value=0.0, value=6.0)
    h = st.number_input("Altura", min_value=0.0, value=4.0)
    a = st.number_input("Lado 1", min_value=0.0, value=5.0)
    c = st.number_input("Lado 2", min_value=0.0, value=5.0)

    if st.button("Calcular"):
        area = (b * h) / 2
        perimetro = a + b + c
        st.success(f"Área = {area:.2f}")
        st.info(f"Perímetro = {perimetro:.2f}")

elif figura == "Círculo":
    st.header("Círculo")
    st.markdown("**Fórmulas:**")
    st.latex(r"A = \pi r^2")
    st.latex(r"C = 2\pi r")

    r = st.number_input("Radio", min_value=0.0, value=3.0)

    if st.button("Calcular"):
        area = math.pi * r ** 2
        perimetro = 2 * math.pi * r
        st.success(f"Área = {area:.2f}")
        st.info(f"Circunferencia = {perimetro:.2f}")

elif figura == "Paralelogramo":
    st.header("Paralelogramo")
    st.markdown("**Fórmulas:**")
    st.latex(r"A = b \cdot h")
    st.latex(r"P = 2(a + b)")

    b = st.number_input("Base", min_value=0.0, value=6.0)
    h = st.number_input("Altura", min_value=0.0, value=4.0)
    a = st.number_input("Lado adyacente (a)", min_value=0.0, value=5.0)

    if st.button("Calcular"):
        area = b * h
        perimetro = 2 * (a + b)
        st.success(f"Área = {area:.2f}")
        st.info(f"Perímetro = {perimetro:.2f}")
