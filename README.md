# Sentiment & Topic Tracker

A natural language processing project that analyzes sentiment and topics from Reddit or Twitter posts in real time.

## Features

- Scrape posts using APIs
- Run sentiment classification (via Hugging Face models)
- Topic modeling with BERTopic
- Interactive dashboard using Streamlit

## Folder Structure

sentiment-topic-tracker/
├── data/                 # Raw + processed data
├── notebooks/            # Jupyter notebooks for EDA
├── app/                  # Streamlit frontend
├── src/                  # Python scripts for scraping, modeling, etc.
├── tests/                # Optional unit tests
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

## Setup

### Install required packages

```bash```
pip install -r requirements.txt

---

###  **Initialize Git Locally**

```bash```
git init
git add .
git commit -m "Initial project layout and boilerplate"

### Clone the Repository

```bash```
git clone https://github.com/yourusername/sentiment-topic-tracker.git
cd sentiment-topic-tracker

### Create Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Run the Streamlit App (once it’s built)
streamlit run app/app.py

### Docker Setup (if using Docker)
```bash```
docker build -t sentiment-tracker .
docker run -p 8501:8501 sentiment-tracker