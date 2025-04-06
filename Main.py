import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#from streamlit_extras.metric_cards import style_metric_cards
import warnings
warnings.filterwarnings('ignore')



Page_one = st.Page(
    page = "Pages/Dataset.py",
    title= "Dataset"
)

Page_two = st.Page(
    page = "Pages/Visualisation.py",
    title= "Visualisation"
)

Page_three = st.Page(
    page = "Pages/Analyse.py",
    title= "Exploration de données"
)

Pages = st.navigation([Page_one,Page_two,Page_three])



def get_Dataset():
    file = st.file_uploader(label='Importez votre fichier', key="Main")
    if file is not None:
        Data = pd.read_csv(file)
        st.write(Data.head())
    else:
        None
    return Data
Data = get_Dataset()
#st.dataframe(Data.head())

if "df" not in st.session_state:
    st.session_state["df"]=Data
if Pages.title == "Dataset":
    Data = st.session_state["df"]
    option = st.selectbox(
        "Choisissez une option",
        ('Info','Description','Variables numériques', 'Variables catégorielles'),)

    if option == "Info":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader('Explorez le dataset')
            Informations = st.radio( "Découvrez votre dataset",
                options = ['Taille du dataset', 'Les variables', 'La description']
            )
            if Informations == "Taille du dataset":
                st.write(Data.shape)
                st.write(Data.info)
            elif Informations ==  "Les variables":
                #st.write(Data.info())
                Type = Data.dtypes
                st.write(Type)
            elif Informations == 'La description':
                st.write(Data.describe(include="all"))
            else:
                None

Pages.run()