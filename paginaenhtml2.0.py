import streamlit as st
import requests

# ==========================================================
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Información y Prevención del VIH en Colombia",
    page_icon="🎗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Key de DeepSeek y Configuración
DEEPSEEK_API_KEY = "REMOVED"
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

SYSTEM_PROMPT = """
Eres "InfoVIH", un asistente virtual educativo especializado EXCLUSIVAMENTE en brindar información clara, precisa y actualizada sobre el VIH (Virus de Inmunodeficiencia Humana) y el SIDA.

Tus principios son:
1. Brindas información basada en evidencia científica y en guías de organismos de salud reconocidos (OMS, ONUSIDA, CDC, ministerios de salud).
2. Hablas con un tono cálido, respetuoso, empático y libre de juicios o estigma.
3. Cubres temas como: formas de transmisión y NO transmisión, prevención (preservativo, PrEP, PEP), pruebas de detección, tratamiento antirretroviral, indetectable = intransmisible (I=I), vivir con VIH, derechos de las personas con VIH, y desmentir mitos comunes.
4. NUNCA diagnosticas a una persona ni das indicaciones de dosis de medicamentos. Para diagnóstico, tratamiento personalizado o resultados de pruebas, siempre remites a un médico, centro de salud o línea de atención especializada.
5. Si detectas angustia emocional, una posible exposición reciente de riesgo, o pensamientos de autolesión, respondes con calma, validas la emoción y recomiendas buscar ayuda profesional o de emergencia de inmediato.
6. Si te preguntan algo fuera del tema VIH/salud sexual, indicas amablemente que tu especialidad es el VIH y rediriges la conversación a ese tema.
7. Usas lenguaje sencillo, evitas tecnicismos innecesarios y explicas los términos médicos cuando los usas.

Recuerda siempre cerrar temas sensibles recordando que este chatbot no sustituye una consulta médica profesional.
"""

# ==========================================================
# BARRA LATERAL (NAVEGACIÓN)
# ==========================================================
st.sidebar.title("🎗️ Prevención VIH")
st.sidebar.markdown("Educando para salvar vidas en Colombia.")

opcion = st.sidebar.radio(
    "Navegación principal:",
    [
        "💬 Chatbot InfoVIH",
        "💡 Información Educativa",
        "💬 Testimonios",
        "🎥 Video Educativo",
        "🏢 Entidades de Apoyo"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("**Líneas de Atención Gratuita:**")
st.sidebar.markdown("📞 Línea Nacional: **192**")
st.sidebar.markdown("🚨 Emergencias: **123**")

# ==========================================================
# SECCIÓN: CHATBOT INFOVIH
# ==========================================================
if opcion == "💬 Chatbot InfoVIH":
    st.title("🎗️ InfoVIH Chatbot")
    st.caption("Asistente virtual confidencial y educativo sobre el VIH y salud sexual en Colombia.")
    
    st.warning("ℹ️ **Aviso:** Este asistente ofrece información educativa y **no reemplaza** una consulta médica profesional.")
    
    # Inicializar el historial de chat en la sesión
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "¡Hola! 👋 Soy **InfoVIH**. Puedes preguntarme sobre prevención, pruebas de detección, tratamiento, PrEP/PEP, o cualquier duda relacionada con el VIH. ¿En qué puedo ayudarte hoy?"
            }
        ]

    # Mostrar mensajes previos
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada del usuario
    if prompt := st.chat_input("Escribe tu duda sobre el VIH aquí..."):
        # Mostrar el mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Preparar la petición a DeepSeek usando 'requests'
        historial_api = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + historial_api,
            "temperature": 0.4
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }

        # Generar respuesta con la API
        with st.chat_message("assistant"):
            with st.spinner("Consultando información..."):
                try:
                    response = requests.post(DEEPSEEK_URL, json=payload, headers=headers, timeout=30)
                    
                    if response.status_code == 200:
                        respuesta_bot = response.json()["choices"][0]["message"]["content"]
                        st.markdown(respuesta_bot)
                        st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
                    else:
                        error_msg = f"❌ Error ({response.status_code}): No se pudo obtener respuesta del servidor."
                        st.error(error_msg)
                except Exception as e:
                    st.error(f"🔌 Error de conexión: {str(e)}")

    if st.button("🗑️ Limpiar conversación"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "¡Hola! 👋 Soy **InfoVIH**. ¿En qué puedo ayudarte hoy?"
            }
        ]
        st.rerun()

# ==========================================================
# SECCIÓN: INFORMACIÓN EDUCATIVA
# ==========================================================
elif opcion == "💡 Información Educativa":
    st.title("💡 ¿Qué debes saber sobre el VIH?")
    st.markdown("Información clara, científica y sin tabúes para jóvenes en Colombia.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💡 ¿VIH y SIDA son lo mismo?")
        st.write("""
        **No.** El **VIH** (Virus de Inmunodeficiencia Humana) ataca el sistema inmune. 
        El **SIDA** (Síndrome de Inmunodeficiencia Adquirida) es la etapa avanzada de la infección cuando no se recibe tratamiento oportuno.
        """)
        
        st.subheader("🧬 Indetectable = Intransmisible")
        st.write("""
        Una persona con VIH en Tratamiento Antirretroviral (TAR) que logra mantener una carga viral **indetectable** por más de 6 meses **no transmite** el virus por vía sexual.
        """)

    with col2:
        st.subheader("🛡️ Métodos de Prevención")
        st.write("""
        - Uso constante del preservativo (condón masculino/femenino).
        - **PrEP** (Profilaxis Preexposición): Pastilla preventiva antes de la exposición.
        - **PEP** (Profilaxis Post-exposición): Tratamiento de emergencia dentro de las primeras 72 horas tras un riesgo.
        """)
        
        st.subheader("🩺 Pruebas y Diagnóstico")
        st.write("""
        Hazte la prueba rápida de VIH gratis en tu EPS o mediante campañas comunitarias. Un diagnóstico a tiempo garantiza una expectativa y calidad de vida completamente normal.
        """)

# ==========================================================
# SECCIÓN: TESTIMONIOS
# ==========================================================
elif opcion == "💬 Testimonios":
    st.title("💬 Historias y Testimonios")
    st.markdown("Historias reales de personas que transforman estigmas en resiliencia y esperanza.")
    
    t1, t2, t3 = st.columns(3)
    
    with t1:
        st.info("**Laura, 23 años (Bogotá D.C.)**")
        st.write('"Descubrí mi diagnóstico tras una etapa difícil. Al principio sentí mucho temor por la desinformación, pero al iniciar mi tratamiento y contar con redes de apoyo, comprendí que el VIH no limita mis sueños."')
        
    with t2:
        st.info("**Andrés, 45 años (Armero, Tolima)**")
        st.write('"Aprendí a cuidar mi salud de forma constante. Hoy no solo mantengo mi carga viral indetectable, sino que dedico tiempo a acompañar a jóvenes en zonas rurales para que entiendan la importancia de la prevención."')

    with t3:
        st.info("**María, 28 años (Melgar, Tolima)**")
        st.write('"Gracias al acompañamiento oportuno de profesionales y organizaciones aliadas, entendí que un diagnóstico temprano hace la diferencia. Romper el silencio nos permite sanar."')

# ==========================================================
# SECCIÓN: VIDEO EDUCATIVO
# ==========================================================
elif opcion == "🎥 Video Educativo":
    st.title("🎥 Aprende en Video")
    st.markdown("Aprende de forma visual y pedagógica cómo prevenir e informarte correctamente.")
    st.video("https://www.youtube.com/watch?v=ofiCQqMCoAU")

# ==========================================================
# SECCIÓN: ENTIDADES DE APOYO
# ==========================================================
elif opcion == "🏢 Entidades de Apoyo":
    st.title("🏢 Entidades de Apoyo en Colombia")
    st.markdown("Organizaciones e instituciones donde puedes solicitar orientación, pruebas y acompañamiento:")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("🔗 **[AHF Colombia](https://ahfcolombia.org.co/)**: Pruebas rápidas gratuitas y asesoría.")
        st.markdown("🔗 **[Fundación EUDES](https://fundacioneudes.co/)**: Atención integral y acompañamiento.")
        st.markdown("🔗 **[Corporación Lucha Contra el Sida](https://cls.org.co/)**: Diagnóstico e investigación en Cali.")

    with col_b:
        st.markdown("🔗 **[Fundación Reviva](https://www.reviva.org.co/)**: Apoyo social y emocional.")
        st.markdown("🔗 **[En Bogotá se Puede Ser](https://enbogotasepuedeser.gov.co/)**: Políticas públicas de inclusión.")
        st.markdown("🔗 **[Fundación Alejandro A. Escobar](https://www.faae.org.co/)**: Proyectos de salud comunitaria.")