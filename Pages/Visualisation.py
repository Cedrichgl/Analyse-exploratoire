import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
#from streamlit_extras.metric_cards import style_metric_cards



# Page_one = st.Page(
#     page = "Pages/Dataset.py",
#     title= "Dataset"
# )

# Page_two = st.Page(
#     page = "Pages/Visualisation.py",
#     title= "Visualisation"
# )

# Page_three = st.Page(
#     page = "Pages/Analyse.py",
#     title= "Analyse"
# )


# Pages = st.navigation([Page_one,Page_two,Page_three])

#if Pages == "Visualisation":

st.title("Choisissez votre graphique")
st.write("Visualisation de données")
#from Main import Data
Data = st.session_state["df"]
Col_num = Data.select_dtypes(['int','float']).columns
Col_str = Data.select_dtypes('object').columns
#Choix = []
Choix = st.radio("Votre graphique",("Analyse bivariée", "Analyse univariée","Serie temporelles"))

#if Choix is not None:
    #st.write("Vous avez selectionnez :", Choix)


#Analyse univariée
if Choix is "Analyse univariée":
    with st.expander("Qu'est-ce qu'une analyse univariée ?"):
        st.subheader("Qu'est-ce qu'une analyse univariée ?",divider=True)
        st.write("L'analyse univariée a pour objectif de décrire et mesurer la répartition des valeurs que prendre une variable "
        "On appelle la répartition des valeurs d’une variable sa distribution , que l’on peut approximativement voir comme son "
        "«histogramme en continu». ")


    Analyse_univariee = st.sidebar.selectbox('Choisissez une option :',("Distribution en bar","Distribution en boxplot","Distribution en pie chart","Histogramme"))
    
    #distribution en bar
    if Analyse_univariee == "Distribution en bar":
        with st.expander("Comprendre la distribution en bar"):
            st.subheader("Comprendre la distribution en bar", divider=True)
            st.write("La distribution en bar montre très bien la répartition des valeurs d'une variable")
    
        

        #bar plot avec value counts
        #st.sidebar.subheader("Bar plot")
        Categ_var_options = Data.select_dtypes('object').columns
        Selectedcategcol = st.selectbox("Variable catégorielle",options=Categ_var_options)
        valuecountdef = Data[Selectedcategcol].value_counts(normalize=True)
        fig,axes =plt.subplots()
        valuecountdef.plot.bar(ax=axes)
        st.pyplot(fig,use_container_width=True)
        st.bar_chart(valuecountdef)


        #
    elif Analyse_univariee == "Distribution en boxplot":
       # """ Distribution = st.radio("Quel type de distribution",["boxplot","Pie Chart","Histogramme"])
        #if Distribution == "Boxplot": """
        with st.expander("Comprendre la distribution en boxplot"):
             st.subheader("Comprendre la distribution en Boxplot",divider=True)
             st.write("La distribution en boxplot est un moyen pratique d'afficher visuellement la distribution des données à travers leurs quartiles. Idéal pour identifier les valeurs abérantes d'une distribition.")
        Variable_distribution = Data.select_dtypes(['int','int64','float']).columns
        Select_variable_boxplot = st.selectbox("Variable",options=Variable_distribution)
        Boxplot = sns.boxplot(data=Data,x=Select_variable_boxplot)
        st.pyplot()

    elif Analyse_univariee == "Distribution en pie chart":
            with st.expander("Comprendre la répartition en pie chart"):
                 st.subheader("Comprendre la répartition en pie chart",divider=True)
                 st.write("Un pie chart (Diagramme circulaire) est un type de graphique dans lequel un cercle est divisé en secteurs qui représentent chacun une proportion de l’ensemble."
                 )

            Variable_distribution = Data.select_dtypes('object').columns
            #Categ_var_options = Data.select_dtypes('object').columns
            Select_variable_pie = st.selectbox("Variable",options=Variable_distribution)
            plt.pie(Select_variable_pie,labels=Select_variable_pie.index,shadow=True,autopct="%1.1f%%")
            st.pyplot()

    else:
            Analyse_univariee == "Histogramme"
            with st.expander("Comprendre la répartition par histogramme"):
                 st.subheader("Comprendre la réparition par histogramme", divider=True)
                 st.write("un histogramme est une représentation graphique permettant de représenter la répartition empirique d'une variable aléatoire ou d'une série statistique en la représentant avec des colonnes correspondant chacune à une classe et dont l'aire est proportionnelle à l'effectif de la classe")
            Variable_distribution = Data.select_dtypes(['int','float']).columns
            Select_variable_distrib = st.selectbox('Variable',options=Variable_distribution)
            Histogramme_slider = st.sidebar.slider(label="Tranches",min_value = 5, max_value = 100, value=30)
            Distplot = sns.displot(Data[Select_variable_distrib],bins=Histogramme_slider)
            st.pyplot()



elif Choix is "Analyse bivariée":
    Analyse_bivariee = st.sidebar.selectbox("Choisissez votre option",("Scatter plot","Analyse de corrélation","Analyse de régression", "Line_chart","Répartition par bar", "Test Anova"))
    #scatter
    if Analyse_bivariee == "Scatter plot":
        Variable_scatter = Data.select_dtypes(['int','float','object']).columns
        col1,col2,col3 = st.columns(3)
        with col1:
            X = st.selectbox("Définissez votre variable X",Variable_scatter)
        with col2:
            Y = st.selectbox("Définissez votre variable Y",Variable_scatter)
        with col3:
            Hue = st.selectbox("La variable couleur",Variable_scatter)
        sns.relplot(data=Data,x=X,y=Y,hue=Hue)
        st.pyplot()


        st.scatter_chart(
    Data,
    x=X,
    y=Y,
    color=Hue,
    #size="col3",
)

    elif Analyse_bivariee == "Répartition par bar":
         Variables_Bar = Data.select_dtypes(['int','float','object']).columns
         col1,col2,col3 = st.columns(3)
         with col1:
              X = st.selectbox('Définissez votre variable X',Variables_Bar)
         with col2:
              Y = st.selectbox("Définissez votre variable Y", Variables_Bar)
         with col3:
              Color = st.selectbox("Variable couleur",Variables_Bar)
         st.bar_chart(Data, x=X, y=Y, color=Color, horizontal=True)
         st.bar_chart(Data, x=X, y=Y, color=Color, stack=False)


              

    elif Analyse_bivariee == "Analyse de corrélation":
        options = ['Polar_chart','Heatmap','pairplot','clustermap']
        graphiques = st.pills("Choisissez votre matrice de correlation",options)
        if graphiques == "Polar_chart":
            Variable_heatmap = Data.select_dtypes(['int','float','object']).columns
            """ sns.heatmap(Variable_heatmap,annot=True)
            st.pyplot() """
            col1,col2,col3 = st.columns(3)
            with col1:
                 Menu_1 = st.selectbox("Définissez votre variable r",Variable_heatmap)
            with col2:
                 Menu_2 = st.selectbox("Définissez votre variable Theta",Variable_heatmap)
            with col3:
                 Color = st.selectbox("Choisissez votre variable couleur",Variable_heatmap)

            #graphique 
            fig = px.bar_polar(Data, r=Menu_1, theta=Menu_2, color=Color, template="plotly_dark",
            color_discrete_sequence= px.colors.sequential.Plasma_r)
            fig.show()

        
        elif graphiques == "pairplot":
            Pairplot = sns.PairGrid(Data)
            st.write(Pairplot)
            #st.pyplot()
    elif Analyse_bivariee == "Line_chart":
        with st.expander("L'objectif du Line_chart"):
             st.subheader("Comprendre le Line_chart",divider=True)
             st.write("Ce type de graphique permet de comparer plusieurs variables Y à une variable X.")
             Variables_Linechart = Data.select_dtypes(['int','float']).columns
        col1,col2 = st.columns(2)
        with col1:
             X = st.selectbox("Définissez votre variable X",Variables_Linechart)
        with col2:
             with st.expander("Vous devez définir au moins deux variables Y"):
                  st.write("")
             Y = st.multiselect("Choisissez vos variables Y", Variables_Linechart, max_selections = 10)
        
        st.line_chart(
        Data,
        x=X,
        y=Y,
        #color=["#FF0000", "#0000FF"],  # Optional
    )

      
    



    elif Analyse_bivariee == "Analyse de régression":
         Variable_regression = Data.select_dtypes(['int','float']).columns
         with st.expander("Comprendre l'analyse de régression"):
              st.subheader("Comprendre l'analyse de régression",divider=True)
              st.write("L'analyse de régression est une technique qui calcule la relation estimée entre une variable dépendante et une ou plusieurs variables explicatives")
         col1,col2 = st.columns(2)
         with col1:
              X = st.selectbox('Définissez votre variable X',Variable_regression)
         with col2:
              Y = st.selectbox("Définissez votre variable Y", Variable_regression)
         sns.regplot(x=X, y=Y, data=Data, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
         st.pyplot()
            
           
                   
                   


        #col1,col2,col3 = st.columns(3)
        #with col1:
            #Variable_heatmap = Data.select_dtypes(['int','float']).columns
            
            