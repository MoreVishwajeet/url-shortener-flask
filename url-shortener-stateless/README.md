# 🔗 URL Shortener

A lightweight and fast **URL Shortener service** built with **Node.js**, **Express.js**, **MongoDB**, and **EJS**. It allows users to convert long URLs into compact 8-character unique links, redirect seamlessly to the original destinations, and track total visits with detailed timestamp analytics.

---

## 🚀 Features

- ✂️ **Custom Short URLs**: Generates unique, compact 8-character nano IDs for long URLs.
- 🔁 **Duplicate Prevention**: Detects existing URLs in the database to prevent duplicate entries.
- 📊 **Visit Analytics & Tracking**: Records visit history and timestamp for each click.
- ⚡ **Instant Redirection**: Fast redirection to the original target URL.
- 🎨 **Server-Side Rendered UI**: Clean interface built with EJS for generating links and viewing live click metrics.
- 🔌 **RESTful API**: Supports both web UI form interactions and JSON API endpoints.

---

## 🛠️ Tech Stack

- **Runtime Environment:** [Node.js](https://nodejs.org/)
- **Web Framework:** [Express.js](https://expressjs.com/) (v5)
- **Database & ODM:** [MongoDB](https://www.mongodb.com/) with [Mongoose](https://mongoosejs.com/)
- **Template Engine:** [EJS](https://ejs.co/)
- **ID Generator:** [NanoID](https://github.com/ai/nanoid)
- **Dev Tooling:** [Nodemon](https://nodemon.io/)

---

## 📁 Project Structure

```text
url-shortener/
├── controllers/
│   └── url.js            # Controller logic for URL shortening, redirect, & analytics
├── models/
│   └── url.js            # Mongoose schema for shortId, redirectURL, & visitHistory
├── routes/
│   ├── staticRouter.js   # Route for rendering the home view (GET /)
│   └── url.js            # Routes for URL operations (POST /url, GET /url/:shortId, GET /url/analytics/:shortId)
├── views/
│   └── home.ejs          # EJS frontend template
├── connection.js         # MongoDB connection module
├── index.js              # Application entry point & server setup
├── package.json          # Dependencies and scripts
└── README.md             # Project documentation
```

---

## 📡 API Endpoints & Routes

| Method | Endpoint | Description | Response Type |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Renders the home page with the input form and list of all URLs | HTML / EJS |
| **POST** | `/url` | Accepts `{ url: "https://example.com" }` and generates a short ID | HTML / EJS |
| **GET** | `/url/:shortId` | Redirects to the original URL and records click timestamp | 302 Redirect |
| **GET** | `/url/analytics/:shortId` | Returns total clicks and visit history timestamp array | JSON |

### Example Analytics Response (`GET /url/analytics/:shortId`)

```json
{
  "totalClicks": 3,
  "analytics": [
    { "timestamp": 1727622800000 },
    { "timestamp": 1727622850000 },
    { "timestamp": 1727622910000 }
  ]
}
```

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have the following installed on your machine:
- [Node.js](https://nodejs.org/) (v16 or higher recommended)
- [MongoDB](https://www.mongodb.com/try/download/community) installed and running locally on port `27017`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MoreVishwajeet/url-shortener-flask.git
   cd url-shortener-flask
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start MongoDB:**
   Ensure your local MongoDB daemon is active:
   ```bash
   # Windows (via Services or mongod)
   mongod
   ```

4. **Run the server:**
   ```bash
   npm start
   ```

5. **Access the application:**
   Open your browser and navigate to:
   ```text
   http://localhost:8001
   ```

---

## 📝 Schema Reference

```javascript
const urlSchema = new mongoose.Schema({
  shortId: {
    type: String,
    required: true,
    unique: true
  },
  redirectURL: {
    type: String,
    required: true
  },
  visitHistory: [
    {
      timestamp: { type: Number }
    }
  ]
}, { timestamps: true });
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a PR.

---

## 📄 License

This project is licensed under the [ISC License](LICENSE) (or MIT).
