import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import joblib
from static.create_graphs_feedback import (
    create_bar_chart,
    create_boxplot,
    create_histogram,
    feedback_section,
    save_feedback,
    validate_inputs
)
from static.inverse_scaler import my_inverse_scaler
from preprocessing.preprocessing import preprocess_user_input
from static.slidebar import add_sidebar, get_postal_code



original_data_path = (
    r"C:/OneDrive/Desktop/becode_projects/Deployment/data/immoweb_data_cleaned.csv"
)
df = pd.read_csv(original_data_path)

IMG_SIDEBAR_PATH = f"./static/img.jpg"
model_path =f"./model/model_simple_no_out_allF_SDV_BEST.h5"
scaler_path=f'./model/scaler.save'

model = load_model(model_path)
#
scaler = joblib.load("scaler_path)

st.set_page_config(
    page_title="House Price Analysis 🏡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# User input
user_selections = add_sidebar(df, IMG_SIDEBAR_PATH)
# st.write("User Selections:", user_selections)

required_features = [
    "Locality",
    "Type_of_Property",
    "Subtype_of_Property",
    "State_of_the_Building",
    "Number_of_Rooms",
    "Living_Area",
    "Surface_area_plot_of_land",
    "Number_of_Facades",
    "Swimming_Pool",
    "Municipality",
    "Province",
    "Salary_prov_med",
    "Prix_m2_prov",
]

# Verifica se i dati dell'utente sono completi e validi prima di proseguire
if not validate_inputs(user_selections, required_features):
    st.stop()


# if st.button("Calculate Price 🏚️"):
#     if validate_inputs(user_selections, required_features):
#         # Procedi con il calcolo

# # Create DataFrame from user input
#         user_df = pd.DataFrame([user_selections])
#         # st.write("Dataframe prima della   trasformazione:", user_df)
#         # Apply necessary transformations (Label Encoding)
#         user_df=preprocess_user_input(user_df)
#         # st.write("Dataframe dopo la  trasformazione:", user_df)
#         # Add a new features because my scaler expects 14 features and the user_df have have only 13
#         user_df.insert(0, 'target', 0)


#         X_user=np.array(user_df)
#         X_user_scaled = scaler.transform(X_user)

#         #Select only the 13 features
#         X_user_selected = X_user_scaled[0][1:]

#         X_test_reshaped =X_user_selected.reshape(1, -1)

#         result=model.predict(X_test_reshaped)
#         # print(result)

#         prediction = my_inverse_scaler(result, X_user_selected)
#         pred_result = round(prediction[0], 2)
#         print("Predizione finale:", round(prediction[0],2))
#         st.metric(label=f"Price 🏚️:", value=f"{pred_result}", delta="Euros (€)")

#     else:
#         st.error("Some required inputs are missing. Please check your selections.")


def main():
    with st.container():
        # Titolo e descrizione iniziale
        st.title("House Price Predictor 🏡")
        st.write(
            "This App predicts using a DNN Machine Learning Model the Price in Euros (€) of a House or Appartement. You can also Update the measurements by hand using sliders in the sidebar."
        )
        st.markdown("<hr/>", unsafe_allow_html=True)

        # Prezzo centrato
        # pred_result = round(prediction[0], 2)
        # pred_result = f"{pred_result}€"

        # st.markdown("### Result of Prediction ")
        st.markdown(
            "<div style='text-align: center; font-size: 24px; font-weight: bold;'>Machine Learning Model Result ✅ 💸:</div>",
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns(
            [1, 2, 1]
        )  # Creazione di colonne (centrale più larga)
        with col2:  # Mettere il widget metric nella colonna centrale
            if st.button("Calculate Price 🏚️"):
                if validate_inputs(user_selections, required_features):
                    # Procedi con il calcolo

                    # Create DataFrame from user input
                    user_df = pd.DataFrame([user_selections])
                    # st.write("Dataframe prima della   trasformazione:", user_df)
                    # Apply necessary transformations (Label Encoding)
                    user_df = preprocess_user_input(user_df)
                    # st.write("Dataframe dopo la  trasformazione:", user_df)
                    # Add a new features because my scaler expects 14 features and the user_df have have only 13
                    user_df.insert(0, "target", 0)

                    X_user = np.array(user_df)
                    X_user_scaled = scaler.transform(X_user)

                    # Select only the 13 features
                    X_user_selected = X_user_scaled[0][1:]

                    X_test_reshaped = X_user_selected.reshape(1, -1)

                    result = model.predict(X_test_reshaped)

                    prediction = my_inverse_scaler(result, X_user_selected)
                    pred_result = round(prediction[0], 2)
                    print("Predizione finale:", round(prediction[0], 2))
                    st.metric(
                        label=f"Price 🏚️:", value=f"{pred_result}", delta="Euros (€)"
                    )

                else:
                    st.error(
                        "Some required inputs are missing. Please check your selections."
                    )

    with st.container():
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown("### Graphs Area 📊")

        # Prima riga con il primo grafico
        col1, col2, col3 = st.columns([1, 2, 1])  # Colonna centrale più larga
        with col2:
            st.markdown("#### Price Distribution")
            create_histogram(df)

        # Seconda riga con il secondo grafico
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("#### Price Distribution by Property Type")
            create_boxplot(df)

        # Terza riga con il terzo grafico
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("#### Prices by Municipality")
            create_bar_chart(df)
    feedback = feedback_section()
    save_feedback(feedback)


if __name__ == "__main__":
    main()

    print("App Running!")
