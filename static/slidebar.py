import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

original_data_path = (
    r"./data/immoweb_data_cleaned.csv"
)
df = pd.read_csv(original_data_path)

IMG_SIDEBAR_PATH = f"./static/img.jpg"


def get_postal_code(df, province, municipality):
    postal_code = df[
        (df["Province"] == province) & (df["Municipality"] == municipality)
    ]["Locality"].values
    if postal_code.size > 0:
        return postal_code[0]
    return "Not found"


def add_sidebar(df, IMG_SIDEBAR_PATH):
    st.sidebar.header("Price Predictor `App 🏠`")
    image = np.array(Image.open(IMG_SIDEBAR_PATH))
    st.sidebar.image(image)
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    st.sidebar.write(
        "This Artificial Intelligence App predicts the price of a house/appartement given their corresponding parameters."
    )

    st.sidebar.subheader("Select the Parameters of the House/Appartement ✅:")

    # Tipo di proprietà
    type_of_property_map = {"Appartement": "APARTMENT", "House": "HOUSE"}
    type_of_property = st.sidebar.selectbox(
        "Choose the type of property", type_of_property_map
    )
    if type_of_property == "Appartement":
        subtype_of_property_map = {
            "Appartement": "APARTMENT",
            "Ground": "GROUND_FLOOR",
            "Duplex": "DUPLEX",
            "Grand floor": "GROUND_FLOOR",
            "Mixed building": "MIXED_USE_BUILDING",
            "Appartement block": "APARTMENT_BLOCK",
            "Flat studio": "FLAT_STUDIO",
            "Penthouse": "PENTHOUSE",
            "Triplex": "TRIPLEX",
            "Loft": "LOFT",
            "Service flat": "SERVICE_FLAT",
            "Kot": "KOT",
        }
    else:
        subtype_of_property_map = {
            "House": "HOUSE",
            "Mixed building": "MIXED_USE_BUILDING",
            "Villa": "VILLA",
            "Town house": "TOWN_HOUSE",
            "Bungalow": "BUNGALOW",
            "Mansion": "MANSION",
            "Country cottage": "COUNTRY_COTTAGE",
            "Chalet": "CHALET",
            "Farmhouse": "FARMHOUSE",
            "Manor house": "MANOR_HOUSE",
        }

    subtype_of_property = st.sidebar.selectbox(
        "Choose the type of sub-property", subtype_of_property_map
    )

    state_of_the_building_map = {
        "Good": "GOOD",
        "As new": "AS_NEW",
        "To renovate": "TO_RENOVATE",
        "To be done up": "TO_BE_DONE_UP",
        "Just renovated": "JUST_RENOVATED",
        "To restore": "TO_RESTORE",
    }
    state_of_the_building = st.sidebar.selectbox(
        "Choose the state of the building", state_of_the_building_map
    )


    Number_of_Rooms = st.sidebar.selectbox(f"Choose the number of rooms", (1, 2, 3, 4))

  
    Living_Area = st.sidebar.number_input(
        label="Enter your living space (m²)",
        min_value=12,
        max_value=155,
        value=50,
        step=1,
    )
    
    if type_of_property == "Appartement":
        Surface_area_plot_of_land=0.0
    else:
        Surface_area_plot_of_land=st.sidebar.number_input(
        label="Enter your surface ares plot of land (m²)",
        min_value=12,
        max_value=1000,
        value=50,
        step=1,
    )

  
    if Living_Area:
        try:
            Living_Area = float(Living_Area)
        except ValueError:
            st.sidebar.error("Please enter a valid number for Living Area.")


    Number_of_Facades = st.sidebar.selectbox(
        "Choose the number of facades", (1, 2, 3, 4, 5)
    )


    Swimming_Pool_map = {"No": 0.0, "Yes": 1.0}
    swimming_pool = st.sidebar.selectbox("Want a house with pool?", Swimming_Pool_map)


    Province_map = {
        "Flandre Orientale": "East Flanders",
        "Anvers": "Antwerp",
        "Bruxelles": "Brussels Capital",
        "Liège": "Liège",
        "Brabant Flamand": "Flemish Brabant",
        "Hainaut": "Hainaut",
        "Braban wallon": "Walloon Brabant",
        "Limbourg": "Limburg",
        "Namur": "Namur",
        "Luxembourg": "Luxembourg",
        "Flandre Occidentale": "Other",
    }
    province = st.sidebar.selectbox("Choose your province", Province_map)

 
    col_one_list = (
        df[df["Province"] == Province_map.get(province)].Municipality.unique().tolist()
    )
    selectbox_01 = st.sidebar.selectbox("Select the Municipality", col_one_list)

    if selectbox_01:
        postal_code = get_postal_code(df, Province_map.get(province), selectbox_01)
        if postal_code != "Not found":
            st.sidebar.write(f"The postal code for {selectbox_01} is: {postal_code}")
        else:
            st.warning(f"No postal code found for {selectbox_01}.")


    user_selections = {
        "Locality": postal_code,
        "Type_of_Property": type_of_property_map[type_of_property],
        "Subtype_of_Property": subtype_of_property_map[subtype_of_property],
        "State_of_the_Building": state_of_the_building_map[state_of_the_building],
        "Number_of_Rooms": Number_of_Rooms,
        "Living_Area": Living_Area,
        "Surface_area_plot_of_land": 0.0,
        "Number_of_Facades": Number_of_Facades,
        "Swimming_Pool": Swimming_Pool_map[swimming_pool],
        "Municipality": selectbox_01,
        "Province": Province_map[province],
        "Salary_prov_med": 21270.0,  # Placeholder value
        "Prix_m2_prov": 2864.0,  # Placeholder value
    }

    return user_selections
