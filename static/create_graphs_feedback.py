import streamlit as st
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px


def create_histogram(df):
    plt.figure(figsize=(5, 3))
    plt.hist(df["Price"], color="skyblue", edgecolor="black")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    st.pyplot(plt)


# Function to create a box plot for prices by property type
def create_boxplot(df):
    plt.figure(figsize=(5, 3))
    sns.boxplot(x="Type_of_Property", y="Price", data=df)
    st.pyplot(plt)


# Function to create an interactive bar chart for prices by municipality
def create_bar_chart(df):
    fig = px.bar(df, x="Municipality", y="Price")
    st.plotly_chart(fig)


# Funzione per il feedback dell'utente
def feedback_section():
    st.subheader("Feedback on Prediction 💬")
    feedback = st.text_area("Tell us how we can improve the prediction:")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")


def save_feedback(feedback):
    feedback_path = "feedback.txt"
    with open(feedback_path, "a") as file:
        file.write(f"{feedback}\n")
    st.write("Feedback saved successfully!")


import streamlit as st


# Funzione per validare le informazioni
def validate_inputs(user_selections, required_features):
    """
    Verifica che tutte le feature richieste siano presenti nei dati dell'utente.

    Args:
        user_selections (dict): I dati forniti dall'utente.
        required_features (list): Le feature che devono essere fornite dall'utente.

    Returns:
        bool: True se tutte le feature sono valide, False altrimenti.
    """
    missing_features = [
        feature
        for feature in required_features
        if feature not in user_selections or user_selections[feature] is None
    ]
    if missing_features:
        st.error(
            f"The following required inputs are missing: {', '.join(missing_features)}"
        )
        return False
    return True
