import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_tags import st_tags
from utils import data_process,data_procees_1
import joblib
import numpy as np

model= joblib.load('model.joblib')



st.set_page_config(page_title="My Webpage",page_icon=":bar_chart:", layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



st.markdown(""" <style> .blue { color:#0000FF ;}
</style> """, unsafe_allow_html=True)




with st.container():
    st.title("Prix de logement à Paris")
    st.write(
        "Vous  cherchez une location sur Paris? connaissez ici le prix au metre carré"
    )



with st.container():
    #st.write("---")
    left_column, right_column = st.columns(2)

    with st.container():
        #st.write("---")
        left_column, right_column = st.columns(2)
    with right_column:
         with st.container():

            st.write("---")


            quartier=st.text_input('Numero de quartier')

            st.write('Cherchez le numero de votre quartier ici [link](https://fr.wikipedia.org/wiki/Liste_des_quartiers_administratifs_de_Paris#:~:text=Les%2080%20quartiers%20administratifs%20constituent,parisien%20compte%20quatre%20quartiers%20administratifs.)')
            pieces=st.text_input('Nombre de pieces')
            construction=st.selectbox('Choisissez l anne de construction', ['1946-1970', '1971-1990','Apres 1990','Avant 1946'])
            meubles=st.selectbox('Choisissez', ['meublé', 'non mueblé'])

                #prix=[[quartier,pieces,construction, meubles]]

            button=st.button('Voir prix')

            if button:

                construction_process=data_process(construction)
                meubles_process=data_procees_1(meubles)
                prix=[[quartier,pieces,construction_process, meubles_process]]

                response=model.predict(prix)

                response=np.round(response, 2)




                st.markdown(f"<h3 class='blue'> Le prix au m2 de loyer est {response} euros </3>", unsafe_allow_html=True)
                #


    with left_column:


        lottie_image = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_MZPu87.json")

        st_lottie(lottie_image)
