import pandas as pd

original_data_path = (
    r"C:/OneDrive/Desktop/becode_projects/Deployment/data/immoweb_data_cleaned.csv"
)
df = pd.read_csv(original_data_path)
# data_clean=r'C:/OneDrive/Desktop/becode_projects/Deployment/data/Data_from_Edo'
# df=pd.read_csv(data_clean)
df.columns = df.columns.str.strip()
# print(df['Municipality'].value_counts())
# print(df['Locality'].value_counts())
# print(df['Subtype_of_Property'].value_counts())
# print(df['Municipality'].value_counts(ascending=False))
# print(df['Salary_prov_med'].median())
# print(df['Prix_m2_prov'].median())
# print(df['Surface_area_plot_of_land'].median())


# Filtra gli appartamenti

# print(df[df['Type_of_Property'] == 'APARTMENT']["State_of_the_Building"].unique())


# Price,Locality,Type_of_Property,Subtype_of_Property,State_of_the_Building,Number_of_Rooms,Living_Area,Fully_Equipped_Kitchen,Terrace,Garden,Surface_area_plot_of_land,Number_of_Facades,Swimming_Pool,Lift,Municipality,Province
citta = df[df["Type_of_Property"] == "APARTMENT"]["State_of_the_Building"]
print(citta.value_counts())


# print(facade_counts)
# print(df['Type_of_Property'].unique())  # Verifica i valori nella colonna
# print(df['Number_of_Facades'].unique())
# print(df['Subtype_of_Property'].unique())
# print(df['State_of_the_Building'].unique())
