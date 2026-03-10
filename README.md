# Sentiment Analysis

A Python application to analyze the sentiment of a text (positive, negative, neutral) using NLTK.

## Stack

- API: FastAPI
- UI: Streamlit
- NLTK (`SentimentIntensityAnalyzer`)
- Logging: Loguru
- Tests: pytest

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Download the required NLTK lexicon (one-time setup):

```bash
python -c "import nltk; nltk.download('vader_lexicon')"
```

## Run the project

1. Start the API:

```bash
uvicorn api:app --reload
```

2. In another terminal, start Streamlit (UI):

```bash
streamlit run app.py
```

3. Open the interface in your browser at `http://localhost:8501`.

## API

### `POST /analyse_sentiment/`

Example JSON body:

```json
{
  "text": "I love this product, it is really excellent!"
}
```

Example response:

```json
{
  "neg": 0.0,
  "neu": 0.4,
  "pos": 0.6,
  "compound": 0.82
}
```

## Tests

Install `pytest`:

```bash
pip install -U pytest
```

Run tests with `pytest`:

```bash
pytest
```

## Logs

Logs are written to `logs/sentiment_analysis.log`.

## Structure

- `api.py`: FastAPI backend
- `app.py`: Streamlit interface
- `requirements.txt`: Python dependencies
