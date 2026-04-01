# URL Shortener Service

A simple backend project built using Flask that converts long URLs into short links and redirects users to the original URL.

## 🚀 Features
- Generate short URLs from long URLs
- Redirect to original URL using short link
- REST API based implementation

## 🛠 Tech Stack
- Python
- Flask

## 📌 How to Run

1. Install dependencies:
   pip install flask

2. Run the server:
   python app.py

3. Open in browser:
   http://127.0.0.1:5000

## 📡 API Usage

### POST /shorten
Request:
{
  "url": "https://www.google.com"
}

Response:
{
  "short_url": "http://localhost:5000/1"
}

## 📖 Learning Outcome
This project demonstrates backend development concepts such as REST APIs, routing, and request handling using Flask.
