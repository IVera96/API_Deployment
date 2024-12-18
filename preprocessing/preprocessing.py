import pandas as pd

original_data_path = (
    r"C:/OneDrive/Desktop/becode_projects/Deployment/data/immoweb_data_cleaned.csv"
)
df = pd.read_csv(original_data_path)


def preprocess_user_input(user_df):
    from sklearn.preprocessing import LabelEncoder

    le_property = LabelEncoder()
    le_property.fit(df["Type_of_Property"])
    user_df["Type_of_Property"] = le_property.transform([user_df["Type_of_Property"]])[
        0
    ]

    le_subtype = LabelEncoder()
    le_subtype.fit(df["Subtype_of_Property"])
    user_df["Subtype_of_Property"] = le_subtype.transform(
        [user_df["Subtype_of_Property"]]
    )[0]

    le_state_of_the_building = LabelEncoder()
    le_state_of_the_building.fit(df["State_of_the_Building"])
    user_df["State_of_the_Building"] = le_state_of_the_building.transform(
        [user_df["State_of_the_Building"]]
    )[0]

    le_province = LabelEncoder()
    le_province.fit(df["Province"])
    user_df["Province"] = le_province.transform([user_df["Province"]])[0]

    le_municipality = LabelEncoder()
    le_municipality.fit(df["Municipality"])
    user_df["Municipality"] = le_municipality.transform([user_df["Municipality"]])[0]

    return user_df
