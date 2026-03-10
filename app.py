import streamlit as st
import requests
from loguru import logger

text = st.text_input("Enter text to analyze sentiment:")

if text:
    logger.info(f"Text to analyse: {text}")

    try:
        response = requests.post("http://localhost:8000/analyse_sentiment/", json={"text": text})

        response.raise_for_status()

        sentiment_scores = response.json()

        st.write("Résultat de l'analyse de sentiment:")
        st.write(f"Polarité positive: {sentiment_scores['pos']}")
        st.write(f"Polarité négative: {sentiment_scores['neg']}")
        st.write(f"Polarité neutre: {sentiment_scores['neu']}")
        st.write(f"Score composé: {sentiment_scores['compound']}")

        if sentiment_scores['compound'] >= 0.05:
            st.write("Sentiment global: Positif 🙂")
        elif sentiment_scores['compound'] <= -0.05:
            st.write("Sentiment global: Négatif 🙁")
        else:    st.write("Sentiment global: Neutre 😐")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
        logger.error(f"Error connecting to the API: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")
else:
    st.write("Please enter some text to analyze its sentiment")