from fastapi import FastAPI, HTTPException
from nltk.sentiment import SentimentIntensityAnalyzer
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from loguru import logger

class Sentiment(BaseModel):
    text: str

app = FastAPI()
sia = SentimentIntensityAnalyzer()
logger.add("logs/sentiment_analysis.log", rotation="500 MB", level="INFO")

@app.post('/analyse_sentiment/')
def analyse_sentiment(sentiment: Sentiment):
    logger.info(f"Received text: {sentiment.text}")
    
    try:        
        sentiment_scores = sia.polarity_scores(sentiment.text)

        logger.info(f"Results: {sentiment_scores}")


        return JSONResponse(content=sentiment_scores)
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {e}")
        raise HTTPException(status_code=500, detail="Error analyzing sentiment")