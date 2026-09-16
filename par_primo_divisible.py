import math
import streamlit as st

st.title("🔢 Par o Impar, Primo y Divisible")

st.markdown("Ingresa un número y descubre si es **par/impar**, **primo** y si es **divisible** por otro número.")

n = st.number_input("Número a analizar (n)", min_value=0, value=7, step=1)
d = st.number_input("Divisor (d)", min_value=1, value=2, step=1)

if st.button("Analizar"):
    st.markdown("---")

    # 1. Par o impar
    if n % 2 == 0:
        st.success(f"✅ {n} es PAR (porque {n} ÷ 2 tiene resto 0)")
    else:
        st.warning(f"🔸 {n} es IMPAR (porque {n} ÷ 2 tiene resto 1)")

    # 2. Primo o no
    if n < 2:
        es_primo = False
    else:
        es_primo = True
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                es_primo = False
                break

    if es_primo:
        st.success(f"✅ {n} es PRIMO (solo es divisible entre 1 y él mismo)")
    else:
        st.warning(f"🔸 {n} NO es primo (tiene divisores además de 1 y él mismo)")

    # 3. Divisible por d
    if n % d == 0:
        st.success(f"✅ {n} es DIVISIBLE por {d} → {n} ÷ {d} = {n // d} (resto 0)")
    else:
        st.warning(f"🔸 {n} NO es divisible por {d} → el resto de la división es {n % d}")

    st.markdown("---")
    st.caption("Regla clave: un número es divisible por otro cuando el resto (módulo %) de la división es 0.")

