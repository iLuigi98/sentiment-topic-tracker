# 📊 Sentiment & Topic Tracker

A natural language processing project that analyzes sentiment and topics from Reddit posts in real time. Built using Python, PRAW, Hugging Face Transformers, and Streamlit.

## 🚀 Features

- ✅ Scrape Reddit posts using Reddit API (PRAW)
- ✅ Save structured data to CSV
- 🚧 Sentiment classification with Hugging Face Transformers (in progress)
- 🚧 Topic modeling with BERTopic (coming soon)
- 🚧 Interactive dashboard using Streamlit

## 📁 Folder Structure

```
sentiment-topic-tracker/
├── data/            # Raw + processed data
├── notebooks/       # Jupyter notebooks for EDA
├── app/             # Streamlit frontend
├── src/             # Python scripts for scraping, modeling, etc.
├── tests/           # Optional unit tests
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sentiment-topic-tracker.git
cd sentiment-topic-tracker
```

### 2. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a file named `.env` in the root directory and add:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
```

### 5. Run the scraper

```bash
python src/scraper.py
```

This will fetch Reddit posts from a subreddit and save them to a CSV file in `data/`.


## 📌 Status & Roadmap

- [x] Reddit scraper + CSV export
- [ ] Sentiment analysis integration
- [ ] Topic modeling with BERTopic
- [ ] Streamlit dashboard for interaction
- [ ] Dockerization and deployment


## 🧠 About the Author

Built by Luigi Cheng as part of a data science portfolio project. For more projects, visit [luigidata.com](https://luigidata.com) or [@iLuigi98 on GitHub](https://github.com/iLuigi98).

---

## 📄 License

MIT License
