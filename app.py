import streamlit as st
import requests
from loguru import logger

st.title ("Analyse de sentiment")

text = st.text_input("Entrer un texte pour analyser son sentiment:")

st.divider()

if text:
    logger.info(f"Text to analyse: {text}")

    try:
        response = requests.post("http://localhost:8000/analyse_sentiment/", json={"text": text})

        response.raise_for_status()

        sentiment_scores = response.json()

        st.header("Résultat de l'analyse de sentiment:")
        
        col1, col2 = st.columns(2);

        with col1:
            st.subheader(f"Polarité positive 🙂")
            st.badge(f"{sentiment_scores['pos']}", color="green")

            st.subheader(f"Polarité négative 🙁")
            st.badge(f"{sentiment_scores['neg']}", color="red")

        with col2:
            st.subheader(f"Polarité neutre 😐")
            st.badge(f"{sentiment_scores['neu']}", color="gray")

            st.subheader(f"Score composé 🎯")
            st.badge(f"{sentiment_scores['compound']}", color="blue")
        
        st.divider()

        if sentiment_scores['compound'] >= 0.05:
            st.success("Sentiment global: Positif 🙂")
        elif sentiment_scores['compound'] <= -0.05:
            st.error("Sentiment global: Négatif 🙁")
        else:    st.info("Sentiment global: Neutre 😐")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
        logger.error(f"Error connecting to the API: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")
else:
    st.write("Please enter some text to analyze its sentiment")