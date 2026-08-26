import streamlit as st
import requests

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="wide"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🌤️ Weather App")

st.sidebar.write("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Weather", "About"]
)

st.sidebar.divider()

st.sidebar.info(
    "This application uses Streamlit as the frontend "
    "and FastAPI as the backend."
)

# ---------------- HOME PAGE ----------------

if page == "Home":

    st.title("🌤️ Weather Application")

    st.subheader("Welcome!")

    st.write(
        """
        This application demonstrates how Streamlit and FastAPI
        can work together.

        **Streamlit → Frontend**

        **FastAPI → Backend**

        **Render → Deployment**
        """
    )

    st.success("Application is running successfully!")

# ---------------- WEATHER PAGE ----------------

elif page == "Weather":

    st.title("🌦️ Check Weather")

    st.write("Enter a city name to get weather information.")

    city = st.text_input(
        "Enter City Name",
        placeholder="Example: Hyderabad"
    )

    if st.button("Get Weather"):

        if city:

            # Replace this with your actual Render URL
            url = "https://str-fst.onrender.com"

            try:

                response = requests.get(
                    url,
                    params={"city": city}
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success("Weather information received!")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "City",
                            data["city"]
                        )

                    with col2:
                        st.metric(
                            "Temperature",
                            f'{data["temperature"]} °C'
                        )

                    with col3:
                        st.metric(
                            "Condition",
                            data["condition"]
                        )

                else:
                    st.error("Unable to get weather information.")

            except requests.exceptions.RequestException:
                st.error(
                    "Could not connect to the FastAPI server."
                )

        else:

            st.warning("Please enter a city name.")

# ---------------- ABOUT PAGE ----------------

elif page == "About":

    st.title("ℹ️ About")

    st.write(
        """
        ### Technology Used

        - 🐍 Python
        - ⚡ FastAPI
        - 🎨 Streamlit
        - 🚀 Render
        - 📦 GitHub
        - 🌐 HTTP

        ### Application Architecture

        Streamlit acts as the frontend.

        FastAPI acts as the backend API.

        Render hosts the FastAPI application.

        GitHub stores the project source code.
        """
    )

    st.info(
        "Streamlit sends HTTP requests to the FastAPI backend "
        "and displays the response to the user."
    )
