import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
#from streamlit_extras.metric_cards import style_metric_cards




st.title("Exploration de données")
Data = st.session_state["df"]
#st.title("Analyse et exploration de données")
#st.write(Data.head())
st.sidebar.subheader('Exploration de données',divider=True)
Menu = ['Analyses statistiques','Manipulation de données','Data cleaning','Filtrez votre dataset','Group by']
Menu_box = st.sidebar.selectbox('Explorez votre dataset',Menu)

#Analyses statistiques
if Menu_box == "Analyses statistiques":
    Menu_analyse_statitiques = st.selectbox("Vos options",('Moyenne','Valeur max','Valeur min','Somme','Médiane','Quartile'))
    if Menu_analyse_statitiques == "Moyenne":
        
        Variables_num = Data.select_dtypes(['int','float']).columns
        #st.write(Data[Variables_num].mean)
        Menu = st.selectbox("Choisissez une variable",Variables_num)
        Mean = st.write(Data[Menu].mean().round(2))
        #Menu.metric(Label ="Moyenne", value=Mean)

    elif Menu_analyse_statitiques == "Valeur max":
        Variables_num = Data.select_dtypes(['int','float']).columns
        Menu = st.selectbox("Choisissez une variable",Variables_num)
        Mean = st.write(Data[Menu].max())

    elif Menu_analyse_statitiques == "Valeur min":
        Variables_num = Data.select_dtypes(['int','float']).columns
        Menu = st.selectbox("Choisissez une variable",Variables_num)
        Mean = st.write(Data[Menu].min())

    elif Menu_analyse_statitiques == "Somme":
        Variables_num = Data.select_dtypes(['int','float']).columns
        Menu = st.selectbox("Choisissez une variable",Variables_num)
        Mean = st.write(Data[Menu].sum())


    elif Menu_analyse_statitiques == "Médiane":
        Variables_num = Data.select_dtypes(['int','float']).columns
        Menu = st.selectbox("Choisissez une variable",Variables_num)
        Mean = st.write(Data[Menu].median())



    elif Menu_analyse_statitiques == "Quartile":
        Variables_num = Data.select_dtypes(['int','float']).columns
        Menu = st.selectbox("Choisissez une variable",Variables_num)
        Mean = st.write(Data[Menu].quantile([0.25,0.75]))

if Menu_box == "Manipulation de données":

    Choix = st.selectbox("Options",("Tri","Slicing","Renommer des colonnes","Supprimer des colonnes","Renommer des colonnes,"))

    #Tri sort values
    if Choix == "Tri":
        Variables_num = Data.select_dtypes(['int','float']).columns
        Choix_tri = st.radio("Triez vos données",options=["Tri croissant","Tri décroissant"])
        if Choix_tri == "Tri croissant":
            Choix_variable = st.selectbox("Définissez une variable",Variables_num)
            Tri_croissant = Data.sort_values(by=Choix_variable,axis=0,ascending=True,inplace=True)
            Ascending = st.write(Tri_croissant)
        #Sort_Values = Choix.sort_values()


        if Choix_tri == "Tri décroissant":
            Choix_variable = st.selectbox("Définissez une variable",Variables_num)
            Tri_croissant = Data.sort_values(by=Choix_variable,axis=0,ascending=False,inplace=True)
            Descending = st.write(Tri_croissant)

    if Choix == "Slicing":
        Choix_slicing = st.radio("Slicing",options=['Recherche par colonne','Recherche par ligne'])
        if Choix_slicing == "Recherche par colonne":
            Variables_slicing = Data.select_dtypes(['int','float']).columns
            Colonnes = st.selectbox("Choisissez une variable",Variables_slicing)
            Data.loc[Variables_slicing]


    if Choix == "Renommer des colonnes":
        with st.expander("Vous avez la possibilité de changer l'intitulé de vos variables"):
            st.write("Choisissez une ou plusieurs colonnes à renommer")
        col1,col2 = st.columns(2)
        with col1:
            Colonne = Data.select_dtypes(['int','float','object']).columns
            Option_colonne = st.selectbox("Définissez une variable à renommer",options=Colonne)
            st.write(Data.rename(Option_colonne))
        with col2:
            Colonnes = Data.select_dtypes(['int','float','object']).columns
            Option_colonnes = st.multiselectbox("Définissez les variables à renommer",options=Colonnes)
            st.write(Data.rename(Option_colonnes))



        




