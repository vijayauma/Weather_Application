import streamlit as st
import requests

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="FastAPI Dashboard",
    page_icon="🚀",
    layout="centered"
)

# -------------------------------
# FastAPI URL
# -------------------------------
FASTAPI_URL = "https://str-fst.onrender.com"
# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #ddd;
    background-color: #ffffff;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown(
    '<div class="title">🚀 FastAPI Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Streamlit Frontend connected with FastAPI Backend</div>',
    unsafe_allow_html=True
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 Navigation")

option = st.sidebar.radio(
    "Choose an option",
    ["Home", "Name", "Weather"]
)

# -------------------------------
# HOME
# -------------------------------
if option == "Home":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🏠 Welcome")

    if st.button("Connect to FastAPI"):

        try:
            response = requests.get(
                FASTAPI_URL + "/",
                timeout=10
            )

            if response.status_code == 200:

                data = response.json()

                st.success("FastAPI connected successfully! ✅")

                st.info(data["message"])

            else:
                st.error("FastAPI returned an error.")

        except requests.exceptions.RequestException:
            st.error("❌ Unable to connect to FastAPI.")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------
# NAME
# -------------------------------
elif option == "Name":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 Get Name")

    if st.button("Get Name"):

        try:
            response = requests.get(
                FASTAPI_URL + "/name",
                timeout=10
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Name received successfully!")

                st.markdown(
                    f"### 👋 Hello, {data['name'].title()}!"
                )

            else:
                st.error("Unable to get name.")

        except requests.exceptions.RequestException:
            st.error("❌ Unable to connect to FastAPI.")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------
# WEATHER
# -------------------------------
elif option == "Weather":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🌤️ Weather Information")

    city = st.text_input(
        "Enter City Name",
        placeholder="Example: Hyderabad"
    )

    if st.button("Get Weather"):

        if city:

            try:

                response = requests.get(
                    FASTAPI_URL + "/weather",
                    params={"city": city},
                    timeout=10
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success("Weather details received! 🌤️")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "🏙️ City",
                            data["city"].title()
                        )

                    with col2:
                        st.metric(
                            "🌡️ Temperature",
                            f"{data['temperature']}°C"
                        )

                    with col3:
                        st.metric(
                            "☀️ Condition",
                            data["condition"].title()
                        )

                else:
                    st.error("Unable to get weather details.")

            except requests.exceptions.RequestException:
                st.error("❌ Unable to connect to FastAPI.")

        else:
            st.warning("Please enter a city name.")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------
# Footer
# -------------------------------
st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit + FastAPI"
)
